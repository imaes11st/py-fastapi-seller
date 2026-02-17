from fastapi import FastAPI
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

@app.post('/customer', response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get('/customers', response_model=list[Customer])
async def list_customers(session: SessionDep):
    return session.exec(Customer.select(Customer)).all()

#TRANSACTION
@app.get('/transaction')
async def create_transaction(transaction_data: Transaction):
    
    return transaction_data

#INVOICE
@app.get('/invoice')
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data







