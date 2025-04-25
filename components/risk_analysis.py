import streamlit as st
from utils.azure_text_analytics import analyze_text
from utils.azure_openai import extract_risks_gpt

def analyze_risks():
    st.subheader("🧠 Risk Analysis from Ingested Data")

    user_input = st.text_area("Paste a sample news or tweet content here:", height=200)
    
    if st.button("Analyze"):
        with st.spinner("Extracting risks..."):
            text_analytics = analyze_text(user_input)
            gpt_insights = extract_risks_gpt(user_input)

        st.markdown("### Key Phrases & Sentiment (Azure Text Analytics)")
        st.json(text_analytics)

        st.markdown("### GPT-4 Extracted Risk Summary")
        st.write(gpt_insights)
