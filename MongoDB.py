
import pymongo



#https://www.mongodb.com/download-center/enterprise



def Creating_Database():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]


def Creating_Collection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]


def Check_Collection_Exists():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")


def Inserting_Data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = {"name": "John", "address": "Highway 37"}

    x = mycol.insert_one(mydict)


def query():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = {"address": "Park Lane 38"}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)