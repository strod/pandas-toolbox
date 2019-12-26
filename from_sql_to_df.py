# Data Visualization and Manipulation
import pandas as pd
# SQL Inserting and Reading
import sqlalchemy as sa
import urllib

# Example Params Set
server_name = "SPLADB20"
db_name = "DATA_BI_CMW"
user_name = "DATA_BI_CMW"
password = "Brasil@19"
table_name = "chev_fb_page_insights"

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};" +
                                 "SERVER={0};".format(server_name) +
                                 "DATABASE={0};".format(db_name) +
                                 "UID={0};".format(user_name) +
                                 "PWD={0}".format(password))

engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

# Query to Table
query = """
SELECT
    TOP (100)*
FROM {0}
""".format(table_name)

# Reading Table
df = pd.read_sql(query, engine, parse_dates=True)
print(df.info())
