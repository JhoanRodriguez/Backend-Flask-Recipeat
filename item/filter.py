import os
import pymongo
from bson.json_util import dumps

# Fetch mongo env vars
usr = os.environ['MONGO_DB_USER']
pwd = os.environ['MONGO_DB_PASS']
mongo_db_name = os.environ['MONGO_DB_NAME']
mongo_collection_name = os.environ['MONGO_COLLECTION_NAME']
url = os.environ['MONGO_DB_URL']

# Connection String
client = pymongo.MongoClient(
    "mongodb+srv://" + usr + ":" + pwd + "@" + url
    + "/test?retryWrites=true&w=majority")
db = client[mongo_db_name]
collection = db[mongo_collection_name]


def filter(event, context):
    """Retieves an object with the query string parameters

    Args:
        event ([object]): Contains all event related keys
        context ([object]): Contains all context related keys

    Returns:
        [object]: A json object with the matches.
    """
    parameters = event["queryStringParameters"]["search"]
    item = collection.find({"$text": {"$search": parameters}})

    # create a response
    response = {
        "statusCode": 200,
        "body": dumps(item)
    }
    # return response
    return response
