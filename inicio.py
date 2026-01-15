import streamlit as st

# --- 1. CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="Herramientas de Coaching", 
    layout="centered", 
    initial_sidebar_state="expanded" 
)

# --- 2. PERSONALIZACIÓN BARRA LATERAL ---
with st.sidebar:
    st.title("Prácticas de Coaching")
    st.caption("#Desarrollado por Juan Pablo Caamaño Valdés")
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

# --- 5. ESTILOS (El Camuflaje Perfecto) ---
st.markdown("""
    <style>
    /* 1. Ocultar Menú hamburguesa y Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 2. OCULTAR LA BARRA DE HERRAMIENTAS SUPERIOR (Donde sale 'Deploy' y los 3 puntos) */
    [data-testid="stToolbar"] {
        visibility: hidden;
        display: none;
    }

    /* 3. OCULTAR LA DECORACIÓN DE COLORES (La línea arcoíris arriba del todo) */
    [data-testid="stDecoration"] {
        visibility: hidden;
        display: none;
    }

    /* 4. HACER EL ENCABEZADO TRANSPARENTE 
       (Esto permite que no se vea la barra blanca, pero mantiene la estructura) */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }

    /* 5. BLOQUEAR EL BOTÓN DE CERRAR BARRA LATERAL 
       (Para que el usuario no pueda cerrarla accidentalmente) */
    [data-testid="stSidebarCollapseButton"] {
        display: none;
    }

    /* 6. SUBIR EL CONTENIDO 
       (Como ocultamos la barra, subimos el texto para aprovechar el espacio) */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    /* 7. ESTILOS DEL MENÚ LATERAL */
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