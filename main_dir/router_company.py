from fastapi import APIRouter
from typing import List, Sequence, Tuple

import sqlmodel
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import Engine
from fastapi import FastAPI, Depends
from sqlmodel import Session

import models

from models import Object, _add_model
from models import engine, get_session

router_company = APIRouter(
    prefix="/company",
    tags=["Company"]
)


@router_company.post("")
def add_company(company: models.Company, session: Session = Depends(get_session)) -> bool:
    """Adds account to the database. Returns true on success,
    false otherwise"""
    result = _add_model(session, company)
    session.commit()
    return result


@router_company.get("")
def get_company_names(
        session: Session = Depends(get_session)
) -> Sequence[models.Company]:
    """Gets a list of account names of a user"""
    statement = sqlmodel.select(models.Company)

    result = session.exec(statement).fetchall()
    return result


@router_company.get("/{id}")
def get_object_name_and_address(
        id: int,
        *,
        session: Session = Depends(get_session)
) -> Sequence[models.Company]:
    """Gets a list of account names of a user"""
    statement = sqlmodel.select(models.Company).where(
        models.Company.id == id,
    )

    result = session.exec(statement).fetchall()
    return result
