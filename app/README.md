# 🇳🇬 Nigeria Postal Code API

A RESTful API for accessing postal code data in Nigeria, with geolocation support using PostGIS.

## 🚀 Features

- FastAPI-powered backend
- PostgreSQL + PostGIS support
- Dockerized for ease of deployment
- CSV import of Nigerian postal codes with coordinates
- GIS querying support using `shapely` and `geoalchemy2`

## 📦 Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL + PostGIS
- Docker + Docker Compose
- Pandas, Shapely, Alembic

## 🧱 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/FuzApp/nigeria-postal-code-api.git
cd nigeria-postal-code-api

# Build and start services
docker-compose up --build

# Run database migrations
docker-compose exec web alembic upgrade head

# Import postal codes
docker-compose exec web python import_postal_codes.py
