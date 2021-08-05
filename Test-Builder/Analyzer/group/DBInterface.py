#!/usr/bin/python

import pymongo
import pandas as pd
from pymongo import message

def getCallsList(session_id=""):
    client = connect()
    try:
        data = client.calls.find({'session_id':session_id}).sort("time")
        res = []

        for call in data:
            res+=[{call.get('_id'),call.get('operation'),call.get('time'),call.get('time'),call.get('label')}]
        return res
    except:
        print("could not get data")
        return None



def getClusteredSessions(webappID,version):
    client = connect()
    # try:
    res = []
    data = client.sessions.find({'webapp':webappID,'processed':True,'app_versoin':version})
    for session in data:
        if session.get('processed') == True:
            res.append(session.get('_id'))
    return res
    # except:
    #     print("could not get data")
    #     return None


def getSessionsForGrouping(session_id):
    client = connect()
    # try:
    data = client.calls.find({'session_id':session_id}).sort("time")
    res = {}

    for call in data:
        label = call.get('label')
        
        if label not in res:
            res[label] = list()

        res[label].append(
            {
                'operation':call.get('operation'),
                'time':call.get('time'),
                'message':call.get('message')
            }
        )
        
    return res
    # except:
    #     print("could not get data")
    #     return None

def setNewGroups():
    pass

def setSessionStateTransfers():
    pass




def connect(url='localhost',port=27017,database='mydb'):
    try:
        client = pymongo.MongoClient(url,port)
        return client[database]
    except:
        print("could not connect to database")
        return None
