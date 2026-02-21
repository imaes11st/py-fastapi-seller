import time

from fastapi import FastAPI, Request
from sqlmodel import select

from  db import SessionDep, create_all_tables
from models import Invoice, Transaction

from app.routers import customers, transactions, plans

app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(plans.router) 


@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} - Complete in {process_time:.4f} seconds")
    return response


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI project!"}


@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data







