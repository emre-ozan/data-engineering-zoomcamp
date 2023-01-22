# Data Engineering Zoomcamp 2023

## Technical Tasks in the Project
### ETL (Extract, Transform, Load)
- Do an ETL. Extract New York City data (CSV files), Transform it, and Load data Google Cloud Storage like a data lake.
### Batch Analysis
- Move data from google data storage to Google Bigquery (Data Warehouse). Transform data with DBT in Google Biguqery. Visulize data with Google Data Studio to show analyzes.
### Streaming Analytics
- Transform data in Google Cloud Storage with Spark. Firstly create a Kafka producer to have a streaming data. And then thanks to the Kafka consumer, have data and show streaming analyzes
### Orchestrate Spark Jobs
- [New york taxi data](docs/dataset.md) is a big data, it consists of a lot of csv files. We will orchestrate spark jobs with Prefect to extract data.


## Overview
### Architecture diagram
<img src="docs/architecture/arch_1.jpg"/>



## Syllabus Topics

* [Week 1: Introduction & Prerequisites](#week-1-introduction--prerequisites)
* [Week 2: Data ingestion](#week-2-data-ingestion)
* [Week 3: Data Warehouse](#week-3-data-warehouse)
* [Week 4: Analytics Engineering](#week-4-analytics-engineering)
* [Week 5: Batch processing](#week-5-batch-processing)
* [Week 6: Streaming](#week-6-streaming)
* [Week 7, 8 & 9: Project](#week-7-8--9-project)

### 2023 Cohort

* **Start Date**: 16 January 2023

## Syllabus Details

> **Note:** NYC TLC changed the format of the data we use to parquet. But you can still access 
> the csv files [here](https://github.com/DataTalksClub/nyc-tlc-data).

### [Week 1: Introduction & Prerequisites](week_1_basics_n_setup)

* Course overview
* Introduction to GCP
* Docker and docker-compose 
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course
* Homework

[More details](week_1_basics_n_setup)


### [Week 2: Workflow Orchestration](week_2_workflow_orchestration/)

* Data Lake
* Workflow orchestration
* Introduction to Prefect
* ETL with GCP & Prefect
* Parametrizing workflows
* Prefect Cloud and additional resources 
* Homework

[More details](week_2_workflow_orchestration/)


### [Week 3: Data Warehouse](week_3_data_warehouse)


* Data Warehouse
* BigQuery
* Partitioning and clustering
* BigQuery best practices
* Internals of BigQuery
* Integrating BigQuery with Airflow
* BigQuery Machine Learning

[More details](week_3_data_warehouse)


### [Week 4: Analytics engineering](week_4_analytics_engineering/)

* Basics of analytics engineering
* dbt (data build tool)
* BigQuery and dbt
* Postgres and dbt
* dbt models
* Testing and documenting
* Deployment to the cloud and locally
* Visualizing the data with google data studio and metabase 


[More details](week_4_analytics_engineering)


### [Week 5: Batch processing](week_5_batch_processing)

* Batch processing 
* What is Spark
* Spark Dataframes
* Spark SQL
* Internals: GroupBy and joins

[More details](week_5_batch_processing)

### [Week 6: Streaming](week_6_stream_processing)

* Introduction to Kafka
* Schemas (avro)
* Kafka Streams
* Kafka Connect and KSQL

[More details](week_6_stream_processing)


### [Week 7, 8 & 9: Project](week_7_project)

Putting everything we learned to practice

* Week 7 and 8: working on your project
* Week 9: reviewing your peers

[More details](week_7_project)


## Other Details

### Technologies
* *Google Cloud Platform (GCP)*: Cloud-based auto-scaling platform by Google
  * *Google Cloud Storage (GCS)*: Data Lake
  * *BigQuery*: Data Warehouse
* *Terraform*: Infrastructure-as-Code (IaC)
* *Docker*: Containerization
* *SQL*: Data Analysis & Exploration
* *Airflow*: Pipeline Orchestration
* *dbt*: Data Transformation
* *Spark*: Distributed Processing
* *Kafka*: Streaming


## Instructors
- Ankush Khanna (https://linkedin.com/in/ankushkhanna2)
- Sejal Vaidya (https://linkedin.com/in/vaidyasejal)
- Victoria Perez Mola (https://www.linkedin.com/in/victoriaperezmola/)
- Alexey Grigorev (https://linkedin.com/in/agrigorev)

## Tools 

For this course, you'll need to have the following software installed on your computer:

* Docker and Docker-Compose
* Python 3 (e.g. via [Anaconda](https://www.anaconda.com/products/individual))
* Google Cloud SDK 
* Terraform

See [Week 1](week_1_basics_n_setup) for more details about installing these tools
