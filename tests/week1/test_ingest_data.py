from week_1_basics_n_setup.docker_sql.ingest_csv_data.ingest_data import connect_postgresdb


def test_connect_postgresdb():
    user = "root"
    password = "root"
    host = "localhost"
    port = "5432"
    db = "ny_taxi"
    engine = connect_postgresdb(user, password, host, port, db)
    assert engine.connect()