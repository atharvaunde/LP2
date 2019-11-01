
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path_to_csv = "/home/bharati/Desktop/iris.csv"


# In[8]:


data = pd.read_csv(path_to_csv,encoding = "utf-8",header = None)


# In[9]:


data


# In[11]:


data.shape


# In[13]:


data.columns


# In[14]:


data.columns = ["sepal length","sepal width","petal length","petal width","class"]


# In[15]:


data


# In[16]:


data.columns


# In[17]:


data.shape


# In[23]:


data.describe(include = "all")


# In[24]:


import matplotlib.pyplot as plt


# In[25]:


data.hist()


# In[30]:


plt.hist(data['sepal width'])


# In[31]:


plt.hist(data['sepal length'])


# In[33]:


plt.hist(data['petal width'])


# In[34]:


plt.hist(data['petal length'])


# In[38]:


data.boxplot()


# In[39]:


data.boxplot("sepal length")


# In[40]:


data.boxplot("sepal width")


# In[41]:


data.boxplot("petal length")


# In[42]:


data.boxplot("petal width")


# In[45]:


data.head()


# In[47]:


data.tail()

data.plot.scatter("sepal length","sepal width")

data.plot.scatter("petal length","petal width")

