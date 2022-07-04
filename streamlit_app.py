import snowflake.connector
import snowflake
import streamlit

conn = snowflake.connector.connect(**streamlit.secrets["snowflake"])
cur = conn.cursor()
cur.execute("SELECT CURRENT_USER(),CURRENT_ACCOUNT(),CURRENT_REGION()")
data_row = cur.fetchone()
streamlit.text(data_row)
