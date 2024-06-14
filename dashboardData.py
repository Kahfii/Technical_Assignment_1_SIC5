import streamlit as st
import requests
import pandas as pd
from datetime import datetime

FLASK_API_URL = "http://ip_address_server:5000/data"

st.title("Dashboard Data")

def fetch_data():
    response = requests.get(FLASK_API_URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Gagal mengambil data dari Flask API")
        return None

if st.button('Fetch Data'):
    data = fetch_data()

    if data:
        df = pd.DataFrame(data)
        
        df['Waktu'] = pd.to_datetime(df['Waktu'])
        
        df['Waktu'] = df['Waktu'].dt.strftime('%Y-%m-%d %H:%M:%S')

        st.write("### Tabel Data")
        st.dataframe(df)

        st.write("### Grafik Garis Data")
        st.line_chart(df.set_index('Waktu'))
