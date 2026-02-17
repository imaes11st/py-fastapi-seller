from pydantic import BaseModel
from sqlmodel import SQLModel, Field


## CUSTOMER MODELS
class CustomerBase(SQLModel):
    name: str = Field(default=None)
    desc: str | None = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)
class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    
    
## TRANSACTION MODELS
class Transaction(BaseModel):
        id: int
        amount: int
        date: str
        description: str
      
## INVOICE MODELS  
class Invoice(BaseModel):
        id: int
        customer_id: Customer
        transactions: list[Transaction]
        total: int
        
        @property
        def amount(self):
            return sum(transaction.amount for transaction in self.transactions) 
        
