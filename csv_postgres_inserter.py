from csv import reader, Sniffer
from psycopg2 import connect, sql
from dotenv import load_dotenv, find_dotenv
from os import getenv
from time import time

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

with open(csv_path, 'r') as csv_file:
    sniffer = Sniffer()
    delimiter = sniffer.sniff(csv_file.read(1000))
    read = reader(csv_file, delimiter=delimiter.delimiter)
    i=0
    next(read)
    for row in read:
        i+=1
        print("still running ", i)
        cur.execute(
            sql.SQL("INSERT INTO {} VALUES ({})").format(
                sql.Identifier(table),
                sql.SQL(', ').join(map(sql.Literal, row))
            )
        )
conn.commit()
cur.close()
conn.close()

end_time = time()

total_time = end_time - start_time
print ("finished in ", total_time, " seconds ")

