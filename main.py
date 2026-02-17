from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
from models import Customer, Transaction, Invoice
    
app = FastAPI()

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
@app.get('/customer')
async def create_customer(customer_data: Customer):
    
    return customer_data

#TRANSACTION
@app.get('/transaction')
async def create_transaction(transaction_data: Transaction):
    
    return transaction_data

#INVOICE
@app.get('/invoice')
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data







