from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


# =====================================
# MANY TO MANY LINK TABLE (PRIMERO)
# =====================================

class CustomerPlan(SQLModel, table=True):
    customer_id: int = Field(foreign_key="customer.id", primary_key=True)
    plan_id: int = Field(foreign_key="plan.id", primary_key=True)


# =====================================
# PLAN
# =====================================

class Plan(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: int
    description: str | None = None

    customers: list["Customer"] = Relationship(
        back_populates="plans",
        link_model=CustomerPlan
    )


# =====================================
# CUSTOMER
# =====================================

class CustomerBase(SQLModel):
    name: str
    desc: str | None = None
    email: str
    age: int


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(SQLModel):
    name: str | None = None
    desc: str | None = None
    email: str | None = None
    age: int | None = None


class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    transactions: list["Transaction"] = Relationship(back_populates="customer")

    plans: list["Plan"] = Relationship(
        back_populates="customers",
        link_model=CustomerPlan
    )


# =====================================
# TRANSACTIONS
# =====================================

class TransactionBase(SQLModel):
    amount: int
    description: str


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")

    customer: "Customer" = Relationship(back_populates="transactions")


class TransactionCreate(TransactionBase):
    customer_id: int


# =====================================
# INVOICE (NO TABLE)
# =====================================

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]

    @property
    def total(self):
        return sum(transaction.amount for transaction in self.transactions)