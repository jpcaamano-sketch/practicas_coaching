import streamlit as st

# --- 1. CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="Herramientas de Coaching", 
    layout="centered", 
    initial_sidebar_state="expanded"  # Intenta forzar la apertura al inicio
)

# --- 2. PERSONALIZACIÓN BARRA LATERAL ---
with st.sidebar:
    st.title("Prácticas de Coaching")
    st.caption("Desarrollado por Juan Pablo Caamaño Valdés")
    st.divider()

# --- 3. DEFINICIÓN DE TUS HERRAMIENTAS ---
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

# --- 5. ESTILOS (CORREGIDOS PARA QUE APAREZCA EL MENÚ) ---
st.markdown("""
    <style>
    /* 1. Ocultar menú de los 3 puntos y pie de página */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 2. ELIMINAMOS LA ORDEN DE OCULTAR EL HEADER COMPLETO 
       (Esto permite que veas la flecha '>' si el menú se cierra) */
    
    /* 3. BLOQUEAR EL BOTÓN DE CERRAR (La 'X' dentro del menú) */
    [data-testid="stSidebarCollapseButton"] {
        display: none;
    }

    /* 4. Alinear contenido */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* 5. Títulos del menú siempre visibles */
    div[data-testid="stSidebarNav"] span {
        visibility: visible !important;
        font-size: 14px;
        font-weight: 600;
        color: #444; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 6. EJECUTAR ---
pg.run()