import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split

import sklearn.metrics as sm




data=pd.read_csv('Crop.csv')
data=data[['temperature','humidity','ph','rainfall','label']]
print(data)



print(data.head(10))
print(data.info() ) #about information colm and rows
print(data.isnull().sum()) #no. of empty spaces
data=data.dropna() #removing empty spaces or cleaning the datasets in empty spaces



print(data.columns) #list of columns
print(data['label'].describe()) #description of perticular column

print(data['label'].value_counts()) #no. of counts for each crop

cropnames=[data.label.unique() ]
print("crops names ",cropnames)

#mapping crop
dictionary_crops={'rice':1, 'maize':2, 'chickpea':3, 'kidneybeans':4, 'pigeonpeas':5,
       'mothbeans':6, 'mungbean':7, 'blackgram':8, 'lentil':8, 'pomegranate':10,
       'banana':11, 'mango':12, 'grapes':13, 'watermelon':14, 'muskmelon':15, 'apple':16,
       'orange':17, 'papaya':18, 'coconut':19, 'cotton':20, 'jute':21, 'coffee':22}

print("each crop mapped for unique number ",dictionary_crops)
data['label']=data['label'].map(dictionary_crops)

print(data)




y = data.label
X = data.drop('label', axis=1)
print(X)
print(y)



# Split X and y into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state=0)

# Print number of observations in X_train, X_test, y_train, and y_test
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)



from sklearn.ensemble import RandomForestRegressor

model1 = RandomForestRegressor(n_estimators=500)

from sklearn.linear_model import LinearRegression

model2 = LinearRegression()  



#training
model1.fit(X_train, y_train)

model2.fit(X_train, y_train)

## Predict Test set results
y_pred1 = model1.predict(X_test)


y_pred2 = model2.predict(X_test)



accuracy=sm.r2_score(y_test, y_pred1)
print("accuracy of Random Forest Regressor is {:.2f}".format(accuracy*100))

accuracy=sm.r2_score(y_test, y_pred2)
print("accuracy of Linear Regressor is {:.2f}".format(accuracy*100))



from  xgboost import XGBRegressor
model3= XGBRegressor()


model3.fit(X_train, y_train)
y_pred3 = model3.predict(X_test)

accuracy=sm.r2_score(y_test, y_pred3)
print("accuracy of XGB Regressor is {:.2f}".format(accuracy*100))


#from sklearn.externals import joblib 
import joblib
# Save the model as a pickle in a file 
joblib.dump(model1, 'final_pickle_model_crop.pkl') 
  
# Load the model from the file 
final_model = joblib.load('final_pickle_model_crop.pkl')

pred=final_model.predict(X_test)

accuracy=sm.r2_score(y_test,pred)
      
print("Accurcay of final model is {:.2f} % ".format(accuracy*100))
