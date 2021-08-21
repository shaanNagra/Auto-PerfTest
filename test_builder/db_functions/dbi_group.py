#!/usr/bin/env python

import pymongo

from . import db_conn
from .db_constants import SessionCol, CallCol

# ////////////////FILE DESCRIPTION/////////////////
# functions that interact with the mongodb database
#  for use in the grouping functionallity
#  (is the interface for grouping module)
# /////////////////////////////////////////////////


# ------------------------------------------
#
# ------------------------------------------
def getCallsList(session_id=""):
    """ 
    """
  
    client = db_conn.connect()
    try:
        data = client.calls.find({
            CallCol.session: session_id
            }).sort(CallCol.time)
        res = []

        for call in data:
            res += [{
                call.get(CallCol.id),
                call.get(CallCol.operation),
                call.get(CallCol.time),
                call.get(CallCol.time),
                call.get(CallCol.label)
                }]

        print('OUT: ')
        return res
    except :
        print("ERR: could not get data")
        return None

#------------------------------------------
# 
#------------------------------------------
def getClusteredSessions(webappID,version):
    """
    def: get all IDs of sessions of given webapp logged at given version

    returns: List [session._id]
    """
    
    client = db_conn.connect()
    try:
        res = []
        data = client.sessions.find({
            SessionCol.application:webappID,
            SessionCol.processed:True,
            SessionCol.appVersion:version
            })
        for session in data:
            if session.get('processed') == True:
                res.append(session.get('_id'))
        return res
    except:
        print("could not get data")
        return None



#------------------------------------------
# 
#------------------------------------------
def getSessionsForGrouping(session_id):
    """
    def: get all calls for session grouped by cluster label
    
    returns: dict[    key:label   value:List[   dict{ operation, time, message} ]]
    """
    
    client = db_conn.connect()
    try:
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

        print("OUT: results returned")    
        return res

    except pymongo.errors.PyMongoError as e:
        print("ERR: could not get data")
        print("ERR: "+e)
        return None



#------------------------------------------
# 
#------------------------------------------
def setNewGroups():
    pass



#------------------------------------------
# 
#------------------------------------------
def setSessionStateTransfers():
    pass
