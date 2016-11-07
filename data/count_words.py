import pandas as pd
import sys
import matplotlib.pyplot as plt

def plot(data):
    x = data['ranking']
    y = data[0]
    plt.loglog(x, y, 'o')

    plt.xlabel('Ranking')
    plt.ylabel('Frequencia')
    plt.show()

def get_data(path):
    file=open(path,"r+")
    wordcount={}
    descarte = [',', '.', '?', '!', '-', ';']
    for word in file.read().split():

        for d in descarte:
            if d in word:
                word = word.replace(d, "")

        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    data = pd.DataFrame.from_dict(wordcount, orient='index')
    data = data.sort_values(by=[0], ascending=False)
    data =  data.reset_index()
    data['ranking'] = data.index
    print data
    return data


data = get_data(sys.argv[1])
plot(data)