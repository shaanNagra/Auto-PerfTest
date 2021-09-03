#!/usr/bin/env python

# from bson.objectid import ObjectId


from db_functions import dbi_cluster as DBI
from .cluster import cluster


# ------------------------------------------
#
# ------------------------------------------
def run(webappID):

    newSessions = DBI.getNewSessions(webappID)

    if len(newSessions) >= 1:
        print("OUT: session exist"+str(newSessions))
        x = 1
        for sID in newSessions:
            x += 1
            print(sID)
            results = cluster(
                DBI.getSessionCalls(sID), str(sID), x
                )

            if results is not None:
                DBI.setCallLabels(results)
                DBI.setSessionClusterd(sID)
                print("OUT: "+str(sID)+" clustered")
            else:
                print("OUT: "+str(sID)+" failed clustering")
                DBI.setSessionFailed(sID)

    else:
        print("OUT: no new sessions")

# # NOTE: used to run as a isolated script during testing
# ClusterNewSessions(ObjectId("60f2bd7437deceb0424afa3b"))
# print("done")
