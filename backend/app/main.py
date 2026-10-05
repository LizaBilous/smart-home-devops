from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sqlalchemy.orm import Session
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from .database import SessionLocal
from . import crud


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )


@app.get("/devices")
def get_devices(db: Session = Depends(get_db)):
    devices = crud.get_devices(db)

    return {
        device.id: {
            "id": device.id,
            "name": device.name,
            "status": device.status
        }
        for device in devices
    }


@app.post("/devices/{device_id}/toggle")
def toggle_device(device_id: int, db: Session = Depends(get_db)):
    device = crud.toggle_device(db, device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Устройство не найдено"
        )

    return {
        "status": "success",
        "device": {
            "id": device.id,
            "name": device.name,
            "status": device.status
        }
    }