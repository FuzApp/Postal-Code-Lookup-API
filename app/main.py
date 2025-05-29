from fastapi import FastAPI
from app.routers import lookup

app = FastAPI(title="Nigeria Postal Code API")
app.include_router(lookup.router)
