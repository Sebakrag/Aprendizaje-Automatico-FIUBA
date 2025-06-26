import streamlit as st
import pandas as pd
import joblib
import os
import gdown

# Configuración de la página
st.set_page_config(page_title="Predicción de Cancelación", layout="centered")
st.title("🔮 Predicción de Cancelación de Reserva")
st.write("Subí un archivo CSV con datos de reservas y obtené predicciones con tu modelo entrenado.")

# === CONFIGURAR IDS DE GOOGLE DRIVE ===
ID_MODELO = "1LNjNuIuy8vAtsjxIUDDF2X67PCtzkxXs"
ID_COLUMNAS = "1DNg0ft8T6gCxdZMhnEFCIHg9mHED2cwl"
ID_TOP10 = "1BcDnK1mRoKyfEiqt4Y_oklzSdSFMY5gq"

# === RUTAS LOCALES DEL DRIVE ===
MODELO_PATH = "modelo_cancelacion.pkl"
COLUMNAS_PATH = "columnas_entrenamiento.pkl"
TOP10_PATH = "top_10_countries.pkl"

# === Descarga desde Google Drive si no están ===
def descargar_archivo(id_archivo, output_path):
    if not os.path.exists(output_path):
        # Crear carpeta si existe (solo si dirname no es vacío)
        dir_path = os.path.dirname(output_path)
        if dir_path != '':
            os.makedirs(dir_path, exist_ok=True)
        url = f"https://drive.google.com/uc?id={id_archivo}"
        gdown.download(url, output_path, quiet=False)

# === Cargar modelo, columnas y top 10 países ===
@st.cache_resource
def cargar_recursos():
    descargar_archivo(ID_MODELO, MODELO_PATH)
    descargar_archivo(ID_COLUMNAS, COLUMNAS_PATH)
    descargar_archivo(ID_TOP10, TOP10_PATH)

    modelo = joblib.load(MODELO_PATH)
    columnas_entrenamiento = joblib.load(COLUMNAS_PATH)
    top_10_countries = joblib.load(TOP10_PATH)

    return modelo, columnas_entrenamiento, top_10_countries

modelo, columnas_entrenamiento, top_10_countries = cargar_recursos()

# === Subida de CSV ===
archivo = st.file_uploader("📁 Subí un archivo CSV", type=["csv"])

if archivo is not None:
    try:
        datos = pd.read_csv(archivo)
        st.write("📄 Datos cargados:")
        st.dataframe(datos)

        # === Preprocesamiento igual que en notebook ===

        # 1. Llenar NaNs con 0
        datos.fillna(0, inplace=True)

        # 2. Mapear mes de llegada
        month_number_in_season = {
            'January': 0, 'February': 0, 'March': 0,
            'April': 1, 'May': 1, 'June': 1,
            'July': 1, 'August': 1, 'September': 1,
            'October': 1, 'November': 0, 'December': 0
        }
        if 'arrival_date_month' in datos.columns:
            datos['arrival_date_month'] = datos['arrival_date_month'].map(month_number_in_season)

        # 3. Reemplazar países fuera del top 10
        if 'country' in datos.columns:
            datos["country"] = datos["country"].apply(lambda x: x if x in top_10_countries else "otros")

        # 4. Variables categóricas a codificar
        variables_categoricas = [
            "hotel", "arrival_date_month", "meal", "country", "market_segment",
            "distribution_channel", "reserved_room_type", "assigned_room_type",
            "deposit_type", "customer_type"
        ]

        # 5. One-hot encoding
        datos = pd.get_dummies(datos, columns=variables_categoricas, drop_first=True)

        # 6. Alinear con columnas de entrenamiento
        datos = datos.reindex(columns=columnas_entrenamiento, fill_value=0)

        # === Predicciones ===
        predicciones = modelo.predict(datos)
        st.write("🔮 Predicciones:")
        st.dataframe(pd.DataFrame(predicciones, columns=["Predicción"]))

    except Exception as e:
        st.error(f"❌ Error al procesar los datos: {e}")
