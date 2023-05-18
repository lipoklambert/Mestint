import pandas as pd
import tensorflow_datasets as tfds
from tqdm import tqdm

####################

dataset_train = tfds.load('fashion_mnist', split='train', shuffle_files=True)
dataset_test = tfds.load('fashion_mnist', split='test', shuffle_files=True)

#####################

def convert_to_df(dataset):
    data = [{ 'image': item['image'].numpy(), 'label': item['label'].numpy() } for item in tqdm(dataset)]
    return pd.DataFrame(data)

df_train = convert_to_df(dataset_train)
df_test = convert_to_df(dataset_test)

#####################

df_test["image"] = df_test["image"].apply(lambda x: x.flatten())
df_train["image"] = df_train["image"].apply(lambda x: x.flatten())
df_train.head()

#####################

import numpy as np
import matplotlib.pyplot as plt

def viz(test_img, test_label, size=(28, 28)):
    plt.imshow(test_img.reshape(size[0], size[1]), cmap="Greys")
    plt.axis('off')
    plt.title(str(test_label))
    plt.show()
    
#####################

choice = np.random.choice(np.arange(len(df_train)))
viz(df_train["image"].values[choice], df_train["label"].values[choice])

#####################

def normalize(x):
  return (x - np.min(x)) / (np.max(x) - np.min(x))
  
#####################

train_test_split_no =  int(df_train.shape[0]*0.8)
train_test_split_no

#####################

X_train = df_train[:train_test_split_no]
y_train = df_train["label"].values[:train_test_split_no].astype(int)


X_test = df_test[train_test_split_no:]
y_test = df_test["label"].values[train_test_split_no:].astype(int)

#####################

X_train.shape, y_train.shape, X_test.shape, y_test.shape

#####################

def one_hot_encode(x, num_labels):
  return np.eye(num_labels)[x]
  
#####################

y_train = one_hot_encode(y_train, 10)
y_test = one_hot_encode(y_test, 10)

X_train.shape, y_train.shape, X_test.shape, y_test.shape

######################

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Input(([X_train.shape[1]])),
    tf.keras.layers.Dense(64,activation="linear"),
    tf.keras.layers.Dense(64,activation="relu"),
    tf.keras.layers.Dense(10,activation="softmax")
])

########################

model.summary()

########################

model.compile(
    optimizer="adam", 
    loss="categorical_crossentropy", 
    metrics=["accuracy"]
)

#########################

model.fit(X_train, y_train, epochs=4, batch_size=16)
model.evaluate(X_test,y_test)