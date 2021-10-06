#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import category_encoders as ce
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import plotly.graph_objects as go
from sklearn.pipeline import make_pipeline
from sklearn.inspection import plot_partial_dependence
import json
import urllib.request
import xgboost as xgb
from xgboost import XGBRegressor


# ## Split data into Train n Test 
# ### split_data give X_train, y_train,  X_test, y_test

# In[52]:


def split_data(df, split_frac=0.3, return_val=False, rand_state=7):
    X  = df.drop('tax', axis=1)
    y  = df['tax']
    #print(y)
    '''stratify = y'''
    return train_test_split(X, y, test_size = split_frac, random_state = rand_state)


# ## get_model_score returns:
# ### X_train, y_train score if val_score && test_score == False
# ### X_train, y_train , X_val & y_val score  if Val_score == True & test_score == False
# ### X_train, y_train , X_val & y_val , X_test, y_test score if Val_score == True & test_score == True

# In[93]:


'''stratify = y_train,'''
def get_model_scores(mod, X_train, y_train, X_test, y_test, val_score = True, test_score=False):
    X_train = X_train.drop('date', axis=1)
    X_test = X_test.drop('date', axis=1)
    if val_score:
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, 
                                                          test_size = 0.8, 
                                                          train_size = 0.2,
                                                          random_state= 9)        
    mod.fit(X_train, y_train)
    
    results = {}
    
    results['train_score'] = mod.score(X_train, y_train)
    if val_score:
        results['val_score'] = mod.score(X_val, y_val)
        
    if test_score:
        results['test_score'] = mod.score(X_test, y_test)
        
    return results


# # Get data locally as csv file
# ## With addition of 3 columns

# In[94]:


def local_dataset():
    data_set = pd.read_csv(r"C:\Users\samina\Desktop\GA_DATA_SCIENCE\Data_Sci\Homework\Unit4\Final_project\data.csv", parse_dates=['date'])
    data_set = data_set.fillna(0)
    data_set['year'] = data_set['date'].dt.year
    data_set['month'] = data_set['date'].dt.month
    data_set['day'] = data_set['date'].dt.day
    return data_set


# # Data frame ready to go

# In[95]:


df = local_dataset()


# In[96]:


df.sort_values(by='date', ascending=True)
df.tail(10)


# # Model Selection and train, test, val baseline scores

# In[97]:


mod = xgb.XGBRegressor(verbosity=1)
te = ce.TargetEncoder()
pipe = make_pipeline(te, mod)

print(pipe)        #debugging need to remove


# In[98]:


#pipe.fit(X_train, y_train)


# In[99]:


X_train, X_test, y_train, y_test = split_data(df)


# In[100]:


X_train


# In[101]:


baseline_score = get_model_scores(pipe, X_train, y_train, X_test, y_test, test_score=True)


# In[102]:


baseline_score


# In[106]:


''','''
imp = pd.DataFrame(
    {
        'Col': X_train.drop('date',axis=1).columns,
       'Imp': pipe[-1].feature_importances_}
)
imp.sort_values(by='Imp', ascending=False)


# In[ ]:




