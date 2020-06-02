from pymongo import MongoClient
from pprint import pprint
from pymongo import TEXT
import credentiels

## FUNCTION TO STORE NEW ARTICLES
def add_article(article):
    try:
        ## DB CONNECTION
        client = MongoClient()

        ## INSERTION
        mydb = client["challenge_code"]
        mycol = mydb["bbc_articles"]
        mycol.insert_many(article)
        print("NEW ARTICLES ADDED SUCCESSFULY")
    except:
        print("connection error")
        exit()

## FUNCTION TO READ ALL ARTICLES
def read_all():
    try:
        ## DB CONNECTION
        client = MongoClient(credentiels.URL_CONNECTION)

        ## READING
        mydb = client["challenge_code"]
        mycol = mydb["bbc_articles"]
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
def fetch_by_keyword(keyword_):
    try:
        ## DB CONNECTION
        client = MongoClient("mongodb+srv://mustapha:Cerona7h@cluster0-jtqqb.gcp.mongodb.net/test?retryWrites=true&w=majority")

        ## FETCH
        mydb = client["challenge_code"]
        mycol = mydb["bbc_articles"]
        mydb.bbc_articles.create_index( [("article", TEXT), ("title", TEXT) ] )
        results = mycol.find({"$text": {"$search": keyword_}})
        return list(results)
    except:
        print("connection error")
        return []
        exit()
    


