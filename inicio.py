import streamlit as st

# --- 1. CONFIGURACIÓN INICIAL (Modificada) ---
# initial_sidebar_state="expanded" fuerza a que arranque abierta.
st.set_page_config(
    page_title="Herramientas de Coaching", 
    layout="centered", 
    initial_sidebar_state="expanded"
)

# --- 2. PERSONALIZACIÓN BARRA LATERAL (Nuevo) ---
# Esto coloca el Título y tu Nombre en la parte superior de la barra
with st.sidebar:
    st.title("Prácticas de Coaching")
    st.caption("Desarrollado por Juan Pablo Caamaño Valdés")
    st.divider() # Una línea separadora elegante

# --- 3. DEFINICIÓN DE TUS HERRAMIENTAS ---
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

# --- 4. CREACIÓN DEL MENÚ DE NAVEGACIÓN ---
pg = st.navigation({
    "COMUNICACIÓN": [p_pedidos, p_correos],
    "LIDERAZGO": [p_delegacion],
    "PRODUCTIVIDAD": [p_priorizador, p_reuniones],
    "NEGOCIACIÓN": [p_negociador]
})

# --- 5. ESTILOS LIMPIOS (CSS Global + Bloqueo de Barra) ---
st.markdown("""
    <style>
    /* 1. Ocultar elementos innecesarios del sistema */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {visibility: hidden;}

    /* 2. BLOQUEAR LA BARRA LATERAL (Truco CSS) */
    /* Esto oculta la flecha "X" para cerrar la barra, haciéndola fija */
    [data-testid="stSidebarCollapseButton"] {
        display: none;
    }

    /* 3. Alinear todas las páginas arriba */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* 4. Estilo de los títulos de categorías en el menú */
    div[data-testid="stSidebarNav"] span {
        visibility: visible !important;
        font-size: 14px;
        font-weight: 600;
        color: #444; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 6. EJECUTAR LA APP SELECCIONADA ---
pg.run()