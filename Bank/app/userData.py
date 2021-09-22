# Serve api request

from Bank.config import client
from Bank.app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
from importlib.machinery import SourceFileLoader

# Import the helpers module
helper_module = SourceFileLoader('*', './app/helpers.py').load_module()

# select the database
db = client.Bank_Project
# select the collection
collection = db.Sample


# @app.route("/add")
# def index():
#
#     return '<h1> Hello World </h1>'

@app.route("/")
def get_initial_response():
    # welcome message from API
    message = {
        'Project Title': 'BANK SYSTEM',
        'apiversion': 'v1.0',
        'status': '200',
        'message': 'Welcome from Flask API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp

@app.route("/api/users", methods=['POST'])
def create_user():
    # create new users
    try:
        try:
            body = ast.literal_eval(json.dumps((request.get_json())))
        except:
            return "",400

        record_created = collection.insert(body)

        if isinstance(record_created, list):
            return jsonify([str(v) for v in record_created]), 201
        else:
            return jsonify(str(record_created)), 201
    except:
        return "", 500


@app.route("/api/users", methods=['GET'])
def fetch_users():
    try:
        query_params = helper_module.parse_query_params(request.query_string)
        if query_params:
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params}
            records_fetched = collection.find(query)

            if records_fetched.count() > 0:
                return dumps(records_fetched)
            else:
                return "", 404
        else:
            if collection.find().count() > 0:
                return dumps(collection.find())
            else:
                return jsonify([])
    except:
        return "", 500


@app.route("/api/users/user_id", methods=['POST'])
def update_user(user_id):
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "", 400

        records_updated = collection.update_one({"id": int(user_id)}, body)

        if records_updated.modified_count > 0:
            return "", 200
        else:
            return "", 404
    except:
        return "", 500


@app.route("/api/users/user_id", methods=['DELETE'])
def remove_user(user_id):
    try:
        delete_user = collection.delete_one({"id": int(user_id)})
        # if user_id in Sample:
        #     del Sample[user_id]
        #     res = make_response(jsonify({"msg": "Deleted.."}), 204)
        #     return res
        if delete_user.delete_count > 0:
            return "", 204
        else:
            return "", 404
    except:
        return "", 500


# @app.errorhandler(404)
# def page_not_found(e):
#     return "", 404
