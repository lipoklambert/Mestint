import numpy as np
import matplotlib.pyplot as plt

def viz(test_img, test_label, size=(28, 28)):
    plt.imshow(test_img.reshape(size[0],size[1]), cmap='Greys')
    plt.axis('off')
    plt.title(str(test_label))
    plt.show()
    
#############

choice = np.random.choice(np.arange(len(df_train)))
viz(df_train["image"].values[choice], df_train["label"].values[choice])

#############

train_img = df_train["image"].values[0]
train_test_split = int(train_img.shape[0])
X_train = df_train["image"].values[:train_test_split]
y_train = df_train["label"].values[:train_test_split]

X_test = df_test["image"].values[train_test_split:]
y_test = df_test["label"].values[train_test_split:]

X_train.shape, y_train.shape, X_test.shape, y_test.shape

#############

def one_hot_encode(x: np.ndarray, num_classes: int) -> np.ndarray:
    return np.eye(num_classes)[x]
    
y_train = one_hot_encode(y_train, 10)
y_test = one_hot_encode(y_test, 10)

X_train.shape, y_train.shape, X_test.shape, y_test.shape

#############

import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Input((X_train.shape[0])),
    tf.keras.layers.Dense(64, activation='linear'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer="adam", 
    loss="categorical_crossentropy", 
    metrics=["accuracy"]
)

############

model.fit(X_train, y_train, epochs=4, batch_size=16)

model.evaluate(X_test, y_test)