from pymongo import MongoClient
import json

client = MongoClient() # sets to localhost automatically
db = client.MosDB
col = db.movies

def setup():
    with open('movies.json', encoding="utf8") as json_file:
        movies_string = json_file.read()
        movies_list = json.loads(movies_string)
        col.insert_many(movies_list)

def delt():
    col.delete_many({})
    print("ge")
