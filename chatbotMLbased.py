import json
from logging import warning 
import random
import string

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

# ignore warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import sklearn

import pickle



f = open("intents.json")
data = json.load(f)
f.close()

# Mendapatkan Penggalan Kata
lemmatizer = WordNetLemmatizer()

# Menampung Penggalan Kata
words = []
classes = []
doc_X = []
doc_Y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        token = nltk.word_tokenize(pattern)
        words.extend(token)
        doc_X.append(pattern)
        doc_Y.append(intent["tag"])

# Menambahkan tag jika belum tersedia
    if intent["tag"] not in "classes":
        classes.append(intent["tag"])

words = [lemmatizer.lemmatize(word.lower())
        for word in words if word not in string.punctuation]
words = sorted(set(words))
classes = sorted(set(classes))

# List training Data
training = []
out_empty = [0] * len(classes)

# Membuat Model Training Chatbot
for idx, doc in enumerate(doc_X):
    bow = []
    text = lemmatizer.lemmatize(doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)

    # membuat urutan index untuk class
    output_row = list(out_empty)
    output_row[classes.index(doc_Y[idx])] = 1

    # add the one hot encoded BoW and associated classes to training
    training.append([bow, output_row])


# deep learning model
# model = tf.keras.models.load_model("model_chatbot.h5")
model = pickle.load(open("modelml_chatbot.pkl", "rb"))


def clean_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens


def bag_of_words(text, vocab):
    tokens = clean_text(text)
    bow = [0] * len(vocab)
    for w in tokens:
        for idx, word in enumerate(vocab):
            if word == w:
                bow[idx] = 1
    return np.array(bow)


def pred_class(text, vocab=words, labels=classes):
    bow = bag_of_words(text, vocab)
    result = model.predict(np.array([bow]))[0]
    thresh = 0.2
    y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

    y_pred.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in y_pred:
        return_list.append(labels[r[0]])
    return return_list


def get_response(intents_list, intents_json = data):
    tag = intents_list[0]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result
