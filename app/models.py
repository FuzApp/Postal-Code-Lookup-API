from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from app.database import Base

class PostalCode(Base):
    __tablename__ = "postal_codes"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, index=True)
    lga = Column(String)
    town = Column(String)
    district = Column(String)
    postal_code = Column(String, index=True)
    latitude = Column(String)
    longitude = Column(String)
    location = Column(Geometry(geometry_type="POINT", srid=4326))
