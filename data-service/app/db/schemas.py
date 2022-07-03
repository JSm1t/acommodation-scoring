from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class Review(BaseModel):
    id: UUID
    accommodation_id: UUID
    #titles: json
    user_id: str
    #texts: json
    entry_date: datetime
    travel_date: datetime
    updated_date: datetime
    locale: str
    rating_general: int | None
    rating_location: int | None
    rating_service: int | None
    rating_price_quality: int | None
    rating_food: int | None
    rating_room: int | None
    rating_child_friendly: int | None
    rating_interior: int | None
    rating_size: int | None
    rating_activities: int | None
    rating_restaurants: int | None
    rating_sanitary_state: int | None
    rating_accessibility: int | None
    rating_nightlife: int | None
    rating_culture: int | None
    rating_surrounding: int | None
    rating_atmosphere: int | None
    rating_novice_ski_area: int | None
    rating_apres_ski: int | None
    rating_beach: int | None
    rating_entertainment: int | None
    rating_environmental: int | None
    rating_pool: int | None
    rating_terrace: int | None
    rating_housing: int | None
    rating_hygiene: int | None
    status_published: bool
    status_checked: bool
    status_reason: str

    class Config:
        orm_mode = True

class Accommodation(BaseModel):
    id: UUID | None
    # names: json
    type: str
    # geo: json
    address_street: str
    address_zipcode: str
    contact_phone: str | None
    contact_email: str | None
    contact_url: str | None
    created_date: datetime
    updated_date: datetime
    reviews: list[Review] = []

    class Config:
        orm_mode = True
