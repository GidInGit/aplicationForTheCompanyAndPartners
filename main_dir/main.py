from typing import List, Sequence, Tuple

import sqlmodel
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import Engine
from fastapi import FastAPI, Depends
from sqlmodel import Session

import models
from router_employee import router_employee
from router_machinery import router_machinery
from router_foreman import router_foreman
from router_company import router_company
from router_object import router_object
from models import Object
from models import engine, get_session

app = FastAPI(
    title="Builder"
)

@app.on_event("startup")
def on_startup():
    models.init_db()


app.include_router(router_object)
app.include_router(router_company)
app.include_router(router_foreman)
app.include_router(router_machinery)
app.include_router(router_employee)













@app.get("/object/{id}")
def get_object_name_and_address(
    id: int,
    *,
    session: Session = Depends(get_session)
) -> list[str]:
    """Gets a list of account names of a user"""
    statement = sqlmodel.select(models.Object.name, models.Object.address).where(
        models.Object.id == id,
    )

    result = session.exec(statement).fetchall()
    return result


