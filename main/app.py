import matplotlib.pyplot
import  pandas as pd
from  matplotlib import pyplot

data = pd.read_csv("/home/jhonier/Documentos/Colaboracion/u_visualization/data/train.csv")
print(data.shape)
data=(3,4 , 5 , 5,  13)
fig,simple_chart = pyplot.subplots()
simple_chart.plot(data)
matplotlib.pyplot.show()