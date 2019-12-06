from pymongo import MongoClient
import matplotlib.pyplot as plt
import random

connection = "mongodb://Charlie:PRO335@pro335-cluster-shard-00-00-1lows.azure.mongodb.net:27017,pro335-cluster-shard-00-01-1lows.azure.mongodb.net:27017,pro335-cluster-shard-00-02-1lows.azure.mongodb.net:27017/test?ssl=true&replicaSet=Pro335-Cluster-shard-0&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(connection)
db = client["Imdb_Pro335_DB"]
serverStatusResult = db.command("serverStatus")
#print(serverStatusResult)

def get_db():
    from pymongo import MongoClient
    db = client.myFirstMB
    return db
    
def get_country(db):
    return db.Movies.find_one()

db = get_db() 
print(get_country(db))

#Line Graph Demo ------------------------------------------------------------------------------------------------

# In next cell
# "label" used for legend
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)], 'b*-', label='Movie Likes') 
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)],'r*-', label='Actor Likes')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)], 'g*-', label='Director Likes')

# Set the title for the current axes
plt.title('Movie Correlation Data')

# Set the axes labels and ranges for the current axes
plt.xlabel('Facebook likes.')
plt.ylabel('The movie gross income.')

# [xmin, xmax, ymin, ymax]
plt.axis([0, 10, 0, 10])  

# Setup legend on the current axes
plt.legend()

# Save the figure to file
plt.savefig('PlotMovieCorrelation.png', dpi=600, format='png')
# Show figure, clear figure and free memory
plt.show()  

#------------------------------------------------------------------------------------------------------------------

Movies = { 
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

Directors = {
    "Director_name": "",
    "Director_facebook_likes": 0
}

Actors = {
    "name": "",
    "facebook_likes": 0
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