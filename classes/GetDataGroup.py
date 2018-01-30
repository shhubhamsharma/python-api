from flask_restful import Resource
from flask import request
from database.db import *
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_restful import reqparse
from flask import request

class GetDataGroup(Resource):
    def post(self):
        jsonD=request.json['data']
        platform= jsonD['platform']
        query="SELECT COUNT(*) AS fragcount,uid,platform FROM `task` WHERE platform='%s' GROUP BY uid ORDER BY uid"%(platform)
        data=connectMySQL(query)
        result = {'data':json.loads(json.dumps(data, indent=3) )}    
        return result