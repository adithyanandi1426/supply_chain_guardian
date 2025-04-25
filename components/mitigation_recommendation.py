import streamlit as st

def show_recommendations():
    st.subheader("🛠️ Mitigation Recommendations")

    st.success("🚢 **Alternative Shipping Route Identified:** Reroute through Singapore port to avoid congestion in Shanghai.")
    st.info("🏭 **Source Change Suggestion:** Temporarily shift sourcing of microchips to Taiwan-based supplier.")
    st.warning("⚠️ **Inventory Alert:** Critical stock below threshold for product X at warehouse Y.")
