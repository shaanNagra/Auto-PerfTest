#!/usr/bin/env python

# INTERNAL IMPORTS
from script_builder.class_state import State

# ////////////////FILE DESCRIPTION/////////////////
# >> given a list of session and list of grouped
# function calls.
# >> it will use look through sessions for those
# groups to build sates and transtions to next group
# >> returns a markov chain once finished
# /////////////////////////////////////////////////


# ------------------------------------------
#
# ------------------------------------------
def test_build(groups, sessionList):

    root = State("ROOT")
    end_node = State("ENDNODE")
    end_node_index = 0
    states = dict({end_node_index: end_node, 1: root})

    for session in sessionList:
        index = 0
        prev_state = root
        processed = False

        while processed is False:

            # RETURN INDEX AT END OF GROUP FOUND IN SESSION
            next_index = find_state(groups, session, index)
            # FIND POINTER TO STATE IN LIST OF FOUND STATES
            state_key = state_exist(states, session[index:next_index])

            # IF EXISTING STATE WAS NOT FOUND
            if state_key is None:
                # CREATE NEW STATE APPEND TO LIST OF STATES
                state_key = len(states)
                states[state_key] = make_new_sate(session[index:next_index])

            # INCREMENT POINTER FROM PREVIOUS STATE TO THIS STATE
            prev_state.addToNextGroup(state_key)
            # PEVIOUS STATE IS NOW THIS STATE
            prev_state = states[state_key]
            index = next_index

            # IF ALL STATES HAVE BEEN FOUND IN SESSION
            if next_index >= len(session):
                processed = True
                # POINT LAST STATE TO END NODE
                prev_state.addToNextGroup(end_node_index)

    for state in states:
        states[state].printState(state)
    return states


# ------------------------------------------
# if list is found in the state dict()
# return the key of that state
# ------------------------------------------
def state_exist(states, list):
    for state in states:
        if states[state].isMatch(list) is True:
            return state
    return None


# ------------------------------------------
# returns state object with list
# ------------------------------------------
def make_new_sate(list):
    return State("NODE", list)


# ------------------------------------------
# looks through sessions for a sequence of
# functions that match shortest one in groups.
# returns index of next function after matched
# sequence if found
# else returns index of next from initial
# ------------------------------------------
def find_state(groups, session, initial_index):

    occurance = {}
    found_state = []
    currently_matched = groups

    # FOR INDEX AFTER FOUND GROUP AND THE REST OF LIST
    for index in range(initial_index, len(session)):

        # USED TO ID ITEMS THAT OCCUR MORE THAN ONCE IN LIST
        # operation = session[i]['operations']
        operation = str(session[index])
        if operation in occurance:
            occurance[operation] += 1
        else:
            occurance[operation] = 1
        operation += ' '+str(occurance[operation])

        still_matched = still_matching_groups(currently_matched, operation)

        # IF NO GROUPGS MATCH ANYMORE
        if len(still_matched) == 0:
            return initial_index + 1
        else:
            found_state.append(operation)

        # IF ONE OF THE GROUPS IS 100% MATCH
        currently_matched = still_matched
        for grp in currently_matched:
            found_state.sort()
            grp.sort()
            if found_state == grp:
                # RETURN INDEX OF END OF MATCHED
                return index + 1

    return initial_index + 1


# ------------------------------------------
# retruns list of groups that have the operation
# if they do
# they still match the sequence including that operation
# ------------------------------------------
def still_matching_groups(currently_matched, operation):
    still_matched = []
    for grp in range(len(currently_matched)):
        if operation in currently_matched[grp]:
            still_matched.append(currently_matched[grp])
    return still_matched


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
test_build(group, sss)
