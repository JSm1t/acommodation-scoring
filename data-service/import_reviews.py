from cgi import print_exception
import json
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.db.database import engine
from sqlalchemy.orm import Session
from app.db import models, repository
from psycopg2.errors import ForeignKeyViolation, UniqueViolation

with (
    open("data-service/reviews.json", encoding = 'utf-8') as file,
    Session(engine) as session
    ):
    json_object = json.loads(file.read());

    if (type(json_object) != list):
        print("JSON does not contain a list")

    for list_item in json_object:
        review_to_insert = models.Review(
            id=list_item['id'],
            accommodation_id=list_item['parents'][0]['id'],
            user_id=list_item['user']['id'],
            entry_date=datetime.fromtimestamp(list_item['entryDate'] / 1000),
            travel_date=datetime.fromtimestamp(list_item['travelDate'] / 1000),
            updated_date=datetime.fromtimestamp(list_item['updatedDate'] / 1000),
            locale=list_item['locale'],
            rating_general=list_item['ratings']['general']['general'],
            rating_location=list_item['ratings']['aspects']['location'],
            rating_service=list_item['ratings']['aspects']['service'],
            rating_price_quality=list_item['ratings']['aspects']['priceQuality'],
            rating_food=list_item['ratings']['aspects']['food'],
            rating_room=list_item['ratings']['aspects']['room'],
            rating_child_friendly=list_item['ratings']['aspects']['childFriendly'],
            rating_interior=list_item['ratings']['aspects']['interior'],
            rating_size=list_item['ratings']['aspects']['size'],
            rating_activities=list_item['ratings']['aspects']['activities'],
            rating_restaurants=list_item['ratings']['aspects']['restaurants'],
            rating_sanitary_state=list_item['ratings']['aspects']['sanitaryState'],
            rating_accessibility=list_item['ratings']['aspects']['accessibility'],
            rating_nightlife=list_item['ratings']['aspects']['nightlife'],
            rating_culture=list_item['ratings']['aspects']['culture'],
            rating_surrounding=list_item['ratings']['aspects']['surrounding'],
            rating_atmosphere=list_item['ratings']['aspects']['atmosphere'],
            rating_novice_ski_area=list_item['ratings']['aspects']['noviceSkiArea'],
            rating_apres_ski=list_item['ratings']['aspects']['apresSki'],
            rating_beach=list_item['ratings']['aspects']['beach'],
            rating_entertainment=list_item['ratings']['aspects']['entertainment'],
            rating_environmental=list_item['ratings']['aspects']['environmental'],
            rating_pool=list_item['ratings']['aspects']['pool'],
            rating_terrace=list_item['ratings']['aspects']['terrace'],
            rating_housing=list_item['ratings']['aspects']['housing'],
            rating_hygiene=list_item['ratings']['aspects']['hygiene'],
            status_published=list_item['status']['published'],
            status_checked=list_item['status']['checked'],
            status_reason=list_item['status']['reason'],
        )
  
        try:
            repository.create_review(session=session, review=review_to_insert)
        except IntegrityError as err:
            if isinstance(err.orig, ForeignKeyViolation):
                print("No accommodation found for id: {id}".format(id=review_to_insert.accommodation_id))
                pass
            elif isinstance(err.orig, UniqueViolation):
                print("Review with id: {id} already exists, skipping...".format(id=review_to_insert.accommodation_id))
                pass
            else:
                raise err

    print('Successfully inserted reviews')
