from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

from app.db import repository, models, schemas
from app.db.database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# TODO: move to seperate file?
# Dependency
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/accommodations", response_model=list[schemas.Accommodation])
async def read_accommodations(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    db_accommodations = repository.list_accommodations(
        session,
        skip=skip,
        limit=limit
    )

    return db_accommodations

@app.get("/accommodations/{accommodation_id}", response_model=schemas.Accommodation)
async def read_accommodation(accommodation_id: str, session: Session = Depends(get_db)):
    db_accommodation = repository.get_accommodation(
        session,
        accommodation_id=accommodation_id
    )

    if db_accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")

    return db_accommodation


@app.get("/accommodations/{accommodation_id}/reviews", response_model=list[schemas.Review])
async def read_reviews(accommodation_id: str, skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    db_reviews = repository.list_reviews(
        session,
        accommodation_id=accommodation_id,
        skip=skip,
        limit=limit
    )

    return db_reviews

@app.get("/accommodations/{accommodation_id}/reviews/{review_id}", response_model=schemas.Review)
async def read_review(accommodation_id: str, review_id: str, session: Session = Depends(get_db)):
    db_review = repository.get_review(
        session,
        review_id=review_id,
        accommodation_id=accommodation_id
    )

    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    return db_review