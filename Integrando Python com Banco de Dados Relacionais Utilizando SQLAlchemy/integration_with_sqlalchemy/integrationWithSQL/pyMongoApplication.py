import datetime
import pprint

import pymongo as pyM
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://victo29:teste123@cluster0.w7nycpj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.test
collection = db.test_collection
print(db.test_collection)

# definição de infor para compor doc
post = {
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
'''
print(post_id)

print(db.posts.find_one())

pprint.pprint(db.posts.find_one())
'''

# bulk inserts
new_post = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()
    },
    {
        "author": "Victor",
        "text": "post from Victor. New post available",
        "title": "Mongo is fun",
        "date": datetime.datetime.utcnow()
    }]

result = posts.insert_many(new_post)
print(result.inserted_ids)

print("--------------------------------------------")
pprint.pprint(db.posts.find_one())

print("--------------------------------------------")
pprint.pprint(db.posts.find_one({"author": "Victor"}))

print("\n--------------------------------------------")
print("Recuperando todos os documentos")
for post in posts.find():
    pprint.pprint(post)

