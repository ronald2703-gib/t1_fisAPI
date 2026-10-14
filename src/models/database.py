from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

#agregar la URI de conexion a tu base de datos MongODB
# URI de conexión de tu base de datos
MONGO_URI = "mongodb+srv://ronaldlunavitydarte_db_user:Jz4viiqtMwZORVzq@cluster0.lmdgg5f.mongodb.net/?appName=Cluster0"

# CORRECCIÓN: Se usa serverSelectionTimeoutMS (3000 ms = 3 segundos)
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)


#crear base de datos y coleccion

db = client.dataapren
collection = db.trainee

try:

#intentar obtener informacion del seridor para verificar la conexion

    client.server_info()
    print("conexion exitosa a mongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al concetar con mongoDB: {e}")
finally:
    client.close()