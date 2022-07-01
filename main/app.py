import matplotlib.pyplot as plt
import  pandas as pd
from  matplotlib import pyplot
from  sklearn.decomposition import  PCA
import numpy as np
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("/home/jhonier/Documentos/Colaboracion/u_visualization/data/data.csv")

X_std = StandardScaler().fit_transform(data)

nuevo_pca = PCA(n_components=2)
X = nuevo_pca.fit_transform(X_std)
print(X)
data2d = pd.DataFrame(X)

x = data2d.iloc[:, 0] # Primera columna
y = data2d.iloc[:, 1] # Segunda columna

plt.scatter(x,y)
plt.show()