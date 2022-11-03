#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:01:11 2022

@author: donatella
"""

import pandas as pd

df = pd.read_csv('export_team.csv')
print(df.info())

print(df.isnull().sum())
print(df.describe())