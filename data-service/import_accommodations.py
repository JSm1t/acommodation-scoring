import os
import json
from datetime import datetime
from app.db.database import engine
from sqlalchemy.orm import Session
from app.db import schemas, repository

directory_location = os.getcwd();

with (
    open("data-service/accommodations.json", encoding = 'utf-8') as file,
    Session(engine) as session
):
    json_object = json.loads(file.read());

    if (type(json_object) != list):
        print("JSON does not contain a list")

    for list_item in json_object:
        accommodation_to_insert = schemas.Accommodation(
            id=list_item['id'],
            type=list_item['type'],
            address_street=list_item['address']['street'],
            address_zipcode=list_item['address']['zipcode'],
            contact_phone=list_item['contactInformation']['phone'],
            contact_email=list_item['contactInformation']['email'],
            contact_url=list_item['contactInformation']['url'],
            created_date=datetime.fromtimestamp(list_item['updatedDate'] / 1000),
            updated_date=datetime.fromtimestamp(list_item['updatedDate'] / 1000),
        )

        repository.create_accommodation(session=session, accommodation=accommodation_to_insert)
