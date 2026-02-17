from fastapi import FastAPI, HTTPException, status

from datetime import datetime
from zoneinfo import ZoneInfo
from models import Customer, CustomerCreate, Transaction, Invoice
from  db import SessionDep, create_all_tables
from sqlmodel import select
    
app = FastAPI(lifespan=create_all_tables)

@app.get("/")
async def root():
    return {"message": "Configuration Fast API"}

country_timezones = {
    "NI": "America/Managua",              # Nicaragua
    "CO": "America/Bogota",               # Colombia
    "MX": "America/Mexico_City",          # México
    "AR": "America/Argentina/Buenos_Aires", # Argentina
    "PE": "America/Lima",                 # Perú
    "US": "America/New_York",             # Estados Unidos
    "ES": "Europe/Madrid",                # España
    "JP": "Asia/Tokyo",                   # Japón
    "AU": "Australia/Sydney",             # Australia
    "BR": "America/Sao_Paulo"             # Brasil
}

@app.get('/time/{iso_code}')
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = ZoneInfo(timezone_str) 
    return { "time": datetime.now(tz) }

#CUSTOMER

db_customers: list[Customer] = []

@app.post('/customers', response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get('/customers/{customer_id}', response_model=Customer)
async def read_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist"
        ) 
    return customer_db

@app.delete('/customers/{customer_id}')
async def delete_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer does not exist"
        ) 
    session.delete(customer_db)
    session.commit()
    return {"detail": "Customer deleted successfully"}

@app.get('/customers', response_model=list[Customer])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()

#TRANSACTION
@app.post('/transactions')
async def create_transaction(transaction_data: Transaction):
    
    return transaction_data

#INVOICE
@app.post('/invoices')
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data







