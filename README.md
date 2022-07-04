 # Accomodation scoring service

The accommodation scoring service calculates a score for each accommodation based on the ratings of each review. It consists of two services:
 - Data service (written in python)
 - Scoring service (written in node.js)

## Installation
The data service requires python 3.10 to run.

To install the dependencies for the dataservice:
```sh
cd data-service
pipenv install
```

The scoring service requires node 16.15.1 to run.

To install the dependencies for the scoring service:
```sh
cd data-service
npm install
```


## Running the project locally
The data-service requires a PostgreSQL database to run. The provided docker-compose file in the root of the project can be used to launch a compatible database for the data service:
```sh
docker-compose up -d
```

The table structure for the data-service can be setup using `alembic` (installed with pipenv). Please set the correct database url in the `alembic.ini` file using `sqlalchemy.url` config option. To setup the table structure run:
```sh
alembic upgrade head
```

After creating the required tables and columns for the data-service, the tables can be filled up with some data. To allow the data-service to connect to the running PostgreSQL database, a `.env` file should be available to the application to read. An example `.env.example` can be found as reference.
Copy the `accommodations.json` and `reviews.json` to the data-service folder. Run:
```sh
python import_accommodations.py && python import_reviews.py
```
This should insert all accommodations and all reviews with one of the accommodations as parent in the database.

Starting the data-service can be done in the `data-service` directory via the following command:
```sh
uvicorn main:app
```
Using the .env.example as env file will let the data-service run locally at port 8000.

The scoring-service is written in typescript, and therefore needs to be build first before it can run:
```sh
npm run build && npm run start
```
Using the .env.example as env file will let the scoring-service run locally at port 6000.

To run the tests for the scoring service, run (this requires a `npm run build` before running the tests):
```sh
npm run test
```

## Routes

Data-service
 - /accommodations
 - /accommodations/{accommodation_id}
 - /accommodations/{accommodation_id}/reviews
 - /accommodations/{accommodation_id}/reviews/{review_id}

Scoring-service
 - /accommodations/{accommodation_id}/scores



## TODOs / Wishlist
Due to time constraints certain aspects of the project couldn't be fully finished. The following was on the wishlist to make the application more production ready and easier to work with:
 - Fetch all reviews instead of just a single large page
 - Complete docker-compose.yml file, including a data-service and scoring service. This allows starting the whole project with just a simple `docker-compose up`.
 - Set up a more complete testing suite for the data-service and scoring-service. Integration tests and e2e tests are missing.
 - Add better logging to both services, to allow for better monitoring.
 - The data-service is missing a linter / formatter.
 - CI to allow building and testing the project after each push.
