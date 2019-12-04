from tkinter import Tk, Menu, Frame
from pymongo import MongoClient
from pprint import pprint

connection = "mongodb://Fernando:PRO335@pro335-cluster-shard-00-00-1lows.azure.mongodb.net:27017,pro335-cluster-shard-00-01-1lows.azure.mongodb.net:27017,pro335-cluster-shard-00-02-1lows.azure.mongodb.net:27017/test?ssl=true&replicaSet=Pro335-Cluster-shard-0&authSource=admin&retryWrites=true&w=majority"



root = Tk()
root.title("Internet Movie Database Project")
root.minsize(480, 360)
root.maxsize(1920, 1080)

client = MongoClient(connection)
db=client.admin
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

movie = { 
    "Movies": {
        "Color": "",
        "Duration": "",
        "Actor_3": "",
        "Actor_2": "",
        "Actor_1": "",
        "Gross": 0,
        "Genres": [],
        "Movie_title": "",
        "Num_voted_users": 0,
        "Cast_total_facebook": 0,
        "Facenumber_in_poster": 0,
        "Plot_keywords": [],
        "Movie_imdb_link": "",
        "Num_user_for_reviews": 0,
        "Language": "",
        "Country": "",
        "Content_rating": "",
        "Budget": 0,
        "Title_year": "",
        "Imdb_score": 0.0,
        "Aspect_ratio": 0.0,
        "Movie_facebook_likes": 0
    }
}

def Q1():
    #Does the movie’s amount of facebook likes correlate with its gross amount made.
    print()

def Q2():
    #The Actors association to the movie to bring success to the film.
    print()

def Q3():
    #The Directors association to the movie to bring success to the film.
    print()

root.mainloop()