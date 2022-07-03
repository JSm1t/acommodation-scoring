from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from .database import Base

class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    names = Column(JSON)
    type = Column(String)
    geo = Column(JSON)
    stars = Column(Integer)
    address_street = Column(String)
    address_zipcode = Column(String)
    contact_phone = Column(String)
    contact_email = Column(String)
    contact_url = Column(String)
    created_date = Column(DateTime, default=datetime.now())
    updated_date = Column(DateTime, default=datetime.now())

class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    accommodation_id = Column(UUID(as_uuid=True), ForeignKey("accommodations.id"), index=True)
    user_id = Column(String)
    titles = Column(JSON)
    texts = Column(JSON)
    entry_date = Column(DateTime)
    travel_date = Column(DateTime)
    updated_date = Column(DateTime)
    locale = Column(String)
    rating_general = Column(Integer, nullable=True)
    rating_location = Column(Integer, nullable=True)
    rating_service = Column(Integer, nullable=True)
    rating_price_quality = Column(Integer, nullable=True)
    rating_food = Column(Integer, nullable=True)
    rating_room = Column(Integer, nullable=True)
    rating_child_friendly = Column(Integer, nullable=True)
    rating_interior = Column(Integer, nullable=True)
    rating_size = Column(Integer, nullable=True)
    rating_activities = Column(Integer, nullable=True)
    rating_restaurants = Column(Integer, nullable=True)
    rating_sanitary_state = Column(Integer, nullable=True)
    rating_accessibility = Column(Integer, nullable=True)
    rating_nightlife = Column(Integer, nullable=True)
    rating_culture = Column(Integer, nullable=True)
    rating_surrounding = Column(Integer, nullable=True)
    rating_atmosphere = Column(Integer, nullable=True)
    rating_novice_ski_area = Column(Integer, nullable=True)
    rating_apres_ski = Column(Integer, nullable=True)
    rating_beach = Column(Integer, nullable=True)
    rating_entertainment = Column(Integer, nullable=True)
    rating_environmental = Column(Integer, nullable=True)
    rating_pool = Column(Integer, nullable=True)
    rating_terrace = Column(Integer, nullable=True)
    rating_housing = Column(Integer, nullable=True)
    rating_hygiene = Column(Integer, nullable=True)
    status_published = Column(Boolean)
    status_checked = Column(Boolean)
    status_reason = Column(String)
  