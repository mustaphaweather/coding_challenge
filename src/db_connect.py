from pymongo import MongoClient
from pprint import pprint

try:
    client = MongoClient("mongodb+srv://mustapha:Cerona7h@cluster0-jtqqb.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db=client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)
except:
    print("connection error")

mydb = client["challenge_code"]
mycol = mydb["bbc_articles"]
print(mycol)