import streamlit as st
from components.dashboard import show_dashboard
from components.data_ingestion import ingest_data
from components.risk_analysis import analyze_risks
from components.mitigation_recommendation import show_recommendations

st.set_page_config(page_title="Supply Chain Guardian", layout="wide")

# st.title("🛡️ Supply Chain Guardian")
st.sidebar.image("assests/DXC.png")
st.sidebar.title("🛡️ Supply Chain Guardian")
st.sidebar.header("Navigation")
view = st.sidebar.radio("Go to", ["Dashboard", "Ingest Data", "Analyze Risks", "Mitigation Recommendations"])

if view == "Dashboard":
    show_dashboard()
elif view == "Ingest Data":
    ingest_data()
elif view == "Analyze Risks":
    analyze_risks()
elif view == "Mitigation Recommendations":
    show_recommendations()
