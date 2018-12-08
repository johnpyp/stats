import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras import preprocessing
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM, Reshape
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
import string
import random

import numpy as np
import pandas
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(10)
data = pandas.read_csv('colors.csv')
print(data.head())

names = data["name"]
h = sorted(names.str.len().as_matrix())

maxlen = 25
t = Tokenizer(char_level=True)
t.fit_on_texts(names)
tokenized = t.texts_to_sequences(names)
padded_names = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)
one_hot_names = np_utils.to_categorical(padded_names)
num_classes = one_hot_names.shape[-1]
print(num_classes)


def norm(value):
    return value / 255.0


normalized_values = np.column_stack(
    [norm(data["red"]), norm(data["green"]), norm(data["blue"])])
model = Sequential()
model.add(LSTM(256, return_sequences=True, input_shape=(maxlen, num_classes)))
model.add(LSTM(128))
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.compile(optimizer='adam', loss='mse', metrics=['acc'])
model.summary()
save_callback = ModelCheckpoint('model.h5', monitor='val_loss', verbose=0,
                                save_best_only=False, save_weights_only=False, mode='auto', period=1)
# model.load_weights('model.h5')

history = model.fit(one_hot_names, normalized_values,
                    epochs=40,
                    batch_size=32,
                    validation_split=0.1,
                    callbacks=[save_callback])

# plot a color image


def plot_rgb(rgb, index, rows):
    data = [[rgb]]
    temp = plt.subplot(1, rows, index)
    temp.imshow(data, interpolation='nearest')


def scale(n):
    return int(n * 255)


def predict(names):
    fig = plt.figure()

    for i, name in enumerate(names, start=1):

        name = name.lower()
        tokenized = t.texts_to_sequences([name])
        padded = preprocessing.sequence.pad_sequences(
            tokenized, maxlen=maxlen)
        one_hot = np_utils.to_categorical(padded, num_classes=28)
        pred = model.predict(np.array(one_hot))[0]
        r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
        ax = fig.add_subplot(5, 5, i)
        ax.imshow([[pred]], interpolation='nearest')
        ax.set_title(name)
        ax.axis('off')
        print(name + ',', 'R,G,B:', r, g, b)
        print(i, len(names))
        # plot_rgb(pred, i, len(names))
    plt.tight_layout()

    plt.show()


predict(['blue bear', 'blood red', 'red bear',
         'blood blue', 'teal', 'aquamarine', 'bleu', 'blue', 'red', 'der', 'rde'])
