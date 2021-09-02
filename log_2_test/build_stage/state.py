

# ------------------------------------------
#
# ------------------------------------------
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
