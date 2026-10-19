from bson import ObjectId
from pymongo import MongoClient  # Importamos MongoClient directamente aquí
from src.models.model import TraineeModel, TraineeUpdateModel

# 1. Configuración de conexión local garantizada y forzada
MONGO_URI = "mongodb+srv://ronaldlunavitydarte_db_user:Jz4viiqtMwZORVzq@cluster0.lmdgg5f.mongodb.net/?appName=Cluster0"

# CORRECCIÓN: Se usa serverSelectionTimeoutMS (3000 ms = 3 segundos)
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

db = client["gestion_aprendices_db"]  # Nombre de tu Base de Datos
collection = db["trainees"]           # Nombre de tu Colección (Tabla)

# Función Helper para estructurar los diccionarios de MongoDB
def helper_trainee(trainee) -> dict:
    if not trainee:
        return None
    return {
        "id": str(trainee["_id"]),  # Cambiado a 'id' para coincidir con respuestas estándar de API
        "document": trainee.get("document"),
        "firstname": trainee.get("firstname"),
        "lastname": trainee.get("lastname"),
        "age": trainee.get("age"),
        "program": trainee.get("program"),
        "record_number": trainee.get("record_number"),
    }

# Registrar aprendiz
def create_trainee(trainee: TraineeModel) -> dict:
    trainee_dict = trainee.model_dump() 
    result = collection.insert_one(trainee_dict)
    new_trainee = collection.find_one({"_id": result.inserted_id})
    return helper_trainee(new_trainee)

# Obtener todos los aprendices
def get_all_trainees():
    trainees = []
    for trainee in collection.find():
        trainees.append(helper_trainee(trainee))
    return trainees

# Obtener datos de aprendiz por ID
def get_trainee_by_id(id: str):
    try:
        trainee = collection.find_one({"_id": ObjectId(id)})
        if trainee:
            return helper_trainee(trainee)
    except Exception:
        return None
    return None

# Actualizar datos del aprendiz
def update_trainee(id: str, data: TraineeUpdateModel):
    try:
        data_update = {
            k: v for k, v in data.model_dump().items() if v is not None
        }
        if data_update:
            collection.update_one({"_id": ObjectId(id)}, {"$set": data_update})
            trainee_updated = collection.find_one({"_id": ObjectId(id)})
            return helper_trainee(trainee_updated)
    except Exception:
        return None
    return None

# Eliminar aprendiz
def delete_trainee(id: str):
    try:
        trainee = collection.find_one({"_id": ObjectId(id)})
        if trainee:
            collection.delete_one({"_id": ObjectId(id)})
            return trainee
    except Exception:
        return None
    return None
