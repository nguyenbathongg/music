from pymongo import MongoClient
import os

client = MongoClient("mongodb://localhost:27017")
db = client["backend_db"]
users_collection = db["users"]
songs_collection = db["songs"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
