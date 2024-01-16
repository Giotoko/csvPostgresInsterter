
# csvPostgresInsterter

Python script that reads a .csv file and inserts its contents into a PostgreSQL database


## Deployment

To deploy this project run

```bash
  python -m pip install python_dotenv
  python -m pip install sqlalchemy
  python -m pip install polars
  python -m pip install pandas
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`hostname`

`username`

`password`

`database`
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




## Usage/Examples

```python
from csv_postgres_inserter import csv_postgres_inserter

csv_postgres_inserter(table="stocks", csv_path="stock.csv", separator=";")

```


## Authors

- [@Giotoko](https://github.com/Giotoko)

