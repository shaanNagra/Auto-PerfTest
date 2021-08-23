#!/usr/bin/env python


# ------------------------------------------
#
# ------------------------------------------
def clusterDifference(clstr1, clstr2):
    c1Len = len(clstr1)
    c2Len = len(clstr2)
    total = c1Len + c2Len
    Difference = 0
    found = []
    for i in range(c1Len):
        for j in range(c2Len):
            if clstr1[i]['operation'] == clstr2[j]['operation'] and \
               j not in found:

                found.append(j)
                break

    Difference += c1Len-len(found)
    Difference += c2Len-len(found)
    # total = all uniqe items plus items that occured in both list
    # l1=(a b c d) l2=(a d g) then total=length of set(a b c d g)
    return Difference/(total-len(found))*100.0


# ------------------------------------------
#
# ------------------------------------------
def clusterSimilarity(cluster1, cluster2):
    total = len(cluster1)+len(cluster2)
    # Difference = 0
    found = []
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            if cluster1[i]['operation'] == cluster2[j]['operation'] and \
               j not in found:
                found.append(j)
                break
    return (len(found)*2)/total*100.0


# ------------------------------------------
#
# ------------------------------------------
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
            operation = cluster[i]['operation']

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

    print(length)
    for k, v in counter.items():
        print(str(k) + '  =>   ' + str(v))

# l1 = ['m','b','d','i','i','i']
# l2 = ['c','i','a','d','d','t']

# print(clusterDifference(l1,l2))
# print(clusterSimilarity(l1,l2))
