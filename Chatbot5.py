#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:25:07 2025

@author: juan
"""

# chatbot_chinchin_streamlit.py

import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Chinchín - Sumiller Digital 🍷",
    page_icon="🍷",
    layout="centered"
)

# Estado de la sesión para mantener la conversación
if "history" not in st.session_state:
    st.session_state.history = ["🤖: ¡Hola! Bienvenido a Chinchín, tu sumiller digital 🍷"]
if "step" not in st.session_state:
    st.session_state.step = "inicio"

st.title("Chinchín - Sumiller Digital 🍷")
st.write("Tu asistente experto en maridaje de vinos. Elige una opción:")

# Opciones iniciales
if st.session_state.step == "inicio":
    col1, col2 = st.columns(2)
    if col1.button("🍽️ Recomendación de vino según comida"):
        st.session_state.step = "recomendar"
    if col2.button("📦 Gestionar mi bodega"):
        st.session_state.step = "bodega"
    col3, col4 = st.columns(2)
    if col3.button("🎁 Suscripción mensual"):
        st.session_state.step = "suscripcion"
    if col4.button("🛒 Comparar precios en supermercados"):
        st.session_state.step = "precios"
    if st.button("🍇 Experiencias y catas"):
        st.session_state.step = "experiencias"

# Recomendación de vinos según comida
if st.session_state.step == "recomendar":
    comida = st.selectbox("¿Qué plato vas a comer?", ["Pescado", "Carne", "Pasta", "Postre", "Otro"])
    if st.button("Obtener recomendación"):
        if comida == "Pescado":
            respuesta = "👉 Te recomiendo un Albariño Rías Baixas o un Verdejo para realzar sabores marinos 🐟."
        elif comida == "Carne":
            respuesta = "👉 Un Rioja o un Ribera del Duero son perfectos para carnes rojas 🥩."
        elif comida == "Pasta":
            respuesta = "👉 Un Chianti o Tempranillo complementan genial con pastas 🍝."
        elif comida == "Postre":
            respuesta = "👉 Un Moscatel o un vino de Oporto es ideal para acompañar postres 🍰."
        else:
            respuesta = "🍷 Aún no tengo recomendaciones para ese plato, ¡pero pronto ampliaré la carta!"
        st.session_state.history.append(f"🤖: {respuesta}")
        st.session_state.step = "inicio"

# Gestión de la bodega personal
if st.session_state.step == "bodega":
    st.write("💾 Aquí podrás registrar los vinos que tienes en tu bodega.")
    vino = st.text_input("Introduce el nombre de tu vino:")
    if st.button("Guardar en mi bodega"):
        st.session_state.history.append(f"🤖: Vino '{vino}' guardado en tu bodega personal. 🍷✅")
        st.session_state.step = "inicio"

# Suscripción mensual
if st.session_state.step == "suscripcion":
    st.write("🎁 ¡Con nuestra suscripción recibirás 3 vinos cada mes adaptados a tus gustos y presupuesto!")
    email = st.text_input("Introduce tu email para más info:")
    if st.button("Solicitar información"):
        st.session_state.history.append(f"🤖: Te hemos enviado la información a {email}. ¡Bienvenido a la experiencia Chinchín! 🎉🍷")
        st.session_state.step = "inicio"

# Comparar precios en supermercados
if st.session_state.step == "precios":
    st.write("🛒 Próximamente podrás comparar precios de vinos en supermercados desde aquí.")
    st.session_state.history.append("🤖: ¡Función en desarrollo! 🏗️ Muy pronto podrás comparar precios en tiempo real.")
    st.session_state.step = "inicio"

# Experiencias y catas
if st.session_state.step == "experiencias":
    st.write("🍇 Organizamos catas, visitas a bodegas y eventos exclusivos.")
    if st.button("Quiero apuntarme"):
        st.session_state.history.append("🤖: ¡Te hemos reservado una plaza para la próxima cata! 🥂 Te contactaremos por email.")
        st.session_state.step = "inicio"

# Mostrar historial de conversación
st.write("---")
st.subheader("💬 Historial")
for mensaje in st.session_state.history:
    st.write(mensaje)

# Botón para reiniciar la conversación
if st.button("🔄 Reiniciar conversación"):
    st.session_state.history = ["🤖: ¡Hola! Bienvenido a Chinchín, tu sumiller digital 🍷"]
    st.session_state.step = "inicio"
