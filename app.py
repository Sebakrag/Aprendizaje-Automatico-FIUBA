import streamlit as st
import pandas as pd
import joblib

# Título y descripción
st.set_page_config(page_title="App AutoML", layout="centered")
st.title("Predicción con modelo AutoML")
st.write("Subí un archivo CSV con datos para predecir con tu modelo.")

# Cargar el modelo desde archivo
@st.cache_resource
def cargar_modelo():
    try:
        modelo = joblib.load("modelos/modelo_cancelacion.pkl")
        return modelo
    except Exception as e:
        st.error(f"No se pudo cargar el modelo: {e}")
        return None

modelo = cargar_modelo()

# Cargar CSV
archivo = st.file_uploader("Elegí un archivo CSV", type=["csv"])

if archivo is not None:
    try:
        datos = pd.read_csv(archivo)
        st.write("📄 Datos cargados:")
        st.dataframe(datos)

        if modelo:
            predicciones = modelo.predict(datos)
            st.write("🔮 Predicciones:")
            st.dataframe(pd.DataFrame(predicciones, columns=["Predicción"]))
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
