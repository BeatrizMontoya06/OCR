import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA Y ESTILO CYBER-RETRO 2000s
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CyberScan 2000 💾", 
    page_icon="🤖", 
    layout="wide"
)

# Estilo visual de los 2000s tecnológico (verde fósforo / hacker / arcade)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #00ff66;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3 {
        color: #00ffff !important;
        text-shadow: 0px 0px 8px rgba(0,255,255,0.6);
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #00ffff !important;
        color: #000000 !important;
        border: 2px solid #00ff66;
        font-weight: bold;
    }
    .terminal-box {
        background-color: #161b22;
        border: 2px solid #00ff66;
        padding: 15px;
        color: #00ff66;
        font-family: 'Courier New', Courier, monospace;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LAYOUT REORGANIZADO: DOS COLUMNAS (CONTROLES A LA IZQUIERDA, CÁMARA A LA DERECHA)
# -----------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center;'>⚡ CYBER-SCANNER OCR 2000 ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>[ Sistema de Reconocimiento Óptico v1.0 - Conectado al mainframe ]</p>", unsafe_allow_html=True)
st.markdown("---")

col_controles, col_camara = st.columns([1, 1], gap="large")

with col_controles:
    st.subheader("🎛️ 1. Panel de Control")
    filtro = st.radio(
        "Selecciona el modo de procesamiento:", 
        ('Modo Normal (RGB)', 'Invertir Colores (Negativo Matrix)')
    )
    
    st.markdown("---")
    st.subheader("💾 3. Texto Extraído del Sistema")
    # Contenedor donde aparecerá el resultado del OCR
    resultado_placeholder = st.empty()

with col_camara:
    st.subheader("📷 2. Captura de Imagen")
    st.write("Alinea tu texto frente a la webcam y presiona capturar:")
    img_file_buffer = st.camera_input("Tomar Foto")

# -----------------------------------------------------------------------------
# LÓGICA DE PROCESAMIENTO OCR
# -----------------------------------------------------------------------------
if img_file_buffer is not None:
    # Leer el buffer de la imagen con OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Aplicar el filtro seleccionado
    if filtro == 'Invertir Colores (Negativo Matrix)':
        cv2_img = cv2.bitwise_not(cv2_img)
    
    # Convertir a RGB para Tesseract
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Extraer texto
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar el resultado dentro del panel de la izquierda
    with col_controles:
        if text.strip() != "":
            st.markdown(f'<div class="terminal-box">{text}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="terminal-box" style="color: #ff5555;">[ERROR: No se detectó texto legible]</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #484f58;'>CyberScan 2000 :: Powered by Python, Tesseract & Streamlit</p>", unsafe_allow_html=True)
