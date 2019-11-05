

import pandas as pd


# In[2]:


import matplotlib.pyplot as plt




path_to_csv = "diabetes.csv"





data = pd.read_csv(path_to_csv, encoding = "utf-8")




data





data.shape




data.describe()





data.describe(include = "all")




data.boxplot()




import numpy as np




df = data.copy()






for i in df.columns[1:8]:
    df[i].replace(0,np.nan,inplace = True)
    m = df[i].mean()
    df[i].replace(np.nan,m,inplace = True)



df.describe(include = "all")





from sklearn.preprocessing import StandardScaler




from sklearn.model_selection import train_test_split





x = np.array(df.drop('outcome',axis = 1))




y = np.array(df['outcome'])





s = StandardScaler()



x_scale = s.fit_transform(x)




x_train, x_test, y_train, y_test = train_test_split(x_scale,y,random_state = 0,test_size = 0.2)





from sklearn.naive_bayes import GaussianNB




gnb = GaussianNB()





gnb.fit(x_train,y_train)




y_pred = gnb.predict(x_test)


from sklearn.metrics import accuracy_score



from sklearn.metrics import confusion_matrix



conf_mat = confusion_matrix(y_test, y_pred)




conf_mat





acc_scr = accuracy_score(y_test, y_pred)



acc_scr




from sklearn.metrics import precision_recall_fscore_support



prf = precision_recall_fscore_support(y_test, y_pred)


prf

