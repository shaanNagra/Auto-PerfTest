#!/usr/bin/env python

# from bson import ObjectId

from db_functions import dbi_group as DBI
from . import comparison


# ------------------------------------------
#
# ------------------------------------------
def GroupSessionsViaVersion(webappID, version):
    sessions = {}
    innerGroups = {}
    selectedSessions = DBI.getClusteredSessions(webappID, version)

    print(selectedSessions)

    if len(selectedSessions) >= 1:
        for sID in selectedSessions:
            sessions[sID] = DBI.getSessionsForGrouping(sID)
            innerGroups[sID] = similarClustersInSession(sessions[sID])
    else:
        print("OUT: no results found")

    for i in innerGroups:
        print(i)
        print(innerGroups[i])

    for s1 in sessions:
        for s2 in sessions:
            if s1 is not s2:

                pass
            pass


# ------------------------------------------
#
# ------------------------------------------
def similarClustersInSession(session):
    e = 1
    results = set()
    # print(session)

    listOfKeys = list(session.keys())

    pointerDict = {}
    for i in session:
        pointerDict[i] = []

    # print(listOfKeys)
    for i in session:
        for j in session:

            # printOpsAcrossTwoSession(session[i],session[j])

            # NOT the same cluster
            if j is not i:

                # DIFF IS LESS THAN 40%
                diff = comparison.clusterDifference(session[i], session[j])
                if diff <= 40:
                    # SIM IS MORE THAN 80%
                    sim = comparison.clusterSimilarity(session[i], session[j])
                    if sim >= 80:
                        # ADD COMBO OF CLUSTERS
                        # print(str(listOfKeys[i])+" & "+str(listOfKeys[j])+": sim = "+str(sim)+" diff = "+str(diff))
                        # t = tuple(sorted([listOfKeys[i], listOfKeys[j]]))
                        # results.add(t)
                        if i not in pointerDict[j]:
                            pointerDict[j].append(i)

            # print(str(e)+"   diff = "+str(diff))
            # print("    sim = "+str(sim))
            e += 1
    # print("=====================")
    # print(pointerDict)

    pointerList = []
    for key in pointerDict:
        pointerDict[key].append(key)
        pointerList += [sorted(pointerDict[key])]

    # print("\n")
    # print(sorted(pointerList))
    # print('\n')
    res = []
    for i in pointerList:
        if i not in res:
            res.append(i)
    # print(res)

    matches = {}
    for i in range(len(res)):
        for j in range(len(res)):
            if len(res[i]) < len(res[j]):
                subset = True
                # print(str(i) + "   " + str(j))
                for ii in res[i]:
                    if ii not in res[j]:
                        subset = False

                if subset is True:
                    if j not in matches:
                        matches[j] = []
                    matches[j].extend(res[i])
                subset = True
    # print(matches)
    
    dontdrop = set()
    for i in matches:
        flag = True
        for j in res[i]:
            if j not in matches[i]:
                dontdrop.add(i)
                flag = False
        if flag is True:
            res.pop(i)

    # print(dontdrop)

    # for i in matches:
    #     if i not in dontdrop:
    #         res.pop(i)
    print(list(session.keys()))
    print(res)
    return results


# ------------------------------------------
#
# ------------------------------------------
def printOpsAcrossTwoSession(s1, s2):
    print('\n\n\n-------------------------')
    for op in s1:
        print(op['operation'])
    print('vs')
    for op in s2:
        print(op['operation'])
    print('-------------------------\n')


# ------------------------------------------
#
# ------------------------------------------
def test(id):
    session = DBI.getSessionsForGrouping(id)
    clusterList = []
    for i in session:
        # print(i)
        clusterList.append(session[i])
    comparison.clusterMulti(clusterList)


# NOTE: used to run as a isolated script during testing
# test('todoapp7488_1627653489854')
# GroupSessionsViaVersion(ObjectId("60f2bd7437deceb0424afa3b"),'1.0')

# session = DBI.getSessionsForGrouping('todoapp7488_1627653489854')
# # similarClustersInSession(session)
