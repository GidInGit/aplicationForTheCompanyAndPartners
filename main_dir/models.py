import datetime
from typing import Optional
from sqlalchemy.exc import IntegrityError
import sqlmodel
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session


def get_time():
    time = datetime.datetime.now()
    return datetime.time(
        hour=time.hour, minute=time.minute
    )



class Object(sqlmodel.SQLModel, table=True):
    __tablename__ = "object"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
        sqlmodel.INT(),
        primary_key=True,
        autoincrement=True,
        )
    )
    name: str = sqlmodel.Field(nullable=False)
    address: str = sqlmodel.Field(nullable=False)




class Employee(sqlmodel.SQLModel, table=True):
    __tablename__ = "employee"
    id: Optional[int] = sqlmodel.Field(sa_column=sqlmodel.Column(
        sqlmodel.INT(),
        primary_key=True,
        autoincrement=True,
        )
    )
    name: str = sqlmodel.Field(nullable=False)
    is_enter: str = sqlmodel.Field(nullable=False)
    date: datetime.date = sqlmodel.Field(default_factory=datetime.date.today, nullable=False)
    time: datetime.time = sqlmodel.Field(default_factory=get_time, nullable=False)









sqlite_url = "postgresql://user:password@postgres/basic_microservice_db"

engine = create_engine(sqlite_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def _add_model(
    session: sqlmodel.Session, model: Object
) -> bool:
    """Adds model to the session. Returns true on success,
    false otherwise"""
    try:
        session.add(model)
    except IntegrityError:
        return False
    else:
        return True
