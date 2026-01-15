import os
import pymongo
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import HTTPException
load_dotenv("./.env")


MONGO_DB = os.getenv("MONGO_DB")

class DbCommunication(BaseModel):


    @staticmethod
    def get_conection():
        try:
            MONGO_HOST = os.getenv("MONGO_HOST")
            MONGO_PORT = int(os.getenv("MONGO_PORT"))
            MONGO_USERNAME = os.getenv("MONGO_USERNAME")
            MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
            client = pymongo.MongoClient(
                f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/",
                serverSelectionTimeoutMS=5000)
            return client
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"MongoDB connection failed: {str(e)}")




    @staticmethod
    def insert_to_db(data, collection_name):
        if not isinstance(data, list) or not data:
            raise HTTPException(status_code=400, detail="Data must be a non-empty list")
        try:
            client = DbCommunication.get_conection()
            MONGO_DB = os.getenv("MONGO_DB")
            db = client[MONGO_DB]
            collection = db[collection_name]
            collection.insert_many(data)
            return True
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to insert data: {str(e)}")


