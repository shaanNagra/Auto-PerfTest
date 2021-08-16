#!/usr/bin/python

import pymongo
import pandas as pd

# def getNewSessionIDs(webappID):
def getNewSessions(webappID):
    client = connect()
    try:
        res = []
        data = client.sessions.find({'webapp':webappID,'processed':False})
        # data = client.sessions.find({'webapp':webappID})
        for session in data:
            # print("s"+str(session))
            res.append(session.get('_id'))
        return res
    except:
        print("could not get data")
        return None


# def getCallsDataFrame(session_id=" "):
def getSessionCalls(session_id=" "):
    
    client = connect()
    try:
        data = client.calls.find({'session_id':session_id}).sort("time")
        res = []

        for call in data:
            res+=[(call.get('_id'),call.get('operation'),call.get('time'),call.get('time'))]
        return pd.DataFrame.from_records(res,columns=['id','op','x','y'])
    except:
        print("could not get data")
        return None


def setSessionClusterd(session_id):
    client = connect()
    try:
        update = { "$set": { "processed": True } }
        client.sessions.update_one({"_id":session_id},update)
        return True
    except:
        print("AHAHAHAHAAH")
        return False

def setSessionFailed(session_id):
    client = connect()
    try:
        update = { "$set": { "processed": None } }
        client.sessions.update_one({"_id":session_id},update)
        return True
    except:
        print("AHAHAHAHAAH")
        return False


def setCallLabels(results):
    client = connect()
    try:
        bulk = client.calls.initialize_unordered_bulk_op()
        for i in results:
            bulk.find({'_id':i[0]}).update({'$set':{"label":str(i[4])}})
        bulk.execute()
        return True
    except:
        print("AHHHHHH")
        return None

def connect(url='localhost',port=27017,database='mydb'):
    try:
        client = pymongo.MongoClient(url,port)
        return client[database]
    except:
        print("could not connect to database")
        return None