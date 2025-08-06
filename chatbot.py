Entendo perfeitamente! Vou **reescrever seu código completo** com todas as atualizações visuais que discutimos, **mantendo 100% da funcionalidade original** e apenas melhorando o design. Aqui está o código atualizado:

```python
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
# CONFIGURAÇÃO INICIAL DO STREAMLIT
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
# NOVO CSS - DESIGN ATUALIZADO
# ======================
hide_streamlit_style = """
<style>
    /* Cores profissionais */
    :root {
        --color-primary: #1a1a1a;
        --color-secondary: #9e0b0f;
        --color-accent: #ff4d8d;
        --color-text: #e0e0e0;
        --color-bg: #0f0f0f;
    }

    /* Layout geral */
    .stApp {
        background: var(--color-bg) !important;
        color: var(--color-text) !important;
    }

    /* Cabeçalho */
    header { 
        background: linear-gradient(90deg, var(--color-primary), var(--color-secondary)) !important;
        color: white !important;
        padding: 15px 0 !important;
    }

    /* Botões */
    div.stButton > button:first-child {
        background: var(--color-accent) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        transition: all 0.3s !important;
        box-shadow: 0 4px 8px rgba(255, 20, 147, 0.3) !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(255, 20, 147, 0.4) !important;
    }

    /* Chat */
    [data-testid="stChatMessageContent"] {
        border-radius: 18px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }
    .stChatMessage[data-testid="user"] [data-testid="stChatMessageContent"] {
        background: rgba(255, 77, 141, 0.15) !important;
        border: 1px solid var(--color-accent) !important;
    }
    .stChatMessage[data-testid="assistant"] [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, var(--color-secondary), var(--color-primary)) !important;
        color: white !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--color-primary), #2a0a0e) !important;
        border-right: 1px solid var(--color-accent) !important;
    }

    /* Prévia de conteúdo */
    .locked-content {
        filter: blur(5px);
        position: relative;
        transition: all 0.3s;
    }
    .locked-content:hover {
        filter: blur(3px);
    }
    .locked-content:after {
        content: "🔒 CONTEÚDO VIP";
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: var(--color-accent);
        font-weight: bold;
        font-size: 1.2em;
        text-shadow: 0 0 5px black;
    }

    /* Efeitos de hover */
    .hover-effect {
        transition: all 0.3s;
    }
