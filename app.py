from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from classes.GetData import GetData
from classes.GetUniqueID import GetDataUnique
from classes.GetPlatform import GetPlatform

app=Flask(__name__)
CORS(app)
api=Api(app)
import os
import mysql.connector
from mysql.connector import Error
from classes.GetDataGroup import GetDataGroup
import json
# port = int(os.getenv("PORT",3100))
port = int(os.getenv('VCAP_APP_PORT', 3100))
print("listening on "+str(port))

api.add_resource(GetData,'/getData','/getData')
api.add_resource(GetPlatform,'/getplatform','/getplatform')

api.add_resource(GetDataUnique,'/getUnique','/getData')
api.add_resource(GetDataGroup,'/getGroup','/getGroup')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=port)