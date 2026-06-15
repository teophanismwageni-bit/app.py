import streamlit as st
import pandas as pd
from PIL import Image

# 1. Kwanza, weka usanidi wa ukurasa (lazima iwe amri ya kwanza ya Streamlit)
st.set_page_config(
    page_title="MFUMO WA KANISA - Dashboard",
    page_icon="⛪", # Unaweza kutumia ikoni ya kanisa
    layout="wide", # Inafanya muonekano uwe mpana zaidi
    initial_sidebar_state="expanded",
)

# --- 2. WEKA STYLES (HTML NA CSS) HAPA ---
# Hapa ndipo uchawi wa muonekano unatokea. Tunaweka rangi na muundo.
st.markdown("""
<style>
    /* Rangi za msingi za mfumo wetu */
    :root {
        --primary-color: #27ae60; /* Rangi kuu (Green) */
        --accent-color-1: #3498db; /* Rangi ya kwanza ya lafudhi (Blue) */
        --accent-color-2: #f1c40f; /* Rangi ya pili ya lafudhi (Yellow) */
        --text-color: #333;
        --background-color: #f4f7f6;
    }

    /* Badilisha muonekano wa background nzima */
    .stApp {
        background-color: var(--background-color);
    }

    /* Styles za Sehemu ya Bango (Hero Section) */
    .hero-container {
        background-color: #333;
        color: white;
        padding: 50px;
        border-radius: 15px;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    .hero-content {
        max-width: 60%;
    }

    .hero-title {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 1.5rem;
        opacity: 0.8;
    }

    .hero-image-container img {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
    }

    /* Styles za Sehemu ya Dashboard Cards (Kadi za Dashboard) */
    .dashboard-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        padding-top: 20px;
    }

    .dashboard-card {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid;
        transition: transform 0.2s;
    }

    .dashboard-card:hover {
        transform: translateY(-5px);
    }

    .card-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: var(--text-color);
        margin-bottom: 15px;
    }

    .card-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: var(--primary-color);
        margin-bottom: 10px;
    }

    .card-icon {
        font-size: 1.5rem;
        margin-right: 10px;
        vertical-align: middle;
    }

    /* Styles za Rangi kwa Kila Kadi */
    .card-waumini { border-left-color: var(--primary-color); }
    .card-mafundisho { border-left-color: var(--accent-color-1); }
    .card-matukio { border-left-color: var(--accent-color-2); }
    .card-miradi { border-left-color: #e74c3c; } /* Rangi ya nyongeza (Red) */

    /* Styles za Chati na Data */
    .chart-container {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)

# --- 3. SEHEMU YA BANGO (HERO SECTION) ---
# Sehemu ya kwanza kabisa yenye logo na jina la kanisa
st.markdown("""
<div class="hero-container">
    <div class="hero-content">
        <h1 class="hero-title">Karibu Kwenye Mfumo wa Kanisa</h1>
        <p class="hero-subtitle">Kuunganisha, Kufundisha, na Kujenga Jumuiya ya Kiimani</p>
    </div>
    <div class="hero-image-container">
        <!-- Weka logo ya kanisa hapa -->
        <img src="https://images.streamlit.io/media-assets/streamlit-logo-secondary-colormark-darktext.png" alt="Logo">
        <!-- Kumbuka kubadilisha hii na picha yako: <img src="images/logo.png" alt="Logo"> -->
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4. DATA ZA MFANO (UNAWEZA KUZIBADILISHA) ---
# Hapa unaweza kusoma data zako kutoka kwenye CSV au database
data_waumini = {
    'Kitengo': ['Wazee', 'Vijana', 'Watoto', 'Wageni'],
    'Idadi': [150, 220, 180, 50]
}
df_waumini = pd.DataFrame(data_waumini)

# --- 5. SEHEMU YA DASHBOARD CARDS (KADI ZA DASHBOARD) ---
# Hapa tunaonyesha takwimu muhimu kwa muonekano wa kijanja
st.markdown("""
<div class="dashboard-container">
    <div class="dashboard-card card-waumini">
        <div class="card-title">👥 <span class="card-icon"></span>Waumini Ambao Wapo Ambao Ni Wazee</div>
        <div class="card-value">600</div>
        <p>Idadi ya waumini waliosajiliwa hadi sasa</p>
    </div>
    <div class="dashboard-card card-mafundisho">
        <div class="card-title">📖 <span class="card-icon"></span>Mafundisho na Makala</div>
        <div class="card-value">12</div>
        <p>Makala na masomo yanayopatikana hewani</p>
    </div>
    <div class="dashboard-card card-matukio">
        <div class="card-title">📅 <span class="card-icon"></span>Matukio Yanayokuja</div>
        <div class="card-value">3</div>
        <p>Matukio muhimu ya kanisa katika mwezi huu</p>
    </div>
     <div class="dashboard-card card-miradi">
        <div class="card-title">🏗️ <span class="card-icon"></span>Miradi ya Maendeleo</div>
        <div class="card-value">2</div>
        <p>Miradi ya kanisa inayotekelezwa sasa hivi</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. SEHEMU YA CHATI NA DATA NYINGINE ---
# Hapa unaweza kuonyesha chati au data nyingine
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.subheader("Idadi ya Waumini Kwa Kitengo")
st.bar_chart(df_waumini.set_index('Kitengo'))
st.markdown("</div>", unsafe_allow_html=True)

# --- 7. SIDEBAR ---
# Unaweza kuweka menu ya upande kwa ajili ya urahisi wa urambazaji
with st.sidebar:
    st.header("MENU KUU")
    st.button("Dashboard", key="dash_btn")
    st.button("Orodha ya Waumini", key="waumini_btn")
    st.button("Ratiba ya Ibada", key="ibada_btn")
    st.button("Ripoti za Fedha", key="fedha_btn")
    st.markdown("---")
    st.markdown("Citations: [1]")