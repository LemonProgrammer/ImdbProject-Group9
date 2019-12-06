import csv
import pprint as pp
from pymongo import MongoClient
dbURL = "mongodb://Fernando:PRO335@pro335-cluster-shard-00-00-1lows.azure.mongodb.net:27017,pro335-cluster-shard-00-01-1lows.azure.mongodb.net:27017,pro335-cluster-shard-00-02-1lows.azure.mongodb.net:27017/test?ssl=true&replicaSet=Pro335-Cluster-shard-0&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(dbURL)
# db = client.admin
db = client["Imdb_Pro335_DB"]
# serverStatusRes = db.command("serverStatus")
# pp.pprint(serverStatusRes)

# filepath = "../PythonProject/movie_metadata.csv"
parsedMovies = []
movieDictionary = {}
# movieFile = open(filepath, encoding="utf8")

def MapColumnNamesToIndexValues():
    global parsedMovies, movieDictionary
    movieColumnNames = parsedMovies[0]
    colCount = 0
    for col in movieColumnNames:
        colName = str(col)
        movieDictionary.update({colName : colCount})
        colCount += 1
    # print(str(parsedMovies[0]))
    # print(str(movieDictionary))


def ParseRecords(reader):
    global parsedMovies
    for row in reader:
            fields_movie = []
            # print("row: " + str(row))
            for col in row:
                fields_movie.append(col)
            parsedMovies.append(fields_movie)

def ImportParsedDataToDB():
    global parsedMovies, movieDictionary, db

    movieInd = 0
    
    moviesCollection = db["Movies"]
    actorsCollection = db["Actors"]
    directorsCollection = db["Directors"]

    MapColumnNamesToIndexValues()
    # mp = pp.PrettyPrinter(indent=3)
    # mp.pprint(movieDictionary)
    # actorStr = "actor_"
    # directStr = "director_"

    actors = []
    directors = []
    movies = []

    actorColNums = [7,10,24,6,5,14]
    directorColNums = [4,1]
    for movieRow in parsedMovies:
        actor = {}
        director = {}
        movie = {}
        fieldIndex = 0
        # movieRow = parsedMovies[movieInd]
        # print(m)
        # entity.update({'movie_title' : movieRow[11]})
        for field in movieRow:
            # check if its a movie title column and put it in entity 
            for c in movieDictionary:
                if  movieDictionary[c] == 11 and fieldIndex == 11:
                    actor.update({c : field})
                    director.update({c : field})
                    movie.update({c : field})
                else:
                    for ac in actorColNums:
                        if fieldIndex != ac:
                            for dc in directorColNums:
                                if fieldIndex != dc:
                                    # for md in movieDictionary:
                                    if movieDictionary[c] == fieldIndex:
                                      movie.update({c : movieRow[fieldIndex]})
                                else:
                                    # for md1 in movieDictionary:
                                    if movieDictionary[c] == fieldIndex: 
                                        director.update({c : movieRow[fieldIndex]})
                                        break

                        else:
                            # for md2 in movieDictionary:
                              # and this
                            if movieDictionary[c] == fieldIndex:
                              actor.update({c : movieRow[fieldIndex]})
                            break
                            
            # else:
                
            fieldIndex += 1
        movies.append(movie)
        print("Appended movie in movies.")
        actors.append(actor)
        print("Appended actor in actors.")
        directors.append(director)
        print("Appended director in directors.")
        print("\n @ row " + str(movieInd) + "\n")
        movieInd += 1
    print("movies count: " + str(len(movies)))
    print("directors count: " + str(len(directors)))
    print("actors count: " + str(len(actors)))
    # ap = pp.PrettyPrinter(indent=4)
    # ap.pprint(actors)
    # print(directors[2])
    mcount = 0
    insertList = []
    for m in movies:
        insertList.append(m)
        if mcount % 1000 == 0:
            mRes = moviesCollection.insert_many(insertList)
            print("Inserted 1000 docs to movies collection: " + str(mRes))
            insertList = []
        if mcount - len(insertList) == 44:
            moviesCollection.insert_many(insertList)
            print("Inserting the rest of the movies...")
            break
        mcount += 1
    print("Inserted all movies in Movies Collection")
    insertList = []
    acount = 0
    for a in actors:
        insertList.append(a)
        if acount % 1000 == 0:
            aRes = actorsCollection.insert_many(insertList)
            print("Inserted 1000 docs to actors collection: " + str(aRes))
            insertList = []
        if acount - len(insertList) == 44:
            actorsCollection.insert_many(insertList)
            print("Inserting the rest of the actors...")
        acount += 1
    # aRes = actorsCollection.insert_many(actors)
    print("Inserted all actors in Actors Collection")
    # dRes = directorsCollection.insert_many(directors)
    insertList = []
    dcount = 0
    for d in directors:
        insertList.append(d)
        if dcount % 1000 == 0:
            dRes = directorsCollection.insert_many(insertList)
            print("Inserted 1000 docs to directors collection: " + str(dRes))
            insertList = []
        if dcount - len(insertList) == 44:
            actorsCollection.insert_many(insertList)
            print("Inserting the rest of the directors...")
        dcount += 1
    print("Inserted all directors in Directors Collection")


def ReadImdbFile(ifile):
    with open(ifile, newline='', encoding="utf8") as csvfile:
        imdbReader = csv.reader(csvfile,  delimiter=',', quotechar='|')
        ParseRecords(imdbReader)

# ReadImdbFile(filepath)
# ImportParsedDataToDB()
# print(str(parsedMovies))