import mysql.connector
import datetime
import decimal
from sqlalchemy import create_engine
import json
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
dbconfig=dbconfig.dbConfig
def connectMySQL(query):
    

    cnx=create_engine('mysql+mysqlconnector://'+dbconfig['user']+':'+dbconfig['passwd']+'@'+dbconfig['host']+'/'+dbconfig['db'])
    cursor = cnx.connect() 
    query=cursor.execute(query)
    column=query._metadata.keys
    rows = query.fetchall()
    column = [t for t in column]
    i=0
    myresult=list()
    for row in rows:
        myresult.append(dict(zip(column,row)))
    return json.loads(json.dumps(myresult, indent=3,default=date_handler) )

def close():
    cnx.commit()
    cnx.close()
