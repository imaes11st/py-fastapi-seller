from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

create_engine = create_engine(f"sqlite:///{sqlite_url}")

def get_session():
    with Session(create_engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]
        
        
        