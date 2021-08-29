#! /usr/bin/env python


class State:
    def __init__(self, Type, calls=[], details=[]):
        self.type = Type
        self.nextGroup = {}
        self.calls = calls
        self.details = details
        pass

    def isMatch(self, list):
        list.sort()
        self.calls.sort()
        if self.calls == list:
            return True
        return False

    def addToNextGroup(self, index):
        print("index = "+str(index))
        if index in self.nextGroup:
            self.nextGroup[index] += 1
        else:
            # print("new group")
            self.nextGroup[index] = 1

    def printState(self):
        pass

    def callsToString(self):
        if self.calls is None:
            return "none"
        else:
            return str(self.calls)


# def build(groups,sessionIDs):
#     root = State(True)
#     states = dict({0: root})

#     for sid in sessionIDs:
#         session = getCalls(sid)
#         processed = False
#         index = 0
#         while processed is False:
#             findState(groups, session, index)


def testBuild(groups, ssss):
    root = State("ROOT")
    endNode = State("ENDNODE")
    endNodeIndex = 0
    states = dict({endNodeIndex: endNode, 1: root})

    for sss in ssss:
        # print(sss)
        t = 1
        index = 0
        prevSate = root
        processed = False
        while processed is False:
            
            nextIndex = findState(groups, sss, index)
            print("SS")
            print(sss[index:nextIndex])
            print(nextIndex)
            print()
            stateKey = stateExist(states, sss[index:nextIndex])
            # if is match with existing state
            # print(stateKey)
            if stateKey is not None:
                #    prev state  add points to this sate
                prevSate.addToNextGroup(stateKey)
                prevSate = states[stateKey]
            else:
                #    create new state
                #    prev state add points to this sate
                newSate = makeNewSate(sss[index:nextIndex])
                stateKey = len(states)
                states[stateKey] = newSate
                prevSate.addToNextGroup(stateKey)
                prevSate = newSate
            # prev state is now this state 

            # print(nextIndex)

            if nextIndex >= len(sss):
                processed = True
                prevSate.addToNextGroup(endNodeIndex)
            index = nextIndex
        
    for state in states:
        print("STATE:")
        print("TYPE : " + states[state].type)
        print(str(state)+"   CALLS:"+states[state].callsToString())
        print("JUMPS TOO:")
        print(states[state].nextGroup)
        print("-----------------------")


def stateExist(states, list):
    for state in states:
        if states[state].isMatch(list) is True:
            return state
    return None


def makeNewSate(list):
    return State("NODE", list)


def findState(groups, session, index):
    offset = index
    occurance = {}
    foundState = []
    matchedGroups = groups
    # print("===============")
    # for i in range(index, len(session)):
        # print(session[i])
    # print("^^^^^^^^^^^^^^^")
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
            # print("AAAAAA")
            # print(foundState)
            return index + 1
        else:
            offset += 1
            foundState.append(operation)

        matchedGroups = newMatchedGroups
        for grp in matchedGroups:
            foundState.sort()
            grp.sort()
            if foundState == grp:
                # print("if full match")
                # print(foundState)
                return offset

    # print("foundstate")
    # print(foundState)
    return offset


group = [['8 1', '8 2', '9 1', '5 1'], ['8 1', '8 2', '9 1', '5 1', '3 1'], ['2 1', '1 1']]
sss = []
sss.append([8, 8, 9, 5, 3, 2, 1])
sss.append([8, 8, 9, 5, 3, 2, 1, 8, 9, 8, 5, 2, 1])
# print(sss)
testBuild(group, sss)
