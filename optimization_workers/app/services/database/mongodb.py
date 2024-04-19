# TODO: Implement the MongoDB service for the optimization workers
import os

from pymongo import MongoClient

mongo_client: MongoClient = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client.rmo_database
