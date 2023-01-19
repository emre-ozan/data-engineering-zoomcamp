## Related Part in the Project
![Week 1 - Overview](../../docs/week1/week1_overview.jpg)

## Data pipelines (Ingesting NY Taxi CSV Data to Postgres DB)

A **data pipeline** is an automated system to do an ETL (Extract, Transform, Load) with data. For this project, We firstly read CSV files, we store the data in a PostgreSQL database (DB) with a convenient schema. Becuase of that, we need a postgresql DB. We will create a postgres DB in a docker container.

![data pipeline](../../docs/week1/01_01.png)

## Connecting pgAdmin and Postgres

pgcli is a handy tool for managing postgres DB but it's cumbersome to use. pgAdmin is a web-based tool that makes it more convenient to access and manage our DB. We will create also a pgadmin tool in a docker container to access the postgres DB visually from the web broser. 

![data pipeline](../../docs/week1/pgadmin4.jpg)

### Connect the postgres DB from pgadmin

![data pipeline](../../docs/week1/pgadmin5.jpg)


## Ingest CSV data to Postgres DB (Pandas and Sqlalchemy in Python)

- Read CSV files and transform data with Pandas.
- Connect Postgres DB and insert data into DB with Sqlalchemy.


## Installation
- Run the docker images for postgres database and management tool
```
docker-compose up -d
```
- Build and run a docker image to ingest csv files into postgres DB
```
docker build -t ingest_taxi:v001 .
export URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
docker run -it \
  --network=postgresdb_connection \
  ingest_taxi:v001 \
  --user=root \
  --password=root \
  --host=pgdatabase \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url="${URL}"
```