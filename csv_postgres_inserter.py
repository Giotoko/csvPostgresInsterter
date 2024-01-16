from dotenv import load_dotenv, find_dotenv
from os import getenv
from time import time
from sqlalchemy import DATE, INT, String, create_engine
from polars import read_csv

load_dotenv(find_dotenv())

start_time = time()

hostname = getenv("hostname")
username = getenv("username")
password = getenv("password")
database = getenv("database")

def csv_postgres_inserter(table="", csv_path="", separator=","):
    try:
        engine = create_engine(f'postgresql://{username}:{password}@{hostname}/{database}')

        data = read_csv(csv_path, separator=separator, dtypes={"poinOfSale":str,"product":str,"date":str, "stock":int})

        print("csv opened in ", time() - start_time, " seconds")

        data.to_pandas().to_sql(table, engine, if_exists='replace', index=False, chunksize=1000, dtype={
            'pointOfSale':String(255),
            'product': String(255),
            'date':DATE,
            'stock':INT 
        })

        total_time = time() - start_time
        print ("finished in ", total_time, " seconds ")
        
    except Exception as e:
        print("An error occurred:", e)
        raise e
        
    finally:
        engine.dispose()
        
csv_postgres_inserter(table="stocks", csv_path="stock.csv", separator=";")