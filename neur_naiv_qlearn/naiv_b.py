import pandas as pd
import tensorflow_datasets as tfds
from tqdm import tqdm

dataset = tfds.load('iris', shuffle_files=True)

###############

def convert_to_df(dataset):
    data = []
    for item in tqdm(dataset["train"]):
        features = item['features'].numpy()
        data.append({
            'sepal length': features[0], # Jellemző ami alapján prediktálni akarunk
            'label': item['label'].numpy() # Cimkék amelyet prediktálni szeretnénk
        })
    return pd.DataFrame(data)

df_dataset = convert_to_df(dataset)

################

df_dataset["sepal length"] = df_dataset["sepal length"].apply(lambda x: int(round(x)))

################

df_dataset.head()
df_dataset.describe()

################

def classes(value):
    if(value == 0):
        return "setosa"
    elif(value == 1):
        return "versicolour"
    else:
        return "virginica"

df_dataset["class"] = df_dataset["label"].apply(classes)

df_dataset.head()

################

num_split = int(len(df_dataset)*0.8)
df_train = df_dataset[:num_split]
df_test = df_dataset[num_split:]

print(df_train.shape)
print(df_test.shape)

################

def freq(cls):
    return {
         sl : [v for k,v in  zip(df_dataset["class"].values, df_dataset["sepal length"].values) if k == cls].count(sl) 
        / len([1 for k in df_dataset["class"].values if k == cls])
        for sl in set(df_dataset["sepal length"].values)
    }


dict_freqs_sepal_length = { 
    "setosa": freq("setosa"),
    "virginica": freq("virginica"), 
    "versicolour": freq("versicolour"),
    }


dict_freqs_sepal_length

################

dict_values = {item : 0.0 for item in list(set(df_dataset['sepal length'].values))}

for k,v in dict_values.items():
    dict_values [k] = len(list(filter(lambda x: x==k, df_dataset["sepal length"].values))) / len(df_dataset["sepal length"].values)

dict_values

#################

ratio = {item : { "setosa" : 0.0, "virginica" : 0.0, "versicolour" : 0.0}
         for item in list(set(df_dataset['sepal length'].values))}

for sl, value in ratio.items():
    for cls, ss in value.items():
        value[cls] = dict_freqs_sepal_length[cls][sl] / dict_values[sl];
ratio

#################

import numpy as np

pred_table = {}

for sl, v in ratio.items():
    pred_table[sl] = sorted(v.items(), key=lambda x: x[1], reverse=True)[0][0]
    
pred_table

#################

def prediction(val):
    return pred_table[val]
    
#################

from sklearn.metrics import accuracy_score

pred = []

for sl,cls in zip(df_train["sepal length"], df_train["class"]):
    pred.append(True if cls == prediction(sl) else False)

accuracy_score(df_train["label"].values, pred)

###################

pred = []

for sl,cls in zip(df_test["sepal length"], df_test["class"]):
    pred.append(True if cls == prediction(sl) else False)

accuracy_score(df_test["label"].values, pred)