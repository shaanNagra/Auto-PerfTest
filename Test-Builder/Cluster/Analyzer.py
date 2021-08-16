import DatabaseInterface as DBI
import callClusterer
from bson.objectid import ObjectId

def ClusterNewSessions(webappID):
    newSessions = DBI.getNewSessions(webappID)
    if newSessions is not None:
        print("session exist"+str(newSessions))
        for sID in newSessions:
            print(sID)
            results = callClusterer.cluster(DBI.getSessionCalls(sID),filePath=str(sID))
            if results is not None:
                DBI.setCallLabels(results)
                DBI.setSessionClusterd(sID)
            else:
                print(str(sID)+" failed clustering")
                DBI.setSessionFailed(sID)
    else:
        print("no new sessions")

       
ClusterNewSessions(ObjectId("60f2bd7437deceb0424afa3b"))
print("done")