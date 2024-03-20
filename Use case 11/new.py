from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pprint import pprint
import sys
from datetime import datetime
load_dotenv()

MONGODB_URI = os.environ['MONGODB_URI']
client = MongoClient(MONGODB_URI)
dbname = client['basicauth']
# collection_name = dbname["password"]
table_password = dbname['table_pwd']
table1 = dbname["Orders"]
table2 = dbname["OrderDetails"]
table3 = dbname["Products"]

table_password.insert_many([{'table':'Orders', 'password':'orders'},{'table':'OrderDetails', 'password':'orderdetails'},{'table':'Products', 'password':'products'}])
pprint("success")

table1.insert_one({"orderId":12345, "customerId":"CA3684", "dateOrdered":"2024-01-01", "status":"Order packed"})

table2.insert_one({"orderId": 12345,"productId": "AVD4603","quantity": 4,"lineNumber":"10"})

table3.insert_one({"productId":"AVD4603","name":"NUVERA","description":"coloured printer","quantity":4,"unitPrice":150})