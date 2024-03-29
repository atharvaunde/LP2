

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





Train = pd.read_csv("Train.csv",header=None)
Test = pd.read_csv("Test.csv",header=None)



headers = ['Item_Identifier','Item_Weight','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type','Item_Outlet_Sales']




Train.columns = headers
Test.columns = headers[:11]




Train['Source'] = 'Train'
Test['Source'] = 'Test'
final_df = Test[['Item_Identifier','Outlet_Identifier']].copy()



Data = pd.concat([Train,Test],ignore_index=True)



Data['Outlet_Establishment_Year'] = Data['Outlet_Establishment_Year'].apply(lambda x: 2017 - x)




Data['Item_Fat_Content'].replace('LF','Low',inplace = True)





Data['Item_Fat_Content'].replace('low fat','Low',inplace = True)





Data['Item_Fat_Content'].replace('reg','Regular',inplace = True)


Item_Weight_Mean = Data['Item_Weight'].mean(axis=0)



Data['Item_Weight'].replace(np.NaN,Item_Weight_Mean, inplace = True)




Data['Item_Visibility'].replace(0,np.NaN,inplace = True)




Item_Visibility_Mean = Data['Item_Visibility'].mean(axis = 0)




Data['Item_Visibility'].replace(np.NaN,Item_Visibility_Mean,inplace = True)





Data['Item_Type'] = Data['Item_Identifier'].apply(lambda x : x[0:2])



from scipy.stats import mode



Outlet_Size_mode = Data.pivot_table(values = 'Outlet_Size',columns = 'Outlet_Type', aggfunc = (lambda x:x.mode().iat[0]))



miss_bool = Data['Outlet_Size'].isnull()



Data.loc[miss_bool,'Outlet_Size'] = Data.loc[miss_bool,'Outlet_Type'].apply(lambda x: Outlet_Size_mode[x])




dummies = ['Item_Fat_Content','Item_Type','Outlet_Location_Type','Outlet_Size','Outlet_Type']



Data = pd.get_dummies(Data, columns = dummies)



Data.drop(['Outlet_Identifier','Item_Identifier'],axis=1, inplace=True)



Train  = Data.loc[Data['Source']=='Train']
Test = Data.loc[Data['Source']=='Test']



Train.drop('Source', axis = 1, inplace = True)
Test.drop('Source', axis = 1, inplace = True)





x_train = np.array(Train.drop(['Item_Outlet_Sales'],axis=1))
y_train = np.array(Train['Item_Outlet_Sales'])




from sklearn.linear_model import LinearRegression
from sklearn import metrics




lr = LinearRegression(normalize = True)




lr.fit(x_train,y_train)




lr.intercept_



lr.coef_




y_train_pred = lr.predict(x_train)





rmse = metrics.mean_squared_error(y_train,y_train_pred)




rmse


y_train_pred



output_df = pd.DataFrame(y_train_pred)



final_df['Outles_Sales'] = output_df




final_df




final_df.to_csv("output.csv")

