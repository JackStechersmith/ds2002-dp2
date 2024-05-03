#!/usr/bin/env python3

import pymongo
from pymongo import MongoClient, errors
from bson.json_util import dumps
import json
import os

MYMONGO = os.getenv('MYMONGO')
client = MongoClient("mongodb+srv://cluster0.v3fakhg.mongodb.net/svc8ft", username='jackstechersmith', password=MYMONGO, connectTimeoutMS=200, retryWrites=True)
db = client.dp2
collection = db.myimports

collection.drop()

directory = "data"

counter = 0


for filename in os.listdir(directory):
    counter += 1
    if counter > 50:
        break
    else:
        with open(os.path.join(directory, filename)) as f:
            # assuming you have defined a connection to your db and collection already:
            # Loading or Opening the json file
            try:
                file_data = json.load(f)
            except Exception as e:
                print(e, "error when loading", f)

# Inserting the loaded data in the collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used

            if isinstance(file_data, list):
                try:
                    collection.insert_many(file_data)
                except Exception as e:
                    print(e, "when importing into Mongo")
                    continue
            else:
                try:
                    collection.insert_one(file_data)
                except Exception as e:
                    print(e)
                    continue
