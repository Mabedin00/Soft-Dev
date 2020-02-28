from pymongo import MongoClient
import pprint
import json


client = MongoClient('localhost', 27017)
db = client.primer
restaurants = db.restaurants

def rest_by_bor(borough):
    return list(restaurants.find({"borough": borough}))[:3]

print("---------- 3 restaurants in a specified borough ----------")
pprint.pprint(rest_by_bor("Staten Island"))

def rest_by_zip(zip):
    return list(restaurants.find({"address.zipcode": zip}))[:3]

print("---------- 3 restaurants in a specified zip code. ----------")
pprint.pprint(rest_by_zip("11228"))

def rest_by_zip_grade(zip, grade):
    return list(restaurants.find({"$and": [{"address.zipcode": zip}, {"grades.grade": grade} ]})) [:3]

print("---------- restaurants in a specified zip code and with a specified grade ----------")

pprint.pprint(rest_by_zip_grade("11228", "C"))

def rest_by_zip_grade_1(zip, score):
    return list(restaurants.find({"$and": [{"address.zipcode": zip}, {"grades.score": {"$lt": score}} ]})) [:3]
print("---------- 3 restaurants in a specified zip code with a score below a specified threshold ----------")
pprint.pprint(rest_by_zip_grade_1("10303", 6))

def something_more_clever(zip, cuisine):
    return list(restaurants.find({"$and": [{"address.zipcode": zip}, {"cuisine": cuisine} ]})) [:3]

print("---------- Something more clever ----------")

pprint.pprint(something_more_clever("10303", "Spanish"))
