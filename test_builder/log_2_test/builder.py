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
            self.nextGroup[index] = 1

    def printState(self, pointer):
        print("OUT: ============= STATE ==============")
        print("OUT: Type = ", self.type)
        print("OUT: Index = ", pointer, ", Calls = ", self.callsToString())
        print("OUT: NextStates = ", self.nextGroup)
        pass

    def callsToString(self):
        if self.calls is None:
            return "none"
        else:
            return str(self.calls)

    def getCalls(self):
        return self.calls

    def getDetails(self):
        return self.details

    def getNextGroup(self):
        return self.nextGroup


def testBuild(groups, sessionList):

    root = State("ROOT")
    endNode = State("ENDNODE")
    endNodeIndex = 0
    states = dict({endNodeIndex: endNode, 1: root})

    for session in sessionList:
        index = 0
        prevSate = root
        processed = False

        while processed is False:

            # RETURN INDEX AT END OF GROUP FOUND IN SESSION
            nextIndex = findState(groups, session, index)
            # FIND POINTER TO STATE IN LIST OF FOUND STATES
            stateKey = stateExist(states, session[index:nextIndex])

            # IF EXISTING STATE WAS NOT FOUND
            if stateKey is None:
                # CREATE NEW STATE APPEND TO LIST OF STATES
                stateKey = len(states)
                states[stateKey] = makeNewSate(session[index:nextIndex])

            # INCREMENT POINTER FROM PREVIOUS STATE TO THIS STATE
            prevSate.addToNextGroup(stateKey)
            # PEVIOUS STATE IS NOW THIS STATE
            prevSate = states[stateKey]
            index = nextIndex

            # IF ALL STATES HAVE BEEN FOUND IN SESSION
            if nextIndex >= len(session):
                processed = True
                # POINT LAST STATE TO END NODE
                prevSate.addToNextGroup(endNodeIndex)

    for state in states:
        states[state].printState(state)


def stateExist(states, list):
    for state in states:
        if states[state].isMatch(list) is True:
            return state
    return None


def makeNewSate(list):
    return State("NODE", list)


def findState(groups, session, initialIndex):

    occurance = {}
    foundState = []
    currentlyMatched = groups

    # FOR INDEX AFTER FOUND GROUP AND THE REST OF LIST
    for index in range(initialIndex, len(session)):

        # USED TO ID ITEMS THAT OCCUR MORE THAN ONCE IN LIST
        # operation = session[i]['operations']
        operation = str(session[index])
        if operation in occurance:
            occurance[operation] += 1
        else:
            occurance[operation] = 1
        operation += ' '+str(occurance[operation])

        stillMatched = stillMatchingGroups(currentlyMatched, operation)

        # IF NO GROUPGS MATCH ANYMORE
        if len(stillMatched) == 0:
            return initialIndex + 1
        else:
            foundState.append(operation)

        # IF ONE OF THE GROUPS IS 100% MATCH
        currentlyMatched = stillMatched
        for grp in currentlyMatched:
            foundState.sort()
            grp.sort()
            if foundState == grp:
                # RETURN INDEX OF END OF MATCHED
                return index + 1

    return initialIndex + 1


def stillMatchingGroups(currentlyMatched, operation):
    stillMatched = []
    for grp in range(len(currentlyMatched)):
        if operation in currentlyMatched[grp]:
            stillMatched.append(currentlyMatched[grp])
    return stillMatched


# NOTE: used to run as a isolated script during testing
group = [
    ['8 1', '8 2', '9 1', '5 1'],
    ['8 1', '8 2', '9 1', '5 1', '3 1'],
    ['2 1', '1 1']
    ]
sss = []
sss.append([8, 8, 9, 5, 3, 2, 1])
sss.append([8, 8, 9, 5, 3, 2, 1, 8, 9, 8, 5, 2, 1])
# print(sss)
testBuild(group, sss)
