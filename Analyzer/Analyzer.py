import DBconn
import clusterCalls
def ClusterNewSessions(webappID):
    newSessions = DBconn.getUnprocessedSessions(webappID)
    if newSessions is not None:
        for sessionID in newSessions:
            results = clusterCalls.clusterCalls(DBconn.getSession(sessionID))
            if results is not None:
                # DBconn.setResults(results,sessionID)
