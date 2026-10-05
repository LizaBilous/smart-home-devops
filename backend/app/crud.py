from sqlalchemy.orm import Session

from . import models


def get_devices(db: Session):
    return db.query(models.Device).all()


def toggle_device(db: Session, device_id: int):
    device = (
        db.query(models.Device)
        .filter(models.Device.id == device_id)
        .first()
    )

    if device is None:
        return None

    device.status = "on" if device.status == "off" else "off"

    db.commit()
    db.refresh(device)

    return device