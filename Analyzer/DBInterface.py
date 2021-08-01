import pymongo
import pandas as pd


def getNewSessionIDs(webappID):
    client = connect()
    try:
        res = []
        data = client.sessions.find({'webapp':webappID,'processed':'false'})
        for session in data:
            res.append(session.get('_id'))
        return res
    except:
        print("could not get data")
        return None



def getSingleSession(session_id=" "):
    
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


def sessionClustered(session_id):
    client = connect()
    try:
        update = { "$set": { "processed": "true" } }
        client.sessions.update_one({"_id":session_id},update)
        return True
    except:
        return False

def getSessionsForGrouping():
    pass

def setNewGroups():
    pass

def setSessionStateTransfers():
    pass

def setCallLabels(results):
    client = connect()
    try:
        bulk = client.calls.initialize_unordered_bulk_op()
        for i in results:
            bulk.find({'_id':i[0]}).update({'$set':{"label":str(i[4])}})
        bulk.execute()
        return True
    except:
        print("")
        return None
def connect(url='localhost',port=27017,database='mydb'):
    try:
        client = pymongo.MongoClient(url,port)
        return client[database]
    except:
        print("could not connect to database")
        return None
