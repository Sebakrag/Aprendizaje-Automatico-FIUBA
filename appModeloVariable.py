import streamlit as st
import pandas as pd
import joblib

# Configuración básica
st.set_page_config(page_title="App AutoML", layout="centered")
st.title("Predicción con modelo AutoML")
st.write("Subí tu modelo entrenado (.pkl) y los datos a predecir (.csv).")

# Subida del modelo
modelo_file = st.file_uploader("📦 Subí tu modelo AutoML (.pkl)", type=["pkl"])

# Subida del archivo CSV
csv_file = st.file_uploader("📄 Subí el archivo CSV con datos a predecir", type=["csv"])

modelo = None
if modelo_file is not None:
    try:
        modelo = joblib.load(modelo_file)
        st.success("✅ Modelo cargado correctamente.")
    except Exception as e:
        st.error(f"❌ Error al cargar el modelo: {e}")

if csv_file is not None and modelo:
    try:
        datos = pd.read_csv(csv_file)
        st.write("📋 Datos cargados:")
        st.dataframe(datos)

        predicciones = modelo.predict(datos)
        st.write("🔮 Predicciones:")
        st.dataframe(pd.DataFrame(predicciones, columns=["Predicción"]))
    except Exception as e:
        st.error(f"❌ Error al procesar los datos: {e}")
