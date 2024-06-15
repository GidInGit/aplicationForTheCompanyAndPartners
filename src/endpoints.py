from concurrent.futures import ProcessPoolExecutor
from datetime import date, datetime

import pydantic
from fastapi import FastAPI
from geopy.distance import geodesic

from db import AnalyticsOfDay, Bracelet, engine, sqlmodel

app = FastAPI()


@app.get("/bracelet")
def get_bracelets(company_id: int) -> list[Bracelet]:
    with sqlmodel.Session(engine) as s:
        query = sqlmodel.select(Bracelet).where(Bracelet.company == company_id)
        return s.exec(query).all()


class BraceletCreate(pydantic.BaseModel):
    company_id: int
    rfid: str


class BraceletCreated(pydantic.BaseModel):
    id: int
    rfid: str


@app.post("/bracelet")
def add_bracelet(bracelet: BraceletCreate) -> BraceletCreated:
    new = Bracelet(
        company=bracelet.company_id, rfid=bracelet.rfid, in_use=False
    )
    with sqlmodel.Session(engine) as s:
        s.add(new)
        s.commit()
        return BraceletCreated(id=new.id, rfid=bracelet.rfid)


class ObjectData(pydantic.BaseModel):
    object_id: int
    object_x: int
    object_y: int
    object_r: int


class PatchData(pydantic.BaseModel):
    bracelet_id: int
    x: int
    y: int
    pulse: int


class PatchBracelet(pydantic.BaseModel):
    objects: list[ObjectData]
    bracelets: list[PatchData]


def process_bracelet(objects: list[ObjectData], bracelet: PatchData):
    with sqlmodel.Session(engine) as s:
        analytics = s.exec(
            sqlmodel.select(AnalyticsOfDay).where(
                AnalyticsOfDay.bracelet == bracelet.bracelet_id,
                AnalyticsOfDay.date == date.today(),
            )
        ).first()
        if analytics is None:
            analytics = AnalyticsOfDay(
                bracelet=bracelet.bracelet_id,
                first_entry_time=None,
                last_exit_time=None,
                time_worked=0,
            )
        if bracelet.pulse <= 10:
            return
        for object in objects:
            distance = geodesic(
                (object.object_x, object.object_y), (bracelet.x, bracelet.y)
            ).km
            if distance > object.object_r:
                continue
            analytics.time_worked += 30
            if analytics.first_entry_time is not None:
                analytics.first_entry_time = datetime.now()
                analytics.object_id = object.object_id
            break
        else:
            analytics.last_exit_time = datetime.now()
        s.add(analytics)
        s.commit()


@app.patch("/bracelet", status_code=201)
def update_bracelets(data: PatchBracelet):
    for object in data.objects:
        object.object_r = (object.object_r + 10) / 1000
    with ProcessPoolExecutor(5) as pool:
        pool.map(
            lambda bracelet: process_bracelet(data.objects, bracelet),
            data.bracelets,
        )


@app.get("/bracelets/daily")
def daily_analitics(object_id, date: date) -> list[AnalyticsOfDay]:
    with sqlmodel.Session(engine) as s:
        return s.exec(
            sqlmodel.select(AnalyticsOfDay).where(
                AnalyticsOfDay.object_id == object_id,
                AnalyticsOfDay.date == date,
            )
        ).all()
