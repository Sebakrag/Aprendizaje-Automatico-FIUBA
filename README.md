# Aprendizaje-Automatico-FIUBA
Repositorio destinado para la materia Aprendizaje Automatico de la Facultad de Ingenieria de Buenos Aires - FIUBA

## Integrantes

| Integrante | Padrón  | Mail |
|------------|---------|--------|
| Maria Delfina Cano Ros Langrehr | 109338 | mcano@fi.uba.ar |
| Sebastian Kraglievich | 109038 | skraglievich@fi.uba.ar |
| Edgardo Francisco Saez | 104896 | esaez@fi.uba.ar |
| Carolina Lucia Mauro | 108294 | cmauro@fi.uba.ar |
| Martin Wainwright | 108211 | mwainwright@fi.uba.ar |
| Mateo Bulnes | 106211 | mbulnes@fi.uba.ar |


## Manual de ejecución

Para poder ejecutar la hay que seguir lo siguientes pasos:
1. Instalar las dependencias necesarias:
    - `pip install streamlit pandas joblib gdown`
 
2. Ejecutar el siguiente comando en la terminal para correr la aplicacion:
    - `streamlit run app.py`

3. Navegar hacia http://localhost:8501.

4. Para utilizar el modelo simplemente agregas un `.csv` con datos nuevos para predecir (sin la columna objetivo). Las predecciones se mostraran por pantalla.
    - Hay un archivo de test en este repositorio. Se encuentra en `Dataset/hotels_test.csv`.

Ahora bien, para cerrar la aplicacion, primero probar con el comando `Ctrl+C` en la terminal donde esta corriendo el proceso de streamlit. Si esto no funciona, hay que matar el proceso manualmente.
