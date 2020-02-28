from pymongo import MongoClient
import pprint
import json

client = MongoClient('localhost', 27017)
db = client.primer
restaurants = db.restaurants

with open("primer-dataset.json", 'r') as file:
    dataset = file.read().replace("$date", "date")

restaurants.insert_many(json.loads(dataset))
