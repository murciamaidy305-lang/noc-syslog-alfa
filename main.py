# Importamos la herramienta FastAPI
from fastapi import FastAPI

# Inicializamos la aplicación
app = FastAPI(
    title="NOC Syslog Inteligente",
    description="Versión Alfa para gestión de redes",
    version="0.1.0"
)

# Creamos nuestra primera "Ruta" o URL
# El decorador @app.get("/") le dice que responda cuando visitemos la página principal
@app.get("/")
def leer_raiz():
    # Devuelve un mensaje de bienvenida en formato de datos (JSON)
    return {
        "mensaje": "¡Hola Maidy! Tu NOC Inteligente está funcionando.",
        "estado": "Alfa"
    }