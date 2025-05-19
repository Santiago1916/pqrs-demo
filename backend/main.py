from fastapi import FastAPI
from dotenv import load_dotenv
from routes import users, pqrs, response

load_dotenv()

app = FastAPI()

# Incluir los routers
app.include_router(users.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(pqrs.router, prefix="/pqrs", tags=["PQRS"])
app.include_router(response.router, prefix="/respuestas", tags=["Respuestas"])

# Ruta de prueba de conexión
@app.get("/test")
def test_connection():
    try:
        # Asegúrate de que la tabla se llama 'pqrs'
        from services.supabase import supabase
        response = supabase.table("pqrs").select("*").limit(1).execute()
        return {
            "estado": "conectado ✅",
            "tabla": "pqrs",
            "datos_de_prueba": response.data
        }
    except Exception as e:
        return {
            "estado": "error ❌",
            "detalle": str(e)
        }
