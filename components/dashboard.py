import streamlit as st

def show_dashboard():
    st.markdown("## 📊 Supply Chain Risk Dashboard")

    # Add some spacing and layout
    st.markdown("""
        <style>
            .card {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                text-align: center;
            }
            .card h3 {
                margin: 0;
                font-size: 20px;
                color: #333;
            }
            .card p {
                font-size: 28px;
                font-weight: bold;
                color: #007BFF;
                margin: 10px 0 0;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="card"><h3>Potential Disruptions</h3><p>12</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>Avg. Mitigation Time</h3><p>2.3 hrs</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>Impact Assessment Accuracy</h3><p>92%</p></div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card"><h3>Disruptions Reduced</h3><p>35%</p></div>', unsafe_allow_html=True)
