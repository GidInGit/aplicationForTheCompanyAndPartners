# from fastapi import APIRouter
# from typing import List, Sequence, Tuple
#
# import sqlmodel
# from sqlalchemy import create_engine
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.future import Engine
# from fastapi import FastAPI, Depends
# from sqlmodel import Session
#
# import models
#
# from models import Object, _add_model
# from models import engine, get_session
#
# router_foreman = APIRouter(
#     prefix="/foreman",
#     tags=["Foreman"]
# )
#
#
# @router_foreman.post("")
# def add_object(foreman: models.Foreman, session: Session = Depends(get_session)) -> bool:
#     """Adds account to the database. Returns true on success,
#     false otherwise"""
#     result = _add_model(session, foreman)
#     session.commit()
#     return result
#
#
# @router_foreman.get("")
# def get_object_name_and_address(
#         session: Session = Depends(get_session)
# ) -> Sequence[models.Foreman]:
#     """Gets a list of account names of a user"""
#     statement = sqlmodel.select(models.Foreman)
#
#     result = session.exec(statement).fetchall()
#     return result
#
#
# @router_foreman.get("/{id}")
# def get_object_name_and_address(
#         id: int,
#         *,
#         session: Session = Depends(get_session)
# ) -> Sequence[models.Foreman]:
#     """Gets a list of account names of a user"""
#     statement = sqlmodel.select(models.Foreman).where(
#         models.Foreman.id == id,
#     )
#
#     result = session.exec(statement).fetchall()
#     return result
