from flask_restful import Resource
from flask import request
from database.db import *
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_restful import marshal_with
from flask_restful import reqparse
from flask import request

class GetPlatform(Resource):
    def get(self):
        query="SELECT DISTINCT(platform) FROM task"
        data=connectMySQL(query)
        result = {'data':json.loads(json.dumps(data, indent=3) )}    
        return result