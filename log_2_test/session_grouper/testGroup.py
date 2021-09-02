#!/usr/bin/env python

inputData = {
    0: ['a'],
    1: ['b', 'c', 'g'],
    2: ['g', 'h'],
    3: ['a', 'b', 'h'],
    4: ['c', 'd'],
    5: ['e'],
    6: ['c', 'd'],
    7: ['f'],
    8: ['g'],
    9: ['e'],
    10: ['e'],
}


inputData = {
    0: ['e'],
    1: ['d', 'b'],
    2: ['b'],
    3: ['e', 'b'],
    4: ['d'],
    5: ['a'],
    6: ['d'],
    7: ['c'],
    8: ['b'],
    9: ['a'],
    10: ['a'],
}


def test(inData):

    pointerDict = {}
    for i in inData:
        pointerDict[i] = []

    listOfKeys = list(inData.keys())
    for i in range(len(listOfKeys)):
        for j in range( len(listOfKeys)):

            if i is not j:
                for item in inData[listOfKeys[i]]:
                    if item in inData[listOfKeys[j]]:
                        if i not in pointerDict[j]:
                            pointerDict[j].append(i)

    print(inData)
    print(pointerDict)
    pointerList = []
    for key in pointerDict:
        pointerDict[key].append(key)
        pointerList += [sorted(pointerDict[key])]

    print("\n")
    print(sorted(pointerList))
    print('\n')
    res = []
    for i in pointerList:
        if i not in res:
            res.append(i) 
    print(res)

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
    print(matches)
    
    dontdrop = set()
    for i in matches:
        flag = True
        for j in res[i]:
            if j not in matches[i]:
                dontdrop.add(i)
                flag = False
        if flag is True:
            res.pop(i)

    print(dontdrop)
    # for i in matches:
    #     if i not in dontdrop:
    #         res.pop(i)
    
    print(res)
    # for i in pointerList:
    #     for j in pointerList:
    #         if len(pointerList(i)) == len(pointerList[j]) and i is not j:
    #             drop += j
    # outData = {}
    # n = 0
    # for key in reversed(list(pointerDict.keys())):
    #     pointers = pointerDict[key]
    #     print(key)
    #     nn = n
        
    #     createNew = True
    #     for i in outData:
    #         if key in outData[i]:
    #             createNew = False

    #     if createNew is True:
    #         outData[n] = [key]
    #         for p in reversed(pointers):
    #             pPointers = pointerDict[p]
    #             for pp in pointers:
    #                 if pp in pPointers:
    #                     outData[n].append(p)
    #                     outData[n].append(pp)
            
    #         for p in reversed(pointers):
    #             if p not in outData[n]:
    #                 n += 1
    #                 outData[n] = [key]
    #                 outData[n].append(p)
                    
        # createNew = True
        # for i in outData:
        #     if key in outData[i]:
        #         nn = i
        #         createNew = False

        # if createNew is True:
        #     outData[n] = [key]
        #     if len(pointers) >= 1:
        #         for p in reversed(pointers):
        #             # print(p)
        #             outData[n].append(p)
                    
        #         print(outData[n])
        #     n += 1
        # else:
        #     if len(pointers) >= 1:
        #         for p in reversed(pointers):
        #             outData[nn].append(p)
        # print(outData)
        # print("    "+str(nn))

    # print(outData)

test(inputData)
