
import matplotlib.pyplot as plt
from kneed import KneeLocator
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import csv
from parseFile import parseFile
import sys

file = parseFile(sys.argv)
if None == file:
    print("EXIT")
    exit()

# with open(sys.argv[1],'r') as dest_f:
#     data_iter = csv.DictReader(dest_f,
#                            delimiter = ',',
#                            quotechar = '"')
#     data = [data for data in data_iter]
# data_array = np.asarray(data, dtype = None)
# print(data_array[0,0:])

data = pd.read_csv(sys.argv[1])
# print(data.head())
X = data.drop(['index','name'],axis=1)
XX = data.drop('y',axis=1)
XY = data.drop('x',axis=1)
print(X)
res = KMeans(n_clusters=50, random_state=89).fit_predict(X)

plt.scatter(XX, XY, c=res)
plt.show()