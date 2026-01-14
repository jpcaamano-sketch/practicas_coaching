import streamlit as st

# --- 1. CONFIGURACIÓN DEL JEFE (Va primero que todo) ---
st.set_page_config(page_title="Herramientas de Coaching", layout="centered")

# --- 2. DEFINICIÓN DE TUS HERRAMIENTAS ---
# Rutas a tus archivos en la carpeta apps

# Comunicación
p_correos = st.Page("apps/2.1_Correos.py", title="Correos Diplomáticos", icon="🗣️")
p_pedidos = st.Page("apps/2.2_Pedidos.py", title="Pedidos Impecables", icon="🛡️")

# Liderazgo
p_delegacion = st.Page("apps/1.1_Delegacion.py", title="Delegación Situacional", icon="🤝")

# Productividad
p_reuniones = st.Page("apps/3.1_Reuniones.py", title="Planificación Reuniones", icon="⏳")
p_priorizador = st.Page("apps/3.2_Priorizador.py", title="Priorizados de Tareas", icon="⚡")

# Resolución de Conflictos
p_negociador = st.Page("apps/4.1_Negociador.py", title="Negociador Harvard", icon="☮️")

# --- 3. CREACIÓN DEL MENÚ DE NAVEGACIÓN ---
# Al agruparlas así, los títulos ("📢 Comunicación", etc.) deben aparecer fijos.
pg = st.navigation({
    "COMUNICACIÓN": [p_pedidos, p_correos],
    "LIDERAZGO": [p_delegacion],
    "PRODUCTIVIDAD": [p_priorizador, p_reuniones],
    "NEGOCIACIÓN": [p_negociador]
})

# --- 4. ESTILOS LIMPIOS (CSS Global) ---
st.markdown("""
    <style>
    /* 1. Ocultar elementos innecesarios */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {visibility: hidden;}

    /* 2. Alinear todas las páginas arriba (evita saltos) */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* 3. Forzar que los títulos de categorías sean visibles siempre */
    div[data-testid="stSidebarNav"] span {
        visibility: visible !important;
        font-size: 14px;
        font-weight: 600;
        color: #444; /* Color gris oscuro profesional */
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. EJECUTAR LA APP SELECCIONADA ---
pg.run()