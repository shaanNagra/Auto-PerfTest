import database
import pymongo
import bson.json_util as bson


database = database.getConnection()
if database == None:
    print("cant connect to database")
    exit()

data = database.sessions.aggregate([{
    '$lookup': {
        'from':"sessionsOps",
        'localField':'_id',
        'foreignField':'session_id',
        'as':'operation'
        }
    }])


for session in data:
    
    results = []
    subs = {}
    prev = None
    minClusterCount = 0

    allOps = session.get('operation')
    
    for log in allOps:
        print(log)
        operation = log.get('operation')

        if prev is not None:
            if (log['timestamp'] - prev['timestamp']) >= 1000:
                minClusterCount += 1

        prev = log

        if operation['msg'] == 'sub':
            
            subs[operation['id']] = operation['name']
            results.append("'sub "+operation['name'] +"',"+str(log['timestamp']))

        elif operation['msg'] == 'unsub':
            
            #need to do some checking(if key exist)
            results.append("'usub "+subs.get(operation['id'])+"',"+str(log['timestamp']))
        

        elif operation['msg'] == 'method':

            results.append(" 'method "+operation['method']+"',"+str(log['timestamp']))

        else:
            pass