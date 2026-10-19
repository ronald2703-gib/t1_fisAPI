from fastapi import FastAPI, HTTPException, status
from src.templates.controllers import (
    create_trainee, 
    get_all_trainees, 
    get_trainee_by_id, 
    update_trainee, 
    delete_trainee
)
from src.models.model import TraineeModel, TraineeUpdateModel

MONGO_URI = "mongodb+srv://ronaldlunavitydarte_db_user:Jz4viiqtMwZORVzq@cluster0.lmdgg5f.mongodb.net/?appName=Cluster0"



# Comando para arrancar en terminal:
# uvicorn src.main:app --reload

app = FastAPI(
    title="Gestión de datos de los aprendices",
    description="API simple con FastApi para consumir los datos de los aprendices",
    version="1.0.0",
)

# 1. Mensaje de bienvenida
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de gestión de aprendices"}

# 2. Registrar aprendices
@app.post(
    "/trainees/", 
    response_description="Registrar un nuevo aprendiz", 
    status_code=status.HTTP_201_CREATED
)
def create_trainee_api(trainee: TraineeModel):
    # Validar si ya existe el documento
    return create_trainee(trainee)

# 3. Obtener la lista de aprendices
@app.get(
    "/trainees/", 
    response_description="Listar todos los aprendices"
)
def get_all_trainees_appi():
    return get_all_trainees()

# 4. Obtener un aprendiz por ID
@app.get(
    "/trainees/{id}", 
    response_description="Obtener un aprendiz por ID"
)
def get_trainee_by_id_api(id: str):
    trainee = get_trainee_by_id(id)
    if not trainee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Aprendiz no encontrado"
        )
    return trainee

# 5. Actualizar aprendiz
@app.put(
    "/trainees/{id}", 
    response_description="Actualizar un aprendiz"
)
def update_trainee_api(id: str, trainee: TraineeUpdateModel):
    trainee_updated = update_trainee(id, trainee)
    if not trainee_updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Aprendiz no encontrado"
        )
    return trainee_updated

# 6. Eliminar aprendiz
@app.delete(
    "/trainees/{id}", 
    response_description="Eliminar un aprendiz"
)
def delete_trainee_api(id: str):
    trainee_deleted = delete_trainee(id)
    if not trainee_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Aprendiz no encontrado"
        )
    return {"message": "Aprendiz eliminado correctamente"}
