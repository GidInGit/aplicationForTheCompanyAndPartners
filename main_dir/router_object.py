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

router_object = APIRouter(
    prefix="/objects",
    tags=["Objects"]
)


@router_object.post("")
def add_object(object: models.Object, session: Session = Depends(get_session)) -> bool:
    """Adds account to the database. Returns true on success,
    false otherwise"""
    result = _add_model(session, object)
    session.commit()
    return result


@router_object.get("")
def get_object_name_and_address(
        session: Session = Depends(get_session)
) -> Sequence[Object]:
    """Gets a list of account names of a user"""
    statement = sqlmodel.select(models.Object)

    result = session.exec(statement).fetchall()
    return result


@router_object.get("/{id}")
def get_object_name_and_address(
        id: int,
        *,
        session: Session = Depends(get_session)
) -> Sequence[Object]:
    """Gets a list of account names of a user"""
    statement = sqlmodel.select(models.Object).where(
        models.Object.id == id,
    )

    result = session.exec(statement).fetchall()
    return result
