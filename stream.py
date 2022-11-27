import streamlit as st
import pandas as pd 
import numpy as np
import psycopg2

class DataCollector:
    def __init__(self):
        self.endpoint = "vitacaptis.ccqjibk2mgb8.us-east-1.rds.amazonaws.com"
        self.port = "5432"
        self.dbname = "postgres"
        self.user = "vitakod"
        self.password = "vita=kod22"
        self.conn = self.get_connection()
    def get_connection(self):
        try:
            conn = psycopg2.connect(host=self.endpoint, port=self.port, database=self.dbname, user=self.user, password=self.password)
            return conn
        except Exception as e:
            print("Database connection failed due to {}".format(e))

dc = DataCollector()
cur = dc.conn.cursor()
cur.execute("""SELECT * from reports""")
query_results = cur.fetchall()
dc.conn.close()
lats = []
lons = []
for element in query_results:
    lat = element[8]
    lon = element[9]
    lats.append(float(lat))
    lons.append(float(lon))

details = {
    "lat": lats,
    "lon": lons
}

df = pd.DataFrame(details)

st.title("Mapa para demonstração dos dados geográficos:")
st.map(df)
st.subheader("Os dados são extraídos diretamente do nosso banco de dados RDS", anchor=None)