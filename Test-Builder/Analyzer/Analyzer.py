import DBInterface
import clusterCalls
def ClusterNewSessions(webappID):
    newSessions = DBInterface.getNewSessionIDs(webappID)
    if newSessions is not None:
        for sessionID in newSessions:
            results = clusterCalls.clusterCalls(DBInterface.getSingleSession(sessionID))
            if results is not None:
                # DBconn.setResults(results,sessionID)
                pass
