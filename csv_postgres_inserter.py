from csv import reader, Sniffer, DictReader
from psycopg2 import connect, sql
from dotenv import load_dotenv, find_dotenv
from os import getenv
from time import time
import dask.dataframe as dataframe

load_dotenv(find_dotenv())

start_time = time()

hostname = getenv("hostname")
username = getenv("username")
password = getenv("password")

database = "bita"
table = "stocks"
csv_path = "stock.csv"

conn = connect(host=hostname, database=database, user=username, password=password)
cur = conn.cursor()

data = dataframe.read_csv(csv_path)

print("opened in ", time() - start_time, " seconds")

data = data.compute()

batch_size = 1000  
batch = []

for index, row in data.iterrows():
    batch.append(row)
    if i % batch_size == 0:
        cur.execute(
            sql.SQL("INSERT INTO {} VALUES {}").format(
                sql.Identifier(table),
                sql.SQL(', ').join(
                    sql.SQL('({})').format(sql.SQL(', ').join(map(sql.Literal, row))) for row in batch
                )
            )
        )
        conn.commit()
        batch = []

if batch:
    cur.execute(
        sql.SQL("INSERT INTO {} VALUES {}").format(
            sql.Identifier(table),
            sql.SQL(', ').join(
                sql.SQL('({})').format(sql.SQL(', ').join(map(sql.Literal, row))) for row in batch
            )
        )
    )
    conn.commit()
cur.close()
conn.close()

total_time = time() - start_time
print ("finished in ", total_time, " seconds ")

