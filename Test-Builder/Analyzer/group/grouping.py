from sklearn import preprocessing
import DBInterface as DBI
import comparison
from bson.objectid import ObjectId

def GroupSessions(webappID,version):
    sessions = {}
    selectedSessions = DBI.getClusteredSessions(webappID,version)
    print(selectedSessions)
    if selectedSessions is not None:
        for sID in selectedSessions:
            sessions[sID] = DBI.getSessionsForGrouping(sID)
            
    print(sessions)

def groupSingleSession(id):
    e = 1
    session = DBI.getSessionsForGrouping(id)
    for i in session:
                
        for j in session:
            print('\n\n\n-------------------------')
            for op in session[i]:
                print(op['operation'])
            print('vs')
            for op in session[j]:
                print(op['operation'])

            print('-------------------------\n')
            diff = comparison.clusterDifference(session[i],session[j])
            sim = comparison.clusterSimilarity(session[i],session[j])
            print(str(e)+"   diff = "+str(diff))
            print("    sim = "+str(sim))
            e +=1
        
        print("\n\n====================\n\n")
# GroupSessions(ObjectId("60f2bd7437deceb0424afa3b"),'1.0')
groupSingleSession('todoapp7488_1627653489854')