#!/usr/bin/env python

# from bson import ObjectId

from db_functions import dbi_group as DBI
from . import comparison


# ------------------------------------------
#
# ------------------------------------------
def GroupSessionsViaVersion(webappID, version):
    listOfSessions = {}
    localGroups = {}

    selectedSessions = DBI.getClusteredSessions(webappID, version)
    # print(selectedSessions)

    if len(selectedSessions) >= 1:
        for sID in selectedSessions:
            listOfSessions[sID] = DBI.getSessionsForGrouping(sID)
            localGroups[sID] = findGrpsInSessions(listOfSessions[sID])
    else:
        print("OUT: no results found")
        return

    # for lg in localGroups:
        # print(lg)
        # print(localGroups[lg])

    listOfGroups = list()
    for sessions in listOfSessions:

        if len(listOfGroups) == 0:

            for groups in localGroups[sessions]:
                listOfGroups.append({sessions: groups})

        else:
            for groups in localGroups[sessions]:
                listOfGroups = findsimilar(
                    listOfGroups, groups, listOfSessions, sessions
                    )
                # print(groups)
                # print(sessions)
                # if findsimilar(
                #      listOfGroups, groups, listOfSessions, sessions
                #      ) is True:
                #     listOfGroups[sessions].append({sessions:groups})
                # else:
                #     pass
    print("FINALLRESULTS\n\n\n\n")
    print(listOfGroups)


# ------------------------------------------
#
# ------------------------------------------
def findsimilar(listOfGroups, grpToMatch, loS, g2mSID):
    print(listOfGroups)
    for i in range(len(listOfGroups)):
        if matchedAllInGroup(listOfGroups[i], grpToMatch, loS, g2mSID) is True:
            print(i)
            listOfGroups[i][g2mSID] = grpToMatch
            return listOfGroups
    listOfGroups.append({g2mSID: grpToMatch})
    return listOfGroups
    #    # print('----------------------------------------------')
    #    # print(grouping)
    #    # print("----------------------------------------------")
    #    # for singleGrp in grouping:
    #        # for grp in grpToMatch:
    #            # print(grp)
    #            # print(listOfSessions[grp])
    #            # return
    #            # break
    #            # print(grouping[singleGrp])
    #    # pass


# {tok1:[2,3],tok2:[1],tok3:[9]}
def matchedAllInGroup(grouping, grpToMatch, loS,  g2mSID):
    for singleGrp in grouping:
        if matchedInLocalGroups(
             grouping[singleGrp], grpToMatch, loS[singleGrp], loS[g2mSID]
             ) is False:
            return False
    return True


def matchedInLocalGroups(grp, grp2match, ops, ops2):
    for clstr in grp:
        for clstr2 in grp2match:
            # print(str(clstr)+"    "+str(clstr2))
            # print(ops[clstr])
            # print(ops2[clstr2])
            if clstrMatched(ops[clstr], ops2[clstr2]) is False:
                return False
    return True


# ------------------------------------------
#
# ------------------------------------------
def temp2():
    pass


# ------------------------------------------
#
# ------------------------------------------
def clstrMatched(clstr1, clstr2):

    # NOT the same cluster
    if clstr1 is not clstr2:

        # DIFF IS LESS THAN 40%
        diff = comparison.clusterDifference(clstr1, clstr2)
        if diff <= 40 :
            # SIM IS MORE THAN 80%
            sim = comparison.clusterSimilarity(clstr1, clstr2)
            if sim >= 80:
                return True
    return False


# ------------------------------------------
#
# ------------------------------------------
def convertPointersDictToList(pointerDict):
    groupsList = []
    for key in pointerDict:
        pointerDict[key].append(key)
        groupsList += [sorted(pointerDict[key])]
    return groupsList


# ------------------------------------------
#
# ------------------------------------------
def removeDuplicates(listwithDups):
    res = []
    for i in listwithDups:
        if i not in res:
            res.append(i)
    return res


# ------------------------------------------
#
# ------------------------------------------
def removeSetwithSubsets(groupsList):

    matches = {}

    for i in range(len(groupsList)):
        for j in range(len(groupsList)):

            if len(groupsList[i]) < len(groupsList[j]):
                subset = True
                # print(str(i) + "   " + str(j))

                for ii in groupsList[i]:
                    if ii not in groupsList[j]:
                        subset = False

                if subset is True:
                    if j not in matches:
                        matches[j] = []
                    matches[j].extend(groupsList[i])
                subset = True
    # print(matches)
    return dropSetswithSubset(groupsList, matches)


# ------------------------------------------
#
# ------------------------------------------
def dropSetswithSubset(groupsList, matches):
    dontdrop = set()
    for i in matches:
        flag = True
        for j in groupsList[i]:
            if j not in matches[i]:
                dontdrop.add(i)
                flag = False
        if flag is True:
            groupsList.pop(i)
    return(groupsList)


# ------------------------------------------
#
# ------------------------------------------
def findGrpsInSessions(sessions):

    # listOfKeys = list(sessions.keys())

    pointerDict = {}
    for i in sessions:
        pointerDict[i] = []

    # print(listOfKeys)
    for i in sessions:
        for j in sessions:
            if clstrMatched(sessions[i], sessions[j]) is True:
                if i not in pointerDict[j]:
                    pointerDict[j].append(i)

    groupsList = convertPointersDictToList(pointerDict)
    groupsList = removeDuplicates(groupsList)
    groupsList = removeSetwithSubsets(groupsList)

    print(list(sessions.keys()))
    print(groupsList)
    return groupsList


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
