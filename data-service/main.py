from typing import TypeVar
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

from app.infrastructure.repositories import accommodation_repository, review_repository
from app.models.schemas import PaginatedResponse, Accommodation, Review
from app.infrastructure.database import SessionLocal

app = FastAPI()

# TODO: move to seperate file?
# Dependency
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


T = TypeVar('T')

def create_paginated_response(list: list[T], skip: int, limit: int):
    return {
        'data': list,
        'meta': {
            'pagination': {
                'skip': skip,
                'limit': limit
            }
        }
    }

@app.get("/accommodations", response_model=PaginatedResponse[Accommodation])
async def read_accommodations(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    db_accommodations = accommodation_repository.list_accommodations(
        session,
        skip=skip,
        limit=limit
    )

    return create_paginated_response(db_accommodations, skip, limit)

@app.get("/accommodations/{accommodation_id}", response_model=Accommodation)
async def read_accommodation(accommodation_id: str, session: Session = Depends(get_db)):
    db_accommodation = accommodation_repository.get_accommodation(
        session,
        accommodation_id=accommodation_id
    )

    if db_accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")

    return db_accommodation


@app.get("/accommodations/{accommodation_id}/reviews", response_model=PaginatedResponse[Review])
async def read_reviews(accommodation_id: str, skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    db_reviews = review_repository.list_reviews(
        session,
        accommodation_id=accommodation_id,
        skip=skip,
        limit=limit
    )

    return create_paginated_response(db_reviews, skip, limit)

@app.get("/accommodations/{accommodation_id}/reviews/{review_id}", response_model=Review)
async def read_review(accommodation_id: str, review_id: str, session: Session = Depends(get_db)):
    db_review = review_repository.get_review(
        session,
        review_id=review_id,
        accommodation_id=accommodation_id
    )

    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    return db_review