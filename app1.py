import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA Y ESTILO "Y2K / EMO / DARK BLOG 2000s"
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="x_DarkReader_x :: 2000s Emo Weblog", 
    page_icon="🖤", 
    layout="wide"
)

# Inyectando CSS personalizado para simular un fotolog oscuro/emo de los 2000s
st.markdown("""
    <style>
    /* Fondo general negro/oscuro con tipografía de estilo retro-alternativo */
    .stApp {
        background-color: #0b0b0b;
        color: #c0c0c0;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Estilo para los títulos (tipo MySpace / FlogVip) */
    h1, h2, h3 {
        color: #ff007f !important;
        text-shadow: 2px 2px #33001a;
        font-family: 'Times New Roman', serif;
        letter-spacing: 2px;
    }
    
    /* Cajas de texto o contenedores con bordes punteados estilo 2000 */
    .css-1544g2n, div[data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 2px dashed #ff007f;
    }
    
    /* Estilo de los botones */
    .stButton>button {
        background-color: #ff007f !important;
        color: #ffffff !important;
        border: 2px solid #ffffff;
        border-radius: 0px;
        font-weight: bold;
    }
    
    /* Área de texto de resultados */
    .output-box {
        background-color: #1a001a;
        border: 1px dashed #ff007f;
        padding: 15px;
        color: #ff99cc;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DISTRIBUCIÓN REORGANIZADA (LAYOUT ESTILO BLOG 2000s)
# -----------------------------------------------------------------------------

# Cabecera gótica / 2000s
st.markdown("<h1 style='text-align: center;'>~* x_DarkDecrypter_x *~</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666666;'><i>\"...porque las palabras escritas en la oscuridad nunca se olvidan...\" [Photolog v2.0]</i></p>", unsafe_allow_html=True)
st.markdown("---")

# Creamos columnas para cambiar drásticamente el orden visual tradicional
col_izq, col_der = st.columns([1, 1], gap="large")

with col_izq:
    st.subheader("🦇 1. Captura tu destino")
    st.write("Abre tu webcam y deja que el sistema lea entre líneas lo que ocultas.")
    
    # El componente de la cámara ahora vive en la columna izquierda principal
    img_file_buffer = st.camera_input("Capturar alma (Foto)")

with col_der:
    st.subheader("⛓️ 2. Opciones de Revelado")
    # El filtro se reubicó fuera de la barra lateral para darle protagonismo en panel central
    filtro = st.radio(
        "Elige tu estado de ánimo visual:", 
        ('Inverso Oscuro (Negativo)', 'Sin Alterar (Normal)')
    )
    
    st.markdown("---")
    st.markdown("### 📜 3. Mensaje Criptográfico Detectado:")
    
    # Contenedor de resultados estilizado
    resultado_placeholder = st.empty()

# -----------------------------------------------------------------------------
# LÓGICA DE PROCESAMIENTO OCR
# -----------------------------------------------------------------------------
if img_file_buffer is not None:
    # Leer el buffer de la imagen con OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Aplicar el filtro según la selección del usuario
    if filtro == 'Inverso Oscuro (Negativo)':
        cv2_img = cv2.bitwise_not(cv2_img)
    
    # Convertir a RGB para que Pytesseract lo procese correctamente
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Extraer el texto mediante OCR
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar el resultado dentro del contenedor de estilo gótico
    with col_der:
        if text.strip() != "":
            st.markdown(f'<div class="output-box">{text}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="output-box" style="color: #666;">[No se encontraron rastros de texto en la oscuridad...]</div>', unsafe_allow_html=True)

# Pie de página clásico de los blogs 2000s
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: #444;'>xoxox - Powered by OpenCV, Tesseract & Streamlit 2000s Dark Edition - xoxox</p>", unsafe_allow_html=True)
