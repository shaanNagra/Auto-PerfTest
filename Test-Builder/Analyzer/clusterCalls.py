#!/usr/bin/python

import numpy as np
import pandas as pd
import DBInterface
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def clusterCalls(data):
    try:
        print(data.head())
        random.seed(1297541)

        scaler = StandardScaler()
        scaledData = scaler.fit_transform(data.drop(['id','op'],axis=1))
        
        kmeans_kwargs = {
            "init":"random",
            "n_init":10,
            "max_iter":300,
            "random_state":42,
        }
        kmax = len(data)
        bestK = 2
        hscore = 0
        s =[]
        for k in range(2,kmax):
            kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans.fit(scaledData)
            score = silhouette_score(scaledData, kmeans.labels_)
            s.append(score)
            if score > hscore:
                hscore = score
                bestK = k
        
        plt.plot(range(2, kmax), s)
        plt.xticks(range(2, kmax))
        plt.xlabel("Number of Clusters")
        plt.ylabel("Silhouette Coefficient")
        plt.savefig('fo1o.png')

        print(str(hscore)+"   "+str(bestK))

        clusterLables = KMeans(n_clusters=bestK+2, random_state=random.randint(0,1000)).fit_predict(scaledData)
        
        plt.close()
        plt.scatter(data['x'], data['y'], c=clusterLables, s=2,alpha=0.5)
        plt.autoscale(enable=True, axis='y')
        plt.savefig('foo.svg')
        
        data['clusterGroup'] = clusterLables
        return data.to_records(index=False)
        # print(data)
    except:
        return None

res = clusterCalls(DBInterface.getSingleSession('todoapp7488_1627653489854'))
DBInterface.setCallLabels(res)