#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

def plot(data):
    x = data['ranking']
    y = data[0]
    plt.loglog(x, y, 'o')

    plt.xlabel('Ranking')
    plt.ylabel('Frequencia')
    plt.show()


def get_data(path):

    file = open(path, "r+")
    wordcount={}
    descarte = [',', '.', '?', '!', '-', '—', ';']
    for word in file.read().split():

        for d in descarte:
            if d in word:
                word = word.replace(d, "")

        if not (word == ""):

            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    data = pd.DataFrame(list(wordcount.iteritems()),
                 columns=['word', 'num_words'])
    data = data.sort_values(by=['num_words'], ascending=False)

    data = data.reset_index()

    data['ranking'] = data.index

    del data['index']

    log = lambda x: 0 if x == 0 else np.log(x)

    data['ranking_log'] = data['ranking'].apply(log)
    data['num_words_log'] = data['num_words'].apply(log)

    data.to_csv("./output.csv")

    return data

data = get_data('brascubas.txt')
#data = get_data(sys.argv[1])
#plot(data)