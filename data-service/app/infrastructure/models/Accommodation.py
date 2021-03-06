from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..database import Base
from . import Review

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

    reviews = relationship("Review", cascade="all, delete", lazy='noload')
