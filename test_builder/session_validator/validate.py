#! /usr/bin/env python

import pymongo


class Database:
    url = 'localhost'
    port = 27017
    name = 'K-Base'


class CallCol:
    name = 'calls'
    session = 'session_id'
    id = '_id'
    operation = 'operation'
    message = 'message'
    time = 'time'
    label = 'label'


def validate(listOfGroups):
    validGroups = []
    for grouping in listOfGroups:
        operations = []
        for session in grouping:
            for cluster in grouping[session]:
                operations.append(getOperations(session, cluster))
        if len(operations) >= 2:
            validGroups.append(clusterMulti(operations))
    validGroups = removeDuplicates(validGroups)
    return validGroups


def removeDuplicates(listwithDups):
    res = []
    for i in listwithDups:
        if i not in res:
            res.append(i)
    return res


def getOperations(session, label):

    client = connect()
    res = []

    data = client.calls.find({
        CallCol.session: session,
        CallCol.label: label
    })
    for call in data:
        res.append(call.get('operation'))
    return res


def connect(url=Database.url, port=Database.port, database=Database.name):
    try:
        client = pymongo.MongoClient(url, port)
        return client[database]
    except pymongo.errors.PyMongoError as e:
        print("ERR: failed to connect")
        print("ERR: " + e)


def clusterMulti(clusterList):
    length = 0
    counter = {}
    for cluster in clusterList:
        length += 1
        foundInCluster = {}
        # l = 0
        for i in range(len(cluster)):
            # l +=1
            # print(l)
            operation = cluster[i]#['operation']

            if operation in foundInCluster:
                foundInCluster[operation] += 1
            else:
                foundInCluster[operation] = 1

            operation += ' '+str(foundInCluster[operation])
            # print(operation)
            if operation in counter:
                counter[operation] += 1
            else:
                counter[operation] = 1

    res = []
    for key in counter:
        if counter[key] == length:
            res.append(key)
    return res
    # print("length "+str(length))
    # for k, v in counter.items():
    #     print(str(k) + '  =>   ' + str(v))
