from bson import ObjectId
from src.models.database import collection 
from src.models.model import TraineeModel, TraineeUpdateModel

def helper_trainee(trainee)-> dict:
    return{
        "_id": str (trainee["_id"]),
        "document": trainee["document"],
        "firstname": trainee["firstname"],
        "lastname": trainee["lastname"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"],
    }