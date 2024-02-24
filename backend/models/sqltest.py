import psycopg2
conn_string = "host='152.23.211.102' dbname='pearlhacks' user='postgres' password='MasterYoshi1!'"
conn = psycopg2.connect(conn_string)

with conn:
    with conn.cursor() as curs:
        curs.execute("DROP TABLE pearl;")
