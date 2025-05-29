import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, PostalCode
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

Base.metadata.create_all(bind=engine)

def import_csv(file_path):
    df = pd.read_csv(file_path)
    db: Session = SessionLocal()
    for _, row in df.iterrows():
        loc = from_shape(Point(float(row['longitude']), float(row['latitude'])), srid=4326)
        postal = PostalCode(
            state=row['state'],
            lga=row['lga'],
            town=row['town'],
            district=row['district'],
            postal_code=row['postal_code'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            location=loc
        )
        db.add(postal)
    db.commit()
    db.close()

if __name__ == "__main__":
    import_csv("postal_codes.csv")
