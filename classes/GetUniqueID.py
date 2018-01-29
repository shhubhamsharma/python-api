from flask_restful import Resource
from flask import request
from database.db import *
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_restful import reqparse
from flask import request

class GetDataUnique(Resource):
    def post(self):
        jsonD=request.json['data']
        platform= jsonD['platform']
        query="SELECT DISTINCT(uid) as uid ,COUNT(*) AS ucount FROM task WHERE platform='%s' GROUP BY uid"%(platform)
        test=connectMySQL(query)
        result = {'data':json.loads(json.dumps(test, indent=3) )}    
        return result