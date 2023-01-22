from week_1_basics_n_setup.docker_sql.ingest_csv_data.ingest_data import connect_postgresdb
from week_1_basics_n_setup.docker_sql.ingest_csv_data.ingest_data import ingest_csv_data
from unittest import TestCase

def test_connect_postgresdb():
    user = "root"
    password = "root"
    host = "localhost"
    port = "5432"
    db = "ny_taxi"
    engine = connect_postgresdb(user, password, host, port, db)
    assert engine.connect()


class ParserTest(TestCase):
    def __init__(self, user, password, host, port, db, table_name, url, nrows):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.table_name = table_name
        self.url = url
        self.nrows = nrows


def test_ingest_csv_data(capsys):
    user = "root"
    password = "root"
    host = "localhost"
    port = "5432"
    db = "ny_taxi"
    table_name = "yellow_taxi_trips"
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
    nrows = 10
    params = ParserTest(user, password, host, port, db, table_name, url, nrows)
    assert ingest_csv_data(params)==True