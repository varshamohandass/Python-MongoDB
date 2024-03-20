from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pprint import pprint
import sys
import crud_operations as co

load_dotenv()

MONGODB_URI = os.environ['MONGODB_URI']
client = MongoClient(MONGODB_URI)
dbname = client['basicauth']
table_password = dbname['table_pwd']
table1 = dbname["Orders"]
table2 = dbname["OrderDetails"]
table3 = dbname["Products"]

# password = sys.argv[1]
# pwd_db = collection_name.find_one({'pwd':password})
table_name = sys.argv[1]
table_pwd = sys.argv[2]


table_auth = table_password.find_one({"table":table_name})
# pprint(table_auth['password'])

if table_name == "Orders" and table_pwd == table_auth['password']:
    co.crud_op(dbname, table_name)

elif table_name == "OrderDetails" and table_pwd == table_auth['password']:
    co.crud_op(dbname, table_name)

elif table_name == "Products" and table_pwd == table_auth['password']:
    co.crud_op(dbname, table_name)
else:
    print("try again")
    

    



