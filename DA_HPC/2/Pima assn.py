
# coding: utf-8

# Download Pima Indians Diabetes dataset. Use Naive Bayes‟ Algorithm for classification
#  Load the data from CSV file and split it into training and test datasets.
#  summarize the properties in the training dataset so that we can calculate
# probabilities and make predictions.
#  Classify samples from a test dataset and a summarized training dataset.

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


path_to_csv = "/home/bharati/Desktop/diabetes.csv"


# In[4]:


data = pd.read_csv(path_to_csv, encoding = "utf-8")


# In[5]:


data


# In[6]:


data.shape


# In[7]:


data.describe()


# In[8]:


data.describe(include = "all")


# In[10]:


data.boxplot()


# In[13]:


import numpy as np


# In[14]:


df = data.copy()


# dq = df.iloc[:,1:8]

# In[20]:


for i in df.columns[1:8]:
    df[i].replace(0,np.nan,inplace = True)
    m = df[i].mean()
    df[i].replace(np.nan,m,inplace = True)


# In[24]:


df.describe(include = "all")


# In[25]:


from sklearn.preprocessing import StandardScaler


# In[26]:


from sklearn.model_selection import train_test_split


# In[28]:


x = np.array(df.drop('outcome',axis = 1))


# In[30]:


y = np.array(df['outcome'])


# In[32]:


s = StandardScaler()


# In[33]:


x_scale = s.fit_transform(x)


# In[70]:


x_train, x_test, y_train, y_test = train_test_split(x_scale,y,random_state = 0,test_size = 0.2)


# In[71]:


from sklearn.naive_bayes import GaussianNB


# In[72]:


gnb = GaussianNB()


# In[73]:


gnb.fit(x_train,y_train)


# In[74]:


y_pred = gnb.predict(x_test)


# In[75]:


from sklearn.metrics import accuracy_score


# In[76]:


from sklearn.metrics import confusion_matrix


# In[77]:


conf_mat = confusion_matrix(y_test, y_pred)


# In[78]:


conf_mat


# In[79]:


acc_scr = accuracy_score(y_test, y_pred)


# In[80]:


acc_scr


# In[81]:


from sklearn.metrics import precision_recall_fscore_support


# In[83]:


prf = precision_recall_fscore_support(y_test, y_pred)


# In[84]:


prf

