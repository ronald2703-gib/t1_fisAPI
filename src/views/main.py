from src.templates.controllers import create_trainee, get_all_trainees, get_trainee_by_id, update_trainee, delete_trainee
from fastapi import FastAPI, HTTPException, status
from src.models.model import TraineeModel, TraineeUpdateModel
# uvicorn src.main:app --reload

app = FastAPI(
    title="Gestión de datos de los aprendices",
    description="API simple con FastApi para consumir los datos de los aprendices",
    version="1.0.0",
)
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de gestión de aprendices"}