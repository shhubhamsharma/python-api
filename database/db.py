import mysql.connector
import datetime
import decimal
import os
# from mysql.connector import Error
from sqlalchemy import create_engine
import json
import redis
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import dbconfig
def date_handler(obj):
    
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    if hasattr(obj, 'isoformat'):
        return obj.isoformat() 
    else:
        raise TypeError(
            "Unserializable object {} of type {}".format(obj, type(obj))
            )
# if cnx.is_connected():
#             print('Connected to MySQL database')
# print(cnx.json)
dbconfig=dbconfig.dbConfig
def connectMySQL(query):
    

    cnx=create_engine('mysql+mysqlconnector://'+dbconfig['user']+':'+dbconfig['passwd']+'@'+dbconfig['host']+'/'+dbconfig['db'])
    cursor = cnx.connect() 
    query=cursor.execute(query)
    column=query._metadata.keys
    print(column)
    rows = query.fetchall()
    print(cursor)
    column = [t for t in column]
    i=0
    myresult=list()
    # myjson = [{column[0]: row[0], column[1]: row[1], column[2]: row[2]} for row in rows]
    for row in rows:
        myresult.append(dict(zip(column,row)))
    return json.loads(json.dumps(myresult, indent=3,default=date_handler) )

def connectRedis():
    rediscon=redis.Redis(
    host='localhost',
    port=6379)
    return rediscon

def mongo():
    try:
       c= MongoClient(host="localhost",port=27017)
    except ConnectionFailure:
        print("Error Occured")
    dbh = c["mydb"]
    
    return dbh

def close():
    cnx.commit()
    cnx.close()
