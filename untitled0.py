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

df['Name EN'] = df['Name EN'].replace(np.nan, "MEP")
print(df.isnull().sum())

df.drop('Created', axis = 1, inplace=True)
df.drop('Updated', axis = 1, inplace=True)
df.drop('ID', axis = 1, inplace=True)
df.drop('Name FR', axis = 1, inplace=True)
df.drop('Name EN', axis = 1, inplace=True)
df.drop('Action', axis = 1, inplace=True)
df.drop('Intro FR', axis = 1, inplace=True)
df.drop('Intro EN', axis = 1, inplace=True)
df.drop('Families', axis = 1, inplace=True)
df.drop('Stats Hashtags', axis = 1, inplace=True)

print(df.columns.to_list())
#print(df.describe())


# plt.subplot(212)
# df["Stats Person"].value_counts(normalize=True).plot(kind='pie')

# plt.subplot(211)
# #df["Stats Question"].value_counts(normalize=True).plot(kind='pie')



G = nx.from_pandas_edgelist(df, source="Parents", target="Stats Person")
nx.draw(G, with_labels = True)
plt.figure(figsize = (200,200))





