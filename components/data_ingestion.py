import streamlit as st
import json
from utils.event_hub_simulator import stream_event_data

def ingest_data():
    st.subheader("🌍 Real-Time Data Ingestion Simulation")
    st.write("Simulated feed from Event Hub using sample data.")
    
    data = stream_event_data("data/sample_news.json")
    
    for i, item in enumerate(data[:5]):
        st.markdown(f"**{i+1}. {item['title']}**")
        st.caption(item['publishedAt'])
        st.write(item['content'])
