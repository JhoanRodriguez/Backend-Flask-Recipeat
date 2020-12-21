from flask import Flask, request, jsonify
import os
import pymongo
from dotenv import load_dotenv
import uuid


# Fetch mongo env vars
load_dotenv()
usr = os.environ['MONGO_DB_USER']
pwd = os.environ['MONGO_DB_PASS']
mongo_db_name = os.environ['MONGO_DB_NAME']
mongo_collection_name = os.environ['MONGO_COLLECTION_NAME']
url = os.environ['MONGO_DB_URL']

app = Flask(__name__)

# Connection String
client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd +
                             "@" + url + "/" + mongo_db_name +
                             "?retryWrites=true&w=majority")

db = client[mongo_db_name]
collection = db[mongo_collection_name]


@app.route('/api/recipes', methods=['GET'])
def Get_Recipes():
    # Getting all data
    response = []
    cursor = collection.find()
    for document in cursor:
        response.append(document)

    # return response
    return jsonify({'response_items': response}), 200


@app.route('/api/recipes/<id>', methods=['GET'])
def Get_Recipe(id):
    # Get a recipe from the ID
    response = []
    cursor = collection.find_one({"_id": id})
    response.append(cursor)
    if response[0] is None:
        return jsonify({'message': 'Recipe not found'}), 404
    # return response
    return jsonify({'response_items': response}), 200


@app.route('/api/recipes/<id>', methods=['DELETE'])
def Del_Recipe(id):
    # Delete a recipe from the ID
    cursor = collection.delete_one({"_id": id})
    if cursor.deleted_count == 0:
        return jsonify({'message': 'Recipe not found'}), 404

    # return response
    return jsonify({'message': 'Recipe Deleted'}), 200


@app.route('/api/recipes', methods=['POST'])
def New_Recipe():
    # Create a new recipe
    data = request.json['body']
    item = {
        '_id': str(uuid.uuid1()),
        'data': data,
    }
    # write item to database
    collection.insert_one(item)
    # return response
    return jsonify({'message': 'Recipe Created'}), 200


@app.route('/api/search<item>', methods=['GET'])
def Search_by(item):
    # Search by ingredients
    response = []
    print(item)
    cursor = collection.find({"$text": {"$search": item}})
    for document in cursor:
        response.append(document)

    # return response
    return jsonify({'response_items': response}), 200


if __name__ == "__main__":
    app.run(debug=True)