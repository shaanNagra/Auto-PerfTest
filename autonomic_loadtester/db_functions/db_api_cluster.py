#!/usr/bin/python

import pymongo
import pandas as pd
import db_conn
from db_constants import AppCol,SessionCol,CallCol

# ////////////////FILE DESCRIPTION/////////////////
# functions that interact with the mongodb database
#  for use in the clustering functionallity
#  (is the interface for clustering module)
# /////////////////////////////////////////////////

#------------------------------------------
# 
#------------------------------------------
def getNewSessions(webappID):
    
    client = db_conn.connect()
    try:
        res = []
        data = client.sessions.find({
            SessionCol.application:webappID,
            SessionCol.processed:False
            })
        
        for session in data:
            # print("s"+str(session))
            res.append(session.get(SessionCol.id))
        
        print("OUT: new sessions returned")
        return res

    except pymongo.errors.PyMongoError as e:
        print("ERR: could not get data")
        print("ERR: "+e)
        return None


#------------------------------------------
# 
#------------------------------------------
def getSessionCalls(session_id=" "):
    
    client = db_conn.connect()
    
    try:
        res = []
        data = client.calls.find({
            CallCol.session:session_id
            }).sort(CallCol.time)
        
        for call in data:
            res+=[(
                call.get(CallCol.id),
                call.get(CallCol.operation),
                call.get(CallCol.time),
                call.get(CallCol.time)
                )]
        
        print("OUT: returned records as DF")
        return pd.DataFrame.from_records(res,columns=['id','op','x','y'])
    
    except pymongo.errors.PyMongoError as e:
        print("ERR: could not get data")
        print("ERR: "+e)
        return None


#------------------------------------------
# 
#------------------------------------------
def setSessionClusterd(session_id):
    
    client = db_conn.connect()
    try:
        update = { "$set": { SessionCol.processed: True } }
        client.sessions.update_one({
            SessionCol.id:session_id
            },update)
        
        print("OUT:")
        return True

    except pymongo.errors.PyMongoError as e:
        print("ERR: ")
        print("ERR: "+e)
        return False


#------------------------------------------
# 
#------------------------------------------
def setSessionFailed(session_id):
    
    client = db_conn.connect()
    try:
        update = { "$set": { "processed": None } }
        client.sessions.update_one({
            SessionCol.id:session_id
            },update)

        print("OUT:")
        return True
    
    except pymongo.errors.PyMongoError as e:
        print("ERR: ")
        print("ERR: "+e)
        return False


#------------------------------------------
# 
#------------------------------------------
def setCallLabels(results):
    
    client = db_conn.connect()
    try:
        bulk = client.calls.initialize_unordered_bulk_op()
        
        for i in results:
            bulk.find({
                CallCol.id:i[0]
                }).update({
                '$set':{
                    CallCol.label:str(i[4])
                    }
                })

        bulk.execute()

        print("OUT:")
        return True

    except pymongo.errors.PyMongoError as e:
        print("ERR: ")
        print("ERR: "+e)
        return None
