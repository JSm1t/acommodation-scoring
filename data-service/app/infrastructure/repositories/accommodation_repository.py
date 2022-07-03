
from sqlalchemy.orm import Session

from .helpers import is_valid_uuid
from ..models.Accommodation import Accommodation
from ...models import schemas

def list_accommodations(session: Session, skip: int = 0, limit: int = 100) -> list[schemas.Review]:
    return session.query(Accommodation).offset(skip).limit(limit).all()

def get_accommodation(session: Session, accommodation_id: str) -> schemas.Accommodation | None:
    if not is_valid_uuid(accommodation_id):
        return None

    return session.query(Accommodation).filter(Accommodation.id == accommodation_id).first()

def create_accommodation(session: Session, accommodation: schemas.Accommodation) -> None:
    db_accommodation = Accommodation(
      id=accommodation.id,
      type=accommodation.type,
      address_street=accommodation.address_street,
      address_zipcode=accommodation.address_zipcode,
      contact_phone=accommodation.contact_phone,
      contact_url=accommodation.contact_url,
      created_date=accommodation.created_date,
      updated_date=accommodation.updated_date,
    )

    session.add(db_accommodation)
    session.commit()
