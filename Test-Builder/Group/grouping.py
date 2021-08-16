#!/usr/bin/python

import DBInterface as DBI
import comparison
from bson import ObjectId

def GroupSessionsViaVersion(webappID,version):
    sessions = {}
    innerGroups = {}
    selectedSessions = DBI.getClusteredSessions(webappID,version)
    
    print(selectedSessions)
    
    if selectedSessions is not None:
        for sID in selectedSessions:
            sessions[sID] = DBI.getSessionsForGrouping(sID)
            innerGroups[sID] = similarClustersInSession(sessions[sID])
    
    for i in innerGroups:
        print(i)
        print(innerGroups[i])

    for s1 in sessions:
        for s2 in sessions:
            if s1 is not s2:
                
                pass
            pass

def similarClustersInSession(session):
    e = 1
    results = set() 
    # print(session)
    for i in session:
        for j in session:
            
            # printOpsAcrossTwoSession(session[i],session[j])
            
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
    return results

##
def mergeTuples(set):
    """e.g. if set has (a,b),(b,c),(a,c) => (a,b,c)"""
    for tpl1 in set:
        for tpl2 in set:
            if tpl1 is not tpl2:
                for x in tpl1:
                    if x in tpl2:
                        pass 

def printOpsAcrossTwoSession(s1,s2):
    print('\n\n\n-------------------------')
    for op in s1:
        print(op['operation'])
    print('vs')
    for op in s2:
        print(op['operation'])
    print('-------------------------\n')


def test(id):
    session = DBI.getSessionsForGrouping(id)
    clusterList = []
    for i in session:
        # print(i)
        clusterList.append(session[i])
    comparison.clusterMulti(clusterList)



# test('todoapp7488_1627653489854')
GroupSessionsViaVersion(ObjectId("60f2bd7437deceb0424afa3b"),'1.0')

session = DBI.getSessionsForGrouping('todoapp7488_1627653489854')
# similarClustersInSession(session)