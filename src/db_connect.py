from pymongo import MongoClient
from pprint import pprint
from pymongo import TEXT

## FUNCTION TO STORE NEW ARTICLES
def add_article(article):
    try:
        ## DB CONNECTION
        client = MongoClient("mongodb+srv://mustapha:Cerona7h@cluster0-jtqqb.gcp.mongodb.net/test?retryWrites=true&w=majority")

        ## INSERTION
        mydb = client["challenge_code"]
        mycol = mydb["bbc_articles"]
        # mycol.insert_one(article)
        mycol.insert_many(article)
        print("NEW ARTICLES ADDED SUCCESSFULY")
    except:
        print("connection error")
        exit()

## FUNCTION TO READ ALL ARTICLES
def read_data_all():
    try:
        ## DB CONNECTION
        client = MongoClient("mongodb+srv://mustapha:Cerona7h@cluster0-jtqqb.gcp.mongodb.net/test?retryWrites=true&w=majority")

        ## INSERTION
        mydb = client["challenge_code"]
        mycol = mydb["bbc_articles"]
        # mycol.insert_one(article)
        results = mycol.find({})
        print("READ ARTICLES SUCCESSFULY")
        return list(results)
    except:
        print("connection error")
        return []
        exit()

### [!] TO BE ABLE TO SEARCH BY KEYWORD ON A COLLECTION I HAD TO CREATE A TEXTINDEX ON MY COLLECTION USING
# myDB.bbc_articles.create_index( [("article", TEXT), ("title", TEXT) ] )
## FUNCTION TO FETCH ARTICLES BY KEYWORD
def fetch_data(keyword_):
    try:
        ## DB CONNECTION
        client = MongoClient("mongodb+srv://mustapha:Cerona7h@cluster0-jtqqb.gcp.mongodb.net/test?retryWrites=true&w=majority")

        ## INSERTION
        mydb = client["challenge_code"]
        mycol = mydb["bbc_articles"]
        mydb.bbc_articles.create_index( [("article", TEXT), ("title", TEXT) ] )
        results = mycol.find({"$text": {"$search": keyword_}})
        return list(results)
    except:
        print("connection error")
        return []
        exit()
    


