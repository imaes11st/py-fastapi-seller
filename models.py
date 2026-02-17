from pydantic import BaseModel


## CUSTOMER MODELS
class CustomerBase(BaseModel):
    name: str
    desc: str | None 
    email: str
    age: int
class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int | None = None
    
    
    
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
        
