#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:01:11 2022

@author: donatella
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx 

df = pd.read_csv('export_team.csv')
df1=df.copy()
print(df.info())


df.drop('Created', axis = 1, inplace=True)
df.drop('Updated', axis = 1, inplace=True)
df.drop('ID', axis = 1, inplace=True)


df.drop('Action', axis = 1, inplace=True)
df.drop('Intro FR', axis = 1, inplace=True)
df.drop('Intro EN', axis = 1, inplace=True)

df.drop('Stats Hashtags', axis = 1, inplace=True)

print(df.columns.to_list())
#print(df.describe())


# plt.subplot(212)
# df["Stats Person"].value_counts(normalize=True).plot(kind='pie')

# plt.subplot(211)
# #df["Stats Question"].value_counts(normalize=True).plot(kind='pie')

# G = nx.from_pandas_edgelist(df, source="Parents", target="Stats Person")
# nx.draw(G, with_labels = True)
# plt.figure(figsize = (200,200))

#LIEN ENTRE TAG ET SES PARENTS FAMILLES
#RECUPERER LE NOM
#TRI SUR DF PAR FAMILLE
#CLUSTER DE FAMILLE(5) VERS CLUSTER DE PARENTS
#PAS DE LIEN SI PAS DE LA MEME FAMILLE

#https://codesandbox.io  https://graphcommons.com https://graphcommons.github.io/api-v1/#get-graphs-id-paths


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing

labelEncod = LabelEncoder()
encode_families = labelEncod.fit_transform(df['Families'])
df['Code Fam']=encode_families.tolist()

encode_name = labelEncod.fit_transform(df['Name FR'])
df['Code Name']=encode_name.tolist()

print(df.columns.to_list())
df2=df.copy()


df, true_labels = make_blobs(n_samples=500, centers=10, random_state=6)
points = pd.DataFrame(df, columns=["Families", "Name FR"])
points.plot.scatter("Families", "Name FR")

kmeans = KMeans(n_clusters=10).fit(points)
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=["Families", "Name Fr"])
cluster_centers
points.plot.scatter("Families", "Name FR", c=kmeans.labels_,figsize=(9,8), colormap="Dark2", title="Clustering par famille", xlabel='Famille',
                ylabel='Name')















