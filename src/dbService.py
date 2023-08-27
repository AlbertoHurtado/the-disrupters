import pymongo
import os
import json
from dotenv import load_dotenv
load_dotenv()

class MongoDBService:
    def __init__(self):
        self.client = pymongo.MongoClient(os.getenv("MONGO_URI"))
        self.database = self.client[os.getenv("DATABASE_NAME")]
        self.collection = self.database[os.getenv("COLLECTION_NAME")]

    def find_matches(self, query, limit=5):
        cursor = self.collection.find(query).limit(limit)
        json_results = [json.dumps(document, default=str) for document in cursor]
        props_dict = [json.loads(json_document) for json_document in json_results]
        return props_dict

    def close(self):
        if self.client:
            self.client.close()