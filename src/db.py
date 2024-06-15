import datetime

import sqlmodel
import dotenv
import os


class Bracelet(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    company: int = sqlmodel.Field()
    rfid: str = sqlmodel.Field(
        sa_column=sqlmodel.Column(sqlmodel.VARCHAR(50), nullable=False)
    )
    in_use: bool = sqlmodel.Field()


class AnalyticsOfDay(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    bracelet: int = sqlmodel.Field()
    first_entry_time: datetime.datetime | None = sqlmodel.Field()
    last_exit_time: datetime.datetime | None = sqlmodel.Field()
    time_out: int = sqlmodel.Field()
    time_untraceble: int = sqlmodel.Field()
    date: datetime.date = sqlmodel.Field()


dotenv.load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = sqlmodel.create_engine(DATABASE_URL, echo=True)

sqlmodel.SQLModel.metadata.create_all(engine)
