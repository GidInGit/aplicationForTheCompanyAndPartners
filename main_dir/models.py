import datetime
from typing import Optional
from sqlalchemy.exc import IntegrityError
import sqlmodel
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session


class Company(sqlmodel.SQLModel, table=True):
    __tablename__ = "company"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
            sqlmodel.INT(),
            primary_key=True,
            autoincrement=True,
        )
    )
    name: str = sqlmodel.Field(nullable=False)

class Machinery(sqlmodel.SQLModel, table=True):
    __tablename__ = "machinary"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
        sqlmodel.INT(),
        primary_key=True,
        autoincrement=True,
        )
    )
    company: int = sqlmodel.Field(foreign_key="company.id")
    chip: int = sqlmodel.Field(default=None, index=True, nullable=True)
    name: str = sqlmodel.Field(max_length=50, nullable=False)
    state_number: str = sqlmodel.Field(max_length=50, nullable=False)
    is_work: bool = sqlmodel.Field(default=False)

class Object(sqlmodel.SQLModel, table=True):
    __tablename__ = "object"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
        sqlmodel.INT(),
        primary_key=True,
        autoincrement=True,
        )
    )
    company: int = sqlmodel.Field(foreign_key="company.id")
    name: str = sqlmodel.Field(nullable=False)
    address: str = sqlmodel.Field(nullable=False)
    start_time: datetime.time = sqlmodel.Field(nullable=False)
    end_time: datetime.time = sqlmodel.Field(nullable=False)
    x: float = sqlmodel.Field(nullable=False)
    y: float = sqlmodel.Field(nullable=False)
    radius: float = sqlmodel.Field(nullable=False)

class Foreman(sqlmodel.SQLModel, table=True):
    __tablename__ = "foreman"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
        sqlmodel.INT(),
        primary_key=True,
        autoincrement=True,
        )
    )
    company: int = sqlmodel.Field(foreign_key="company.id")
    object: int = sqlmodel.Field(foreign_key="object.id")
    bracelet: int = sqlmodel.Field(default=None, index=True, nullable=True)
    role: str = sqlmodel.Field(default="Бригадир")
    full_name: str = sqlmodel.Field(max_length=50, nullable=False)



class Employee(sqlmodel.SQLModel, table=True):
    __tablename__ = "employee"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
        sqlmodel.INT(),
        primary_key=True,
        autoincrement=True,
        )
    )
    company: int = sqlmodel.Field(foreign_key="company.id")
    object: int = sqlmodel.Field(foreign_key="object.id")
    foreman: int = sqlmodel.Field(foreign_key="foreman.id")
    bracelet: int = sqlmodel.Field(default=None, index=True, nullable=True)
    full_name: str = sqlmodel.Field(nullable=False)
    role: str = sqlmodel.Field(nullable=False)









sqlite_url = "postgresql://user:password@postgres/basic_microservice_db"

engine = create_engine(sqlite_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def _add_model(
    session: sqlmodel.Session, model: Company
) -> bool:
    """Adds model to the session. Returns true on success,
    false otherwise"""
    try:
        session.add(model)
    except IntegrityError:
        return False
    else:
        return True
