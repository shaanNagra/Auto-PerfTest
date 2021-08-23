#! /usr/bin/env python

import pymongo


class state:
    def __init__(self, root):
        self.isRoot = root
        self.nextGroup = {}
        self.calls = []
        pass

    def isMatch(self, list):
        list.sort()
        self.calls.sort()
        if self.calls == list:
            return True
        return False


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

def getCalls(sid):
    pass

def connect(url=Database.url, port=Database.port, database=Database.name):
    try:
        client = pymongo.MongoClient(url, port)
        return client[database]
    except pymongo.errors.PyMongoError as e:
        print("ERR: failed to connect")
        print("ERR: " + e)


def build(groups,sessionIDs):
    root = state(True)
    states = dict({0: root})

    for sid in sessionIDs:
        session = getCalls(sid)
        processed = False
        index = 0
        while processed is False:
            findState(groups,session,index)


def testBuild(groups, sss):
    root = state(True)
    states = dict({0: root})

    processed = False
    index = 0
    while processed is False:
        index = findState(groups, sss, index)
        print(index)
        if index == len(sss):
            processed = True
        
    pass


def findState(groups, session, index):
    offset = index
    occurance = {}
    foundState = []
    matchedGroups = groups
    print("===============")
    for i in range(index, len(session)):
        print(session[i])
    print("^^^^^^^^^^^^^^^")
    for i in range(index, len(session)):
        
        # operation = session[i]['operations']
        operation = str(session[i])
        if operation in occurance:
            occurance[operation] += 1
        else:
            occurance[operation] = 1
        operation += ' '+str(occurance[operation])
        # print(operation)

        newMatchedGroups = []
        for grp in range(len(matchedGroups)):
            if operation in matchedGroups[grp]:
                newMatchedGroups.append(matchedGroups[grp])
        if len(newMatchedGroups) == 0:
            print("AAAAAA")
            print(foundState)
            return index + 1
        else:
            offset += 1
            foundState.append(operation)

        matchedGroups = newMatchedGroups
        for grp in matchedGroups:
            foundState.sort()
            grp.sort()
            if foundState == grp:
                print(foundState)
                return offset
    print(foundState)
    return offset

group = [['8 1', '8 2', '9 1', '5 1'], ['8 1', '8 2', '9 1', '5 1', '3 1'], ['2 1', '1 1']]
sss = [8, 8, 9, 5, 3, 2, 1]

testBuild(group, sss)
