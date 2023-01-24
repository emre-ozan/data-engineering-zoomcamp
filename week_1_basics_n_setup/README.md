## Related Part in the Project
![Week 1 - Overview](../docs/week1/week1_overview.jpg)

## Data pipelines

Our task is to create a data pipeline for this week. A **data pipeline** is an automated system to do an ETL (Extract, Transform, Load) with data. We firstly read CSV files, store the data in a PostgreSQL database (DB) with a convenient schema. We need a postgresql DB. We create a postgres DB in a docker container. And then we explore data with sql commands.

However, **we will not use postgres for the rest of the project**. Instead of storing data in the postgres DB, we transform them into parquet format and store in the google cloud storage (GCS).


![data pipeline](../docs/week1/01_01.png)


### Docker + Postgres

[Code](2_docker_sql)

* [Introduction to Docker](https://www.youtube.com/watch?v=EYNwNlOrpr0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * Why do we need Docker
  * Creating a simple "data pipeline" in Docker
* [Ingesting NY Taxi Data to Postgres](https://www.youtube.com/watch?v=2JM-ziJt0WI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * Running Postgres locally with Docker
  * Using `pgcli` for connecting to the database
  * Exploring the NY Taxi dataset
  * Ingesting the data into the database
  * **Note** if you have problems with `pgcli`, check [this video](https://www.youtube.com/watch?v=3IkfkTwqHx4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
    for an alternative way to connect to your database
* [Connecting pgAdmin and Postgres](https://www.youtube.com/watch?v=hCAIVe9N0ow&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * The pgAdmin tool
  * Docker networks
* [Putting the ingestion script into Docker](https://www.youtube.com/watch?v=B1WwATwf-vY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * Converting the Jupyter notebook to a Python script
  * Parametrizing the script with argparse
  * Dockerizing the ingestion script
* [Running Postgres and pgAdmin with Docker-Compose](https://www.youtube.com/watch?v=hKI6PkPhpa0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * Why do we need Docker-compose
  * Docker-compose YAML file
  * Running multiple containers with `docker-compose up`
* [SQL refresher](https://www.youtube.com/watch?v=QEcps_iskgg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * Adding the Zones table
  * Inner joins
  * Basic data quality checks
  * Left, Right and Outer joins
  * Group by
* Optional: If you have some problems with docker networking, check [Port Mapping and Networks in Docker](https://www.youtube.com/watch?v=tOr4hTsHOzU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  * Docker networks
  * Port forwarding to the host environment
  * Communicating between containers in the network
  * `.dockerignore` file

