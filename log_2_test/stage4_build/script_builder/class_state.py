#!/usr/bin/env python


# ////////////////FILE DESCRIPTION/////////////////
# connects to databse, returns object id of webapp
# /////////////////////////////////////////////////


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

    def is_Match(self, list):
        list.sort()
        self.calls.sort()
        if self.calls == list:
            return True
        return False

    def add_to_next_group(self, index):
        print("index = "+str(index))
        if index in self.nextGroup:
            self.nextGroup[index] += 1
        else:
            self.nextGroup[index] = 1

    def print_state(self, pointer):
        print("OUT: ============= STATE ==============")
        print("OUT: Type = ", self.type)
        print("OUT: Index = ", pointer, ", Calls = ", self.callsToString())
        print("OUT: NextStates = ", self.nextGroup)
        pass

    def calls_to_string(self):
        if self.calls is None:
            return "none"
        else:
            return str(self.calls)

    def get_calls(self):
        return self.calls

    def get_details(self):
        return self.details

    def get_next_group(self):
        return self.nextGroup
