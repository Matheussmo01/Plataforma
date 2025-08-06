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
# CONSTANTES
# ======================
class Config:
    API_KEY = "AIzaSyDcAPgbK0xSNIGmdq5ySof7XSODfYEZ2-M"
    IMG_PROFILE = "https://i.ibb.co/ks5CNrDn/IMG-9256.jpg"
    IMG_HOME_PREVIEWS = [
        "https://i.ibb.co/k2MJg4XC/Save-ClipApp-412457343-378531441368078-7870326395110089440-n.jpg",
        "https://i.ibb.co/MxqKBk1X/Save-ClipApp-481825770-18486618637042608-2702272791254832108-n.jpg",
        "https://i.ibb.co/F4CkkYTL/Save-ClipApp-461241348-1219420546053727-2357827070610318448-n.jpg"
    ]

# ======================
# CSS ESSENCIAL (CORRIGIDO)
# ======================
st.markdown("""
<style>
    /* Reset básico */
    .stApp {
        background: #0f0f0f;
        color: #e0e0e0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #1e0033 !important;
    }
    
    /* Chat */
    [data-testid="stChatMessage"] {
        padding: 12px;
    }
    
    /* Esconder elementos padrão */
    header, footer, .stDeployButton {
        display: none !important;
    }
    
    /* Botões */
    .stButton>button {
        background: #ff4d8d !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# INICIALIZAÇÃO DO ESTADO (CRÍTICO)
# ======================
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'initialized' not in st.session_state:
    st.session_state.initialized = True

# ======================
# PÁGINA HOME (SIMPLIFICADA PARA TESTE)
# ======================
def show_home():
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem;">
        <img src="{Config.IMG_PROFILE}" width="150" style="border-radius: 50%; border: 3px solid #ff4d8d;">
        <h1 style="color: #ff4d8d;">Paloma Premium</h1>
        <p>Bem-vindo ao meu conteúdo exclusivo</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for col, img in zip(cols, Config.IMG_HOME_PREVIEWS):
        with col:
            st.image(img, use_column_width=True)
    
    if st.button("ENTRAR", use_container_width=True):
        st.session_state.page = "chat"

# ======================
# PÁGINA CHAT (BÁSICA)
# ======================
def show_chat():
    st.title("Chat Privado")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    if prompt := st.chat_input("Digite sua mensagem"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Resposta simulada
        response = f"Olá! Isso é uma resposta simulada para: {prompt}"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# ======================
# ROTEAMENTO PRINCIPAL
# ======================
def main():
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "chat":
        show_chat()

if __name__ == "__main__":
    main()
