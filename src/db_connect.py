from pymongo import MongoClient
from pprint import pprint

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

    