#!/usr/bin/python

import json
import sys
import math
from parseFile import parseFile

subCalls = ['sub']
methodCalls = ['method']

file = parseFile(sys.argv)
if None == file:
    print("EXIT")
    exit()

data = json.load(file)

def duplicateCheck(stamp, tempStore):
    if (stamp+" 1") in tempStore:
        # print("\n\n\n\n\n FOUND")
        found = False
        index = 2
        while found == False:
            if ""+stamp+" "+str(index)+"" in tempStore:
                index += 1
            else:
                found = True
                # print(""+stamp+" "+str(index)+"")
                return ""+stamp+" "+str(index)+""
    else:
        return stamp+" 1"
allOperations = ["one,two,time"]
sessionIndex = 1
for sessions in data:
    tempStore = []
    operations = sessions['sessionOps']
    operations.sort(key=lambda s: s['timestamp'], reverse=False)

    for op in operations:
        if op['operation']['msg'] in subCalls:
            stamp = "sub "+op['operation']['name']
            stamp = duplicateCheck(stamp,tempStore) 

            for otherOp in operations:
                if(otherOp['operation']['msg'] == 'unsub' 
                and op['operation']['id'] == otherOp['operation']['id']):
                    otherOp['stamp'] = "unsub"+op['operation']['name']
        else:
            stamp = "method "+op['operation']['method']
            stamp = duplicateCheck(stamp,tempStore)
        op['stamp'] = stamp
        tempStore += [stamp]
        # print(stamp)

    for op in operations:
        op['diff']={}
        for otherOp in operations:
            diff = str(abs(otherOp['timestamp']-op['timestamp']))
            i = otherOp['stamp']
            # op['diff'][i] = {}
            op['diff'][i] = diff
            allOperations.append(""+str(sessionIndex)+","+op['stamp']+","+otherOp['stamp']+","+diff)


# for sessions in data:
#     operations = sessions['sessionOps']
#     operations.sort(key=lambda s: s['timestamp'], reverse=False)

#     for op in operations:
#         if op['operation']['msg'] in subC alls:
#             op['stamp'] = "sub "+op['operation']['name']
#             for otherOp in operations:
#                 if(otherOp['operation']['msg'] == 'unsub' 
#                 and op['operation']['id'] == otherOp['operation']['id']):
#                     otherOp['stamp'] = "unsub"+op['operation']['name']
#         else:
#             op['stamp'] = "sub "+op['operation']['method']      
        # op['stamp'] = op

    # for op in operations:
    #     for otherOp in operations:
    # print(sessions
for i in allOperations:
    print(i)
# def markUnsubs():

#     return


# print(v.keys())
# print(v['sessionOps'])

# print(type(data))
