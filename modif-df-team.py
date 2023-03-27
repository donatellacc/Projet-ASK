#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:03:36 2023

@author: donatella
"""
# Créer une liste pour stocker les lignes uniques
json_data =[]

import json
unique_data = []

# Itérer sur chaque ligne du JSON et ajouter les lignes uniques à la liste
for data in json_data:
    if data not in unique_data:
        unique_data.append(data)

# Créer un nouveau JSON à partir des lignes uniques
with open('nouveau_json.json', 'w') as f:
    json.dump(unique_data, f)

print("Le nouveau JSON a été enregistré avec succès.")

with open("nouveau_json.json", "r") as f:
    json_data = f.read()

# Supprimer tous les espaces du JSON
json_data = json_data.replace(" ", "")

# Charger le JSON dans un dictionnaire Python
data = json.loads(json_data)

# Enregistrer le dictionnaire dans un nouveau fichier JSON sans espaces
with open("nouveau_exemple.json", "w") as f:
    json.dump(data, f)