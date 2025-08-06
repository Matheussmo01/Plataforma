# ======================
# IMPORTAÇÕES
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
# CONFIGURAÇÃO INICIAL
# ======================
st.set_page_config(
    page_title="Paloma Premium",
    page_icon="💋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# CSS CORRIGIDO E TESTADO
# ======================
st.markdown("""
<style>
    :root {
        --color-primary: #1a1a1a;
        --color-secondary: #9e0b0f;
        --color-accent: #ff4d8d;
        --color-text: #e0e0e0;
        --color-bg: #0f0f0f;
    }

    /* Layout corrigido */
    .stApp {
        background: var(--color-bg) !important;
        color: var(--color-text) !important;
        padding: 0 !important;
    }

    /* Sidebar corrigida */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e0033, #3c0066) !important;
        border-right: 1px solid var(--color-accent) !important;
    }

    /* Chat corrigido */
    [data-testid="stChatMessageContent"] {
        border-radius: 18px !important;
    }
    [data-testid="stChatMessage"].user [data-testid="stChatMessageContent"] {
        background: rgba(255, 77, 141, 0.15) !important;
    }
    [data-testid="stChatMessage"].assistant [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #9e0b0f, #1a1a1a) !important;
        color: white !important;
    }

    /* Botões corrigidos */
    .stButton>button {
        border: 1px solid var(--color-accent) !important;
        background: rgba(255, 77, 141, 0.2) !important;
        color: white !important;
        transition: all 0.3s !important;
    }
    .stButton>button:hover {
        background: rgba(255, 77, 141, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    /* Esconder elementos indesejados */
    header, footer, .stDeployButton {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# [...] (RESTANTE DO CÓDIGO ORIGINAL PRESERVADO)

# ======================
# PÁGINA HOME CORRIGIDA
# ======================
class NewPages:
    @staticmethod
    def show_home_page():
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1e0033, #3c0066);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 2rem;
            border: 1px solid #ff4d8d;
        ">
            <img src="{Config.IMG_PROFILE}" width="120" style="border-radius:50%; border:3px solid #ff4d8d;">
            <h1 style="color: #ff4d8d;">PALOMA PREMIUM</h1>
            <p>Conteúdo exclusivo que vai te deixar sem palavras...</p>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)
        for col, img in zip(cols, Config.IMG_HOME_PREVIEWS):
            with col:
                st.markdown(f"""
                <div style="position:relative;">
                    <img src="{img}" style="width:100%; border-radius:10px; filter:blur(3px);">
                    <div style="
                        position:absolute;
                        top:50%;
                        left:50%;
                        transform:translate(-50%,-50%);
                        color:#ff4d8d;
                        font-weight:bold;
                        font-size:1.2rem;
                    ">
                        🔒 CONTEÚDO VIP
                    </div>
                </div>
                """, unsafe_allow_html=True)

        if st.button("👉 ACESSAR CONTEÚDO COMPLETO", use_container_width=True):
            st.session_state.current_page = "offers"
            st.rerun()

# [...] (MANTENHA O RESTO DO CÓDIGO ORIGINAL)

def main():
    # [...] (IMPLEMENTAÇÃO ORIGINAL)
    pass

if __name__ == "__main__":
    main()
