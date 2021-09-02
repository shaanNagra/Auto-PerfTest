#!/usr/bin/env python

import re
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer, PowerTransformer, Normalizer, MaxAbsScaler

from db_functions import dbi_cluster as DBI


# ------------------------------------------
#
# ------------------------------------------
def sc_func(data, filePath=None, num=0):
    try:
        kmeans_kwargs = {
            "init": "random",
            "n_init": 10,
            "max_iter": 300,
            "random_state": 42,
        }
        kmax = len(data)
        bestK = 2
        hscore = 0
        s = []
        res = {}
        for k in range(2, kmax):
            kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans.fit(data)
            score = silhouette_score(data, kmeans.labels_)
            s.append(score)
            res[k] = score
            if score > hscore:
                hscore = score
                bestK = k

        selectedK = 0
        selectedKscore = 0

        for k in res:
            if res[k] >= (hscore * 0.9):
                selectedK = k
                selectedKscore = res[k]

        if filePath is not None:
            plt.close()
            plt.plot(range(2, kmax), s)
            plt.xticks(range(2, kmax))
            plt.xlabel("Number of Clusters")
            plt.ylabel("Silhouette Coefficient")
            plt.savefig("extra_data/sc-graphs/"+filePath+'__SC.svg')
            # plt.savefig(filePath+'_SilhouetteCoefficient.svg')
            plt.close()
        print("OUT: SELECTED K  score = "+str(selectedKscore)+"  K = "+str(selectedK))
        print("OUT: BEST  K     score = "+str(hscore)+"  K = "+str(bestK))
        return selectedK
    except:
        return None


# ------------------------------------------
#
# ------------------------------------------
def cluster(data, filePath, xn):
    try:
        print(data.head())
        random.seed(1297541)

        scaler = StandardScaler()
        scaledData = scaler.fit_transform(data.drop(['id', 'op'], axis=1))
        bestK = sc_func(scaledData, filePath=str(xn)+ "ScaledData"+ filePath)

        if bestK is None:
            return None

        # scaler = StandardScaler(with_std=False)
        # scaledData = scaler.fit_transform(data.drop(['id', 'op'], axis=1))
        # bestK = sc_func(scaledData, filePath=str(xn)+"ScaledDataSTDFalse"+filePath)

        # Ro = RobustScaler()
        # RobustData = Ro.fit_transform(data.drop(['id', 'op'], axis=1))
        # sc_func(RobustData, filePath=str(xn)+"Robust  "+filePath)

        # qt = QuantileTransformer(output_distribution='uniform')
        # QData = qt.fit_transform(data.drop(['id', 'op'], axis=1))
        # sc_func(QData, filePath=str(xn)+"QuantileUniform  "+filePath)

        # qnt = QuantileTransformer(output_distribution='normal')
        # QNData = qnt.fit_transform(data.drop(['id', 'op'], axis=1))
        # sc_func(QNData, filePath=str(xn)+"QuantileNormilize "+filePath)

        # mas = MaxAbsScaler()
        # masData = mas.fit_transform(data.drop(['id', 'op'], axis=1))
        # sc_func(masData, filePath=str(xn)+"MAS "+filePath)

        # nt = Normalizer
        # NData = nt.fit_transform(data.drop(['id', 'op'], axis=1))
        # sc_func(NData, filePath=str(xn)+"Normilizer  "+filePath)

        # pt = PowerTransformer(method='box-cox')
        # PData = pt.fit_transform(data.drop(['id', 'op'], axis=1))
        # sc_func(PData, filePath=str(xn)+"Power  "+filePath)

        # nonScaledData = data.drop(['id', 'op'], axis=1)
        # sc_func(nonScaledData, filePath=str(xn)+"nonScaled  "+filePath)

        clusterLables = KMeans(
                n_clusters=bestK,
                random_state=random.randint(0, 1000)
            ).fit_predict(scaledData)

        if filePath is not None:
            plt.scatter(data['x'], data['y'], c=clusterLables, s=2, alpha=0.5)
            plt.autoscale(enable=True, axis='y')
            plt.savefig("extra_data/cluster-graphs/"+str(xn)+filePath+'_Results.svg')
            plt.close()

        data['clusterGroup'] = clusterLables
        return data.to_records(index=False)
        # print(data)
    except:
        return None

# # NOTE: used to run as a isolated script during testing
# res = clusterCalls(DBInterface.getSingleSession('todoapp7488_1627653489854'))
# DBInterface.setCallLabels(res)
