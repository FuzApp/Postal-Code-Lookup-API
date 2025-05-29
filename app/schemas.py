from pydantic import BaseModel

class PostalCodeBase(BaseModel):
    state: str
    lga: str
    town: str
    district: str
    postal_code: str
    latitude: str
    longitude: str

class PostalCodeResponse(PostalCodeBase):
    id: int
    class Config:
        orm_mode = True
