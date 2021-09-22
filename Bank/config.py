#
import pymongo
from pymongo import MongoClient

DEBUG = True
client = pymongo.MongoClient("mongodb://localhost:27017/")
DATABASE = client['restfulapi']