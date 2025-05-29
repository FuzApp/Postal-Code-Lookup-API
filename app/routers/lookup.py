from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/lookup", response_model=schemas.PostalCodeResponse)
def lookup_postal_code(code: str, db: Session = Depends(get_db)):
    return crud.get_by_postal_code(db, code)
