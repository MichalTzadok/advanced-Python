from pymongo import MongoClient

client = MongoClient("")

db = client['sample']
users = db['sample']
