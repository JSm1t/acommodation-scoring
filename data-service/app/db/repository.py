from sqlalchemy.orm import Session

from . import models, schemas

def list_accommodations(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.Accommodation).offset(skip).limit(limit).all()

def get_accommodation(session: Session, accommodation_id: int):
    return session.query(models.Accommodation).filter(models.Accommodation.id == accommodation_id).first()

def create_accommodation(session: Session, accommodation: schemas.Accommodation):
    db_accommodation = models.Accommodation(
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

def list_reviews(session: Session, accommodation_id: str, skip: int = 0, limit: int = 100):
    return session.query(models.Review).filter(models.Review.accommodation_id == accommodation_id).offset(skip).limit(limit).all()

def get_review(session: Session, accommodation_id: str, review_id: str):
    return session.query(models.Accommodation).filter(models.Review.id == review_id).filter(models.Accommodation.id == accommodation_id).first()

def create_review(session: Session, review: schemas.Review):
    db_review = models.Review(
      id=review.id,
      accommodation_id=review.accommodation_id,
      user_id=review.user_id,
      entry_date=review.entry_date,
      travel_date=review.travel_date,
      updated_date=review.updated_date,
      locale=review.locale,
      rating_general = review.rating_general,
      rating_location = review.rating_location,
      rating_service = review.rating_service,
      rating_price_quality = review.rating_price_quality,
      rating_food = review.rating_food,
      rating_room = review.rating_room,
      rating_child_friendly = review.rating_child_friendly,
      rating_interior = review.rating_interior,
      rating_size = review.rating_size,
      rating_activities = review.rating_activities,
      rating_restaurants = review.rating_restaurants,
      rating_sanitary_state = review.rating_sanitary_state,
      rating_accessibility = review.rating_accessibility,
      rating_nightlife = review.rating_nightlife,
      rating_culture = review.rating_culture,
      rating_surrounding = review.rating_surrounding,
      rating_atmosphere = review.rating_atmosphere,
      rating_novice_ski_area = review.rating_novice_ski_area,
      rating_apres_ski = review.rating_apres_ski,
      rating_beach = review.rating_beach,
      rating_entertainment = review.rating_entertainment,
      rating_environmental = review.rating_environmental,
      rating_pool = review.rating_pool,
      rating_terrace = review.rating_terrace,
      rating_housing = review.rating_housing,
      rating_hygiene = review.rating_hygiene,
      status_published = review.status_published,
      status_checked = review.status_checked,
      status_reason = review.status_reason
    )

    session.add(db_review)

    try:
        session.commit()
    except Exception as err:
        session.rollback()
        raise err