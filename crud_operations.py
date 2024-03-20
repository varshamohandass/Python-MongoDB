import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import json


def create(collection_name, doc):
    # print(doc)
    # print(type(doc))
    collection_name.insert_one(json.loads(doc))
    print('Document inserted successfully')

def create_many(collection_name,doc):
    for i in doc:
        collection_name.insert_one(json.loads(i))
    print('Documents inserted successfully')

def read(collection_name):
    data = collection_name.find()
    for document in data:
        pprint(document)

# def read_one(user_name):
#     data = collection_name.find_one({'username':user_name})

def update(collection_name,user_name, updated_values):
    collection_name.update_one({'username':user_name}, {'$set':json.loads(updated_values)})

def delete(collection_name,user_name):
    collection_name.delete_one({"username": user_name})




load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

#reading the number of databases 
client = MongoClient(MONGODB_URI)

def crud_op(dbname,table_name):


    collection_name = dbname[table_name]

    choice = input('''Choose an Operation: 
                \n 1. Create
                \n 2. Read 
                \n 3. Update 
                \n 64. Delete : ''')

    if choice == "Create":
        document = input("Enter documet: ")
        create(collection_name,document)
    elif choice == "Read":
        # user_name = input("Enter user name: ")
        read(collection_name)
    elif choice == 'Update':
        user_name = input("Enter user name: ")
        updated_values = input("Enter values need to be updated with their keys")
        update(collection_name,user_name,updated_values)

    elif choice == 'Delete':
        user_name = input("Enter user name: ")
        delete(collection_name,user_name)



