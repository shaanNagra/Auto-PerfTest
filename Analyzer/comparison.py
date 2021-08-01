
def clusterDifference(cluster1,cluster2):
    c1Len = len(cluster1)
    c2Len = len(cluster2)
    total = c1Len + c2Len
    Difference = 0
    found = []
    for i in range(c1Len):
        for j in range(c2Len):
            if cluster1[i] == cluster2[j] and j not in found:
                found.append(j)
                break

        
    Difference += c1Len-len(found)
    Difference += c2Len-len(found)
    # total = all uniqe items plus items that occured in both list
    # l1 = (a b c d)   l2 = (a d g)    then  total = length of set (a b c d g)  
    return Difference/(total-len(found))*100.0

def clusterSimilarity(cluster1,cluster2):
    total = len(cluster1)+len(cluster2)
    Difference = 0
    found = []
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            if cluster1[i] == cluster2[j] and j not in found:
                found.append(j)
                break
    return (len(found)*2)/total*100.0


# def 




l1 = ['m','b','d','i','i','i']
l2 = ['c','i','i','d']

print(clusterDifference(l1,l2))
print(clusterSimilarity(l1,l2))