from dotenv import load_dotenv, find_dotenv
from os import getenv
from time import time
import dask.dataframe as dataframe
from sqlalchemy import DATE, INT, String, create_engine

load_dotenv(find_dotenv())

start_time = time()

hostname = getenv("hostname")
username = getenv("username")
password = getenv("password")
database = getenv("database")

table = "stocks"
csv_path = "stock.csv"

engine = create_engine(f'postgresql://{username}:{password}@{hostname}/{database}')

data = dataframe.read_csv(csv_path)

print("opened in ", time() - start_time, " seconds")

data = data.compute()

data.to_sql(table, engine, if_exists='replace', index=False, dtype={
    'pointOfSale':String(255),
    'product': String(255),
    'date':DATE,
    'stock':INT 
})

engine.dispose()

total_time = time() - start_time
print ("finished in ", total_time, " seconds ")

