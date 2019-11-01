
# coding: utf-8

# # Bigmart Sales Analysis: For data comprising of transaction records of a sales store. 
# The data has 8523 rows of 12 variables. Predict the sales of a store. Sample Test data set available
# here https://datahack.analyticsvidhya.com/contest/practice-problem-big-mart-sales-iii/
# 
# Variable - Description
# 
# Item_Identifier - Unique product ID
# 
# Item_Weight - Weight of product
# 
# Item_Fat_Content - Whether the product is low fat or not
# 
# Item_Visibility - The % of total display area of all products in a store allocated to the particular product
# 
# Item_Type - The category to which the product belongs
# 
# Item_MRP - Maximum Retail Price (list price) of the product
# 
# Outlet_Identifier - Unique store ID
# 
# Outlet_Establishment_Year - The year in which store was established
# 
# Outlet_Size - The size of the store in terms of ground area covered
# 
# Outlet_Location_Type - The type of city in which the store is located
# 
# Outlet_Type - Whether the outlet is just a grocery store or some sort of supermarket
# 
# Item_Outlet_Sales - Sales of the product in the particulat store. This is the outcome variable to be predicted.

# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[48]:


Train = pd.read_csv("Train.csv",header=None)
Test = pd.read_csv("Test.csv",header=None)


# In[49]:


headers = ['Item_Identifier','Item_Weight','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type','Item_Outlet_Sales']


# In[50]:


Train.columns = headers
Test.columns = headers[:11]


# In[51]:


Train['Source'] = 'Train'
Test['Source'] = 'Test'
final_df = Test[['Item_Identifier','Outlet_Identifier']].copy()


# In[52]:


Data = pd.concat([Train,Test],ignore_index=True)


# In[53]:


Data['Outlet_Establishment_Year'] = Data['Outlet_Establishment_Year'].apply(lambda x: 2017 - x)


# In[54]:


Data['Item_Fat_Content'].replace('LF','Low',inplace = True)


# In[55]:


Data['Item_Fat_Content'].replace('low fat','Low',inplace = True)


# In[56]:


Data['Item_Fat_Content'].replace('reg','Regular',inplace = True)


# replace missing values with mean for Item_Weight

# In[57]:


Item_Weight_Mean = Data['Item_Weight'].mean(axis=0)


# In[58]:


Data['Item_Weight'].replace(np.NaN,Item_Weight_Mean, inplace = True)


# replace missing values with mean for Item_Visibility

# In[59]:


Data['Item_Visibility'].replace(0,np.NaN,inplace = True)


# In[60]:


Item_Visibility_Mean = Data['Item_Visibility'].mean(axis = 0)


# In[61]:


Data['Item_Visibility'].replace(np.NaN,Item_Visibility_Mean,inplace = True)


# replace item_type by itemID initials (to reduce total number of types from 16 to 3)

# In[62]:


Data['Item_Type'] = Data['Item_Identifier'].apply(lambda x : x[0:2])


# replace missing values for Outlet_Size

# In[63]:


from scipy.stats import mode


# In[64]:


Outlet_Size_mode = Data.pivot_table(values = 'Outlet_Size',columns = 'Outlet_Type', aggfunc = (lambda x:x.mode().iat[0]))


# In[65]:


miss_bool = Data['Outlet_Size'].isnull()


# In[66]:


Data.loc[miss_bool,'Outlet_Size'] = Data.loc[miss_bool,'Outlet_Type'].apply(lambda x: Outlet_Size_mode[x])


# Convert categorical to numerical using dummy columns

# In[67]:


dummies = ['Item_Fat_Content','Item_Type','Outlet_Location_Type','Outlet_Size','Outlet_Type']


# In[68]:


Data = pd.get_dummies(Data, columns = dummies)


# Drop useless columns

# In[69]:


Data.drop(['Outlet_Identifier','Item_Identifier'],axis=1, inplace=True)


# split df into train and test

# In[70]:


Train  = Data.loc[Data['Source']=='Train']
Test = Data.loc[Data['Source']=='Test']


# In[71]:


Train.drop('Source', axis = 1, inplace = True)
Test.drop('Source', axis = 1, inplace = True)


# In[72]:


x_train = np.array(Train.drop(['Item_Outlet_Sales'],axis=1))
y_train = np.array(Train['Item_Outlet_Sales'])


# In[73]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics


# In[74]:


lr = LinearRegression(normalize = True)


# In[75]:


lr.fit(x_train,y_train)


# In[76]:


lr.intercept_


# In[77]:


lr.coef_


# In[78]:


y_train_pred = lr.predict(x_train)


# In[79]:


rmse = metrics.mean_squared_error(y_train,y_train_pred)


# In[80]:


rmse


# In[81]:


y_train_pred


# In[82]:


output_df = pd.DataFrame(y_train_pred)


# In[83]:


final_df['Outles_Sales'] = output_df


# In[84]:


final_df


# In[85]:


final_df.to_csv("output.csv")

