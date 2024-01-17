
# csvPostgresInsterter

Python script that reads a .csv file and inserts its contents into a PostgreSQL database


## Deployment

To deploy this project run

```bash
  python -m pip install python_dotenv sqlalchemy polars pandas psycopg2 pyarrow

```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`hostname` the database host 

`username` the database username

`password` the dabase password for specified username

`database` the database name
## Parameter Reference

#### table

```python
  table="tablename"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `table`   | `string` | **Required**. the name of the sql table |

#### csv_path

```python
  csv_path="path/to/csv_file.csv"
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `csv_path` | `string` | **Required**. path to the csv file |

#### separator

```python
  separator=","
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `separator` | `string` | **optional**. value separator of csv file |


#### table_types

```python
  table_types={"column1":str, "column2":int...}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `table_types` | `dictionary` | **required**. map specifying the data types
 || | of every column of the postgresql table (sqlalchemy types)|

#### table_types

```python
  csv_types={"column1":str, "column2":int...}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `csv_types` | `dictionary` | **required**. map specifying the data types of every column of the csv |



## Usage/Examples

```python
from csv_postgres_inserter import csv_postgres_inserter

csv_postgres_inserter(table="table", csv_path="file.csv", separator="," table_type={"column1":String(255), "column2":INT}, csv_type={"column1":str, "column2":int})

```


## Features

- works with any csv and any postgresql table
- there's no need to create the table, the script handles that for you


## Authors

- [@Giotoko](https://github.com/Giotoko)

