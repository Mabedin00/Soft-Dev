from pymongo import MongoClient

client = MongoClient() # sets to localhost automatically
db = client.MosDB

col = db.movies

def get_movies_by_us_gross(gross):
    gross = int(gross)
    return [(movie_data["Title"], movie_data["US_Gross"]) for movie_data in col.find({"US_Gross": {"$gt": gross}})]

def get_movies_by_rating(IMDB, Rotten_Tomatoes):
    Rotten_Tomatoes = int(Rotten_Tomatoes)
    IMDB = int(IMDB)

    return [(movie_data["Title"], movie_data["IMDB_Rating"], movie_data["Rotten_Tomatoes_Rating"])   for movie_data in col.find(\
	{"Rotten_Tomatoes_Rating": {"$gt": Rotten_Tomatoes}, "IMDB_Rating": {"$gt": IMDB}})]

def get_movies_by_year(year):
    year = int(year)
    return [(movie["Title"], movie["Release_Date"]) for movie in col.find({}) if int(movie["Release_Date"][-4:]) > year]

def get_movies_by_genre(genre):
    genre = genre.capitalize()
    return [(movie["Title"], movie["Major_Genre"])  for movie in col.find({"Major_Genre": genre})]

def is_your_name_popular(name):
    movies = list(col.find({}))
    for movie in movies:
        if (movie["Director"] != None and name in movie["Director"] and movie["IMDB_Votes"] > 1000):
            return True
    return False

# print(get_movies_by_rating(8, 80))
# print(get_movies_by_us_gross(50000000))
# list = get_movies_by_year(2007)
# print(list)
# print(get_movies_by_genre("Drama"))
# print(is_your_name_popular("Greg"))
