import streamlit as st
import pandas as pd 
from VitakodConnector import VitakodConnector

class VitaDashboard:
    def __init__(self, title="Explorador de Dados", favicon= None):
        self.vk = VitakodConnector()
        st.set_page_config(page_title=title, page_icon=favicon, layout="centered", initial_sidebar_state="auto", menu_items=None)
    
    def reports_map(self, limit = None, offset = None):
        data = self.vk.get_reports(limit, offset)
        lats = []
        lons = []
        for element in data:
            lat = element["Lat"]
            lon = element["Lon"]
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