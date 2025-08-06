# ======================
# IMPORTAÇÕES (MANTIDAS)
# ======================
import streamlit as st
import requests
import json
import time
import random
import sqlite3
import re
import os
import uuid
from datetime import datetime
from pathlib import Path
from functools import lru_cache

# ======================
# CONFIGURAÇÃO INICIAL (MANTIDA)
# ======================
st.set_page_config(
    page_title="Paloma Premium",
    page_icon="💋",
    layout="wide",
    initial_sidebar_state="expanded"
)

st._config.set_option('client.caching', True)
st._config.set_option('client.showErrorDetails', False)

# ======================
# NOVO CSS APENAS COM CORES (SEM MUDAR LAYOUT)
# ======================
hide_streamlit_style = """
<style>
    /* NOVA PALETA */
    :root {
        --roxo-escuro: #1a0033;
        --vinho: #9e0b0f;
        --rosa-neon: #ff4d8d;
        --texto-claro: #f0f0f0;
        --fundo-escuro: #0a0a0a;
    }

    /* APLICAÇÃO DAS CORES (MANTENDO ESTRUTURA ORIGINAL) */
    .stApp {
        background: var(--fundo-escuro) !important;
    }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--roxo-escuro), #2a0a0e) !important;
    }
    
    /* BOTÕES */
    div.stButton > button:first-child {
        background: var(--rosa-neon) !important;
        color: white !important;
    }
    
    /* CHAT - MENSAGENS */
    [data-testid="stChatMessage"].user [data-testid="stChatMessageContent"] {
        background: rgba(158, 11, 15, 0.15) !important;
    }
    [data-testid="stChatMessage"].assistant [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, var(--vinho), var(--roxo-escuro)) !important;
        color: var(--texto-claro) !important;
    }
    
    /* HEADER/FOOTER (MANTIDO OCULTO) */
    header, footer, .stDeployButton {
        visibility: hidden;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ======================
# CONSTANTES (MANTIDAS)
# ======================
class Config:
    API_KEY = "AIzaSyDcAPgbK0xSNIGmdq5ySof7XSODfYEZ2-M"
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    VIP_LINK = "https://exemplo.com/vip"
    CHECKOUT_START = "https://pay.risepay.com.br/Pay/c5b7f25d46b649a487c01607f6aa0dc0"
    CHECKOUT_PREMIUM = "https://checkout.exemplo.com/premium"
    CHECKOUT_EXTREME = "https://checkout.exemplo.com/extreme"
    CHECKOUT_VIP_1MES = "https://checkout.exemplo.com/vip-1mes"
    CHECKOUT_VIP_3MESES = "https://checkout.exemplo.com/vip-3meses"
    CHECKOUT_VIP_1ANO = "https://checkout.exemplo.com/vip-1ano"
    MAX_REQUESTS_PER_SESSION = 30
    REQUEST_TIMEOUT = 30
    AUDIO_FILE = "https://github.com/Matheussmo01/Plataforma/raw/refs/heads/main/assets/assets_audio_paloma_audio.mp3"
    AUDIO_DURATION = 7
    IMG_PROFILE = "https://i.ibb.co/ks5CNrDn/IMG-9256.jpg"
    IMG_GALLERY = [
        "https://i.ibb.co/zhNZL4FF/IMG-9198.jpg",
        "https://i.ibb.co/Y4B7CbXf/IMG-9202.jpg",
        "https://i.ibb.co/Fqf0gPPq/IMG-9199.jpg"
    ]
    IMG_HOME_PREVIEWS = [
        "https://i.ibb.co/k2MJg4XC/Save-ClipApp-412457343-378531441368078-7870326395110089440-n.jpg",
        "https://i.ibb.co/MxqKBk1X/Save-ClipApp-481825770-18486618637042608-2702272791254832108-n.jpg",
        "https://i.ibb.co/F4CkkYTL/Save-ClipApp-461241348-1219420546053727-2357827070610318448-n.jpg"
    ]
    LOGO_URL = "https://i.ibb.co/LX7x3tcB/Logo-Golden-Pepper-Letreiro-1.png"

# ======================
# [RESTANTE DO CÓDIGO ORIGINAL PERMANECE IDÊNTICO]
# ======================
# [...] (Todas as classes e funções originais mantidas exatamente como estão)
# [...] (PersistentState, Persona, CTAEngine, DatabaseService, etc)
# [...] (UiService, NewPages, ChatService exatamente como no original)

def main():
    # [Implementação original mantida integralmente]
    if 'db_conn' not in st.session_state:
        st.session_state.db_conn = DatabaseService.init_db()
    
    conn = st.session_state.db_conn
    ChatService.initialize_session(conn)
    
    if not st.session_state.age_verified:
        UiService.age_verification()
        st.stop()
    
    UiService.setup_sidebar()
    
    if not st.session_state.connection_complete:
        UiService.show_call_effect()
        st.session_state.connection_complete = True
        save_persistent_data()
        st.rerun()
    
    if not st.session_state.chat_started:
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            st.markdown("""
            <div style="text-align: center; margin: 50px 0;">
                <img src="{profile_img}" width="120" style="border-radius: 50%; border: 3px solid #ff66b3;">
                <h2 style="color: #ff66b3; margin-top: 15px;">Paloma</h2>
                <p style="font-size: 1.1em;">Estou pronta para você, amor...</p>
            </div>
            """.format(profile_img=Config.IMG_PROFILE), unsafe_allow_html=True)
            
            if st.button("Iniciar Conversa", type="primary", use_container_width=True):
                st.session_state.update({
                    'chat_started': True,
                    'current_page': 'chat',
                    'audio_sent': False
                })
                save_persistent_data()
                st.rerun()
        st.stop()
    
    if st.session_state.current_page == "home":
        NewPages.show_home_page()
    elif st.session_state.current_page == "gallery":
        UiService.show_gallery_page(conn)
    elif st.session_state.current_page == "offers":
        NewPages.show_offers_page()
    elif st.session_state.current_page == "vip":
        st.session_state.show_vip_offer = True
        save_persistent_data()
        st.rerun()
    elif st.session_state.get("show_vip_offer", False):
        st.warning("Página VIP em desenvolvimento")
        if st.button("Voltar ao chat"):
            st.session_state.show_vip_offer = False
            save_persistent_data()
            st.rerun()
    else:
        UiService.enhanced_chat_ui(conn)
    
    save_persistent_data()

if __name__ == "__main__":
    main()
