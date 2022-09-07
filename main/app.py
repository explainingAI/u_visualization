import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import  PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from tkinter import filedialog
import logging as log

def openfilename():
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title="Open csv")
    return filename

def trainPca(data):
    nuevo_pca = PCA(n_components=2)
    data_pca = nuevo_pca.fit_transform(data)
    return data_pca

def trainTsne(data):
    x_embedded = TSNE(n_components=2, learning_rate='auto',
    init ='random', perplexity = 3).fit_transform(data)

    return x_embedded

def main():
    path= openfilename()
    #path="/home/jhonier/Documentos/Colaboracion/u_visualization/data/data.csv"
    log.info("read dataset: ", path)
    data = pd.read_csv(path)

    x_std = StandardScaler().fit_transform(data)

    log.info("train data with PCA")
    #PCA
    data_pca= trainPca(x_std)
    dfPca = pd.DataFrame(data_pca)
    x_pca = dfPca.iloc[:, 0]
    y_pca = dfPca.iloc[:, 1]

    log.info("train data with TSNE")
    #TSNE
    data_tsne = trainTsne(x_std)
    data_tsne = pd.DataFrame(data_tsne)
    x_tsne = data_tsne.iloc[:, 0]  # Primera columna
    y_tsne = data_tsne.iloc[:, 1]  # Segunda columna

    log.info("plotting data")
    #plot
    fig,(pltPca,pltTsne) = plt.subplots(2)

    fig.suptitle('Data visualization')

    pltPca.set_title("pca")
    pltPca.scatter(x_pca, y_pca)

    pltTsne.set_title("tsne")
    pltTsne.scatter(x_tsne, y_tsne)
    plt.show()

if __name__ == '__main__':
    main()
