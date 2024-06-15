import asyncio
from concurrent.futures import ProcessPoolExecutor
from datetime import date, datetime

import pydantic
from fastapi import FastAPI, Response
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


class UseBracelet(pydantic.BaseModel):
    bracelet_id: int
    in_use: bool


@app.patch("/bracelet/use")
def use_bracelet(use: UseBracelet, response: Response):
    with sqlmodel.Session(engine) as s:
        s.exec(
            sqlmodel.update(Bracelet)
            .where(Bracelet.id == use.bracelet_id)
            .values(in_use=use.in_use)
        )
        s.commit()
        analytics = s.exec(
            sqlmodel.select(AnalyticsOfDay).where(
                AnalyticsOfDay.bracelet == use.bracelet_id
            )
        ).first()
        if analytics is None and not use.in_use:
            response.status_code = 500
            return
        elif analytics is None:
            analytics = AnalyticsOfDay(
                bracelet=use.bracelet_id,
                first_entry_time=datetime.now(),
                last_exit_time=None,
                time_out=0,
                time_untraceble=0,
                date=date.today(),
            )
            s.add(analytics)
        elif not use.in_use:
            analytics.last_exit_time = datetime.now()
            s.add(analytics)
        s.commit()


class PatchData(pydantic.BaseModel):
    bracelet_id: int
    x: int
    y: int
    pulse: int


class PatchBracelet(pydantic.BaseModel):
    object_x: int
    object_y: int
    object_r: int
    data: list[PatchData]


def process_bracelet(data: PatchBracelet, bracelet: PatchData):
    with sqlmodel.Session(engine) as s:
        analytics = s.exec(
            sqlmodel.select(AnalyticsOfDay).where(
                AnalyticsOfDay.bracelet == bracelet.bracelet_id,
                AnalyticsOfDay.date == date.today(),
            )
        ).first()
        if bracelet.pulse <= 10:
            analytics.time_untraceble += 30
        else:
            distance = geodesic(
                (data.object_x, data.object_y), (bracelet.x, bracelet.y)
            )
            if distance.km > data.object_r:
                analytics.time_out += 30
        s.add(analytics)
        s.commit()


@app.patch("/bracelet")
async def update_bracelets(data: PatchBracelet):
    with ProcessPoolExecutor(5) as pool:
        loop = asyncio.get_event_loop()
        await asyncio.gather(
            *(
                loop.run_in_executor(pool, process_bracelet, data, bracelet)
                for bracelet in data.data
            )
        )


@app.post("/bracelets/daily")
def daily_analitics(ids: list[int], date: date):
    with sqlmodel.Session(engine) as s:
        return s.exec(
            sqlmodel.select(AnalyticsOfDay).where(
                sqlmodel.col(AnalyticsOfDay.id).in_(ids),
                AnalyticsOfDay.date == date,
            )
        ).all()
