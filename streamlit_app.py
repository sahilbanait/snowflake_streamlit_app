import pandas
import requests
import streamlit
import snowflake.connector

conn = snowflake.connector.connect(**streamlit.secrets["snowflake"])
cur = conn.cursor()
cur.execute("SELECT CURRENT_ACCOUNT()")
