



import pandas as pd





path_to_csv = "iris.csv"





data = pd.read_csv(path_to_csv,encoding = "utf-8",header = None)




data




data.shape




data.columns




data.columns = ["sepal length","sepal width","petal length","petal width","class"]




data




data.columns




data.shape




data.describe(include = "all")




import matplotlib.pyplot as plt




data.hist()




plt.hist(data['sepal width'])




plt.hist(data['sepal length'])




plt.hist(data['petal width'])




plt.hist(data['petal length'])




data.boxplot()




data.boxplot("sepal length")




data.boxplot("sepal width")





data.boxplot("petal length")





data.boxplot("petal width")





data.head()





data.tail()

data.plot.scatter("sepal length","sepal width")

data.plot.scatter("petal length","petal width")

