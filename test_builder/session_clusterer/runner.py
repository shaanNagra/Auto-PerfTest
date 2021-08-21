#!/usr/bin/env python

from bson.objectid import ObjectId

from test_builder.db_functions import dbi_cluster as DBI
from .cluster import cluster

# ------------------------------------------
#
# ------------------------------------------
def ClusterNewSessions(webappID):

    newSessions = DBI.getNewSessions(webappID)
    
    if newSessions is not None:
        print("session exist"+str(newSessions))

        for sID in newSessions:
            print(sID)
            results = cluster(DBI.getSessionCalls(sID),filePath=str(sID))

            if results is not None:
                DBI.setCallLabels(results)
                DBI.setSessionClusterd(sID)

            else:
                print(str(sID)+" failed clustering")
                DBI.setSessionFailed(sID)
    else:
        print("no new sessions")

# # NOTE: used to run as a isolated script during testing       
# ClusterNewSessions(ObjectId("60f2bd7437deceb0424afa3b"))
# print("done")