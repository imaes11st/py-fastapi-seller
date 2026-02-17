from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    desc: str | None 
    email: str
    age: int
    
class Transaction(BaseModel):
        id: int
        amount: int
        date: str
        description: str
        
class Invoice(BaseModel):
        id: int
        customer_id: Customer
        transactions: list[Transaction]
        total: int
        
        @property
        def amount(self):
            return sum(transaction.amount for transaction in self.transactions) 
        
