from sqlalchemy.orm import Session
from app import models

def get_by_postal_code(db: Session, code: str):
    return db.query(models.PostalCode).filter(models.PostalCode.postal_code == code).first()

def get_all_by_state(db: Session, state: str):
    return db.query(models.PostalCode).filter(models.PostalCode.state.ilike(state)).all()
