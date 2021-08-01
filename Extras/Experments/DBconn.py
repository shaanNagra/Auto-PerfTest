import pymongo
import string
import bson.json_util as j
import json

header = '''
index,name,x,y
''' 

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['mydb']
data = database.sessions.aggregate([{
    '$lookup': {
        'from':"calls",
        'localField':'_id',
        'foreignField':'session_id',
        'as':'operation'
        }
    }])
bigFile = open('aadfsf.csv','w')
bigFile.write(header)
for session in data:
    file = open(session['_id']+".csv",'w')
    index = 0
    
    results = []
    subs = {}
    sessionOp = session.get('operation')
    for log in sessionOp:
        index += 1
        # log = json.loads(log)
        print(log)
        op = log.get('operation')

        if op['msg'] == 'sub':
            
            subs[op['id']] = op['name']
            results.append(str(index)+",'sub "+op['name'] +"',"+str(log['timestamp'])+","+str(log['timestamp']))

        elif op['msg'] == 'unsub':
            
            #need to do some checking(if key exist)
            results.append(str(index)+",'usub "+subs.get(op['id'])+"',"+str(log['timestamp'])+","+str(log['timestamp']))
        

        elif op['msg'] == 'method':
            results.append(str(index)+", 'method "+op['method']+"',"+str(log['timestamp'])+","+str(log['timestamp']))

        else:
            pass

    file.write(header)
    for stuff in results:
        bigFile.write(stuff+" \n")
        file.write(stuff+" \n")
    file.close()
bigFile.close()

def op2String(op):
     return

def getUnproccessedSessions():

    pass


def getSession(session_id=" "):
    
    client = connect()
    data = database.calls.find({'session_id':session_id}).sort("time")

    for session in data:
        file = open(session['_id']+".csv",'w')
        index = 0
        
        results = []
        subs = {}
        sessionOp = session.get('operation')
        for log in sessionOp:
            index += 1
            # log = json.loads(log)
            print(log)
            op = log.get('operation')

            if op['msg'] == 'sub':
                
                subs[op['id']] = op['name']
                results.append(str(index)+",'sub "+op['name'] +"',"+str(log['timestamp'])+","+str(log['timestamp']))

            elif op['msg'] == 'unsub':
                
                #need to do some checking(if key exist)
                results.append(str(index)+",'usub "+subs.get(op['id'])+"',"+str(log['timestamp'])+","+str(log['timestamp']))
            

            elif op['msg'] == 'method':
                results.append(str(index)+", 'method "+op['method']+"',"+str(log['timestamp'])+","+str(log['timestamp']))

            else:
                pass

    file.write(header)
    for stuff in results:
        bigFile.write(stuff+" \n")
        file.write(stuff+" \n")
    file.close()
    bigFile.close()
    
    return



def connect(url='localhost',port=27017,database='mydb'):
    try:
        client = pymongo.MongoClient(url,port)
        return client[database]
    except:
        return None