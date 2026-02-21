from http.client import HTTPException
import time

from typing import Annotated
from fastapi import FastAPI, Request, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
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

security = HTTPBasic()

@app.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print(credentials)
    if credentials.username != "admin" or credentials.password != "admin":
        return {"message": f"Hola, {credentials.username}!"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data







