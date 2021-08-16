#!/usr/bin/python
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
    results = set() 
    session = DBI.getSessionsForGrouping(id)
    # print(session)

    for i in session:
                
        for j in session:
            
            # print('\n\n\n-------------------------')
            # for op in session[i]:
            #     print(op['operation'])
            # print('vs')
            # for op in session[j]:
            #     print(op['operation'])
            # print('-------------------------\n')
            
            #NOT the same cluster
            if j is not i:
                #DIFF IS LESS THAN 40%
                diff = comparison.clusterDifference(session[i],session[j])
                if diff <= 40:
                    #SIM IS MORE THAN 80%
                    sim = comparison.clusterSimilarity(session[i],session[j])
                    if sim >= 80:
                        #ADD COMBO OF CLUSTERS
                        t = tuple(sorted([i,j]))
                        results.add(t)

            # print(str(e)+"   diff = "+str(diff))
            # print("    sim = "+str(sim))
            e +=1
        
        # print("\n\n====================\n\n")
    print(results)
# GroupSessions(ObjectId("60f2bd7437deceb0424afa3b"),'1.0')
groupSingleSession('todoapp7488_1627653489854')

def test(id):
    session = DBI.getSessionsForGrouping(id)
    clusterList = []
    for i in session:
        # print(i)
        clusterList.append(session[i])
    comparison.clusterMulti(clusterList)

# test('todoapp7488_1627653489854')