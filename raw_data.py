
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression


# In[2]:


df_mvp = pd.read_html('https://www.basketball-reference.com/awards/mvp.html')


# In[3]:


len(df_mvp)


# In[4]:


df_mvp = df_mvp[0]


# In[5]:


df_mvp.columns


# In[6]:


df_mvp.columns = df_mvp.columns.droplevel()


# In[7]:


df_mvp_new = df_mvp.drop(columns=['Voting','Lg','Tm','Player','Age','MP','STL','BLK','FG%','3P%','FT%','WS','WS/48','G'],axis=1)
df_mvp_pivot = df_mvp_new.pivot_table(columns='Season')


# In[8]:


df_mvp1 = df_mvp_pivot.transpose()
df_mvp1 = df_mvp1.reset_index()
df_mvp1['Year'] = [int(i.split('-')[0]) for i in df_mvp1['Season']]
df_mvp1.drop('Season',axis=1)
df_mvp1 = df_mvp1.pivot_table(columns='Year')


# In[9]:


df_mvp2 = df_mvp1.transpose()
df_mvp2


# In[10]:


df_mvp2.to_csv("mvp_data.csv")


# In[11]:


df_mvp_position = pd.read_html('https://basketball.realgm.com/nba/awards/by-type')


# In[12]:


len(df_mvp_position)


# In[13]:


df_mvp_position = df_mvp_position[0]


# In[14]:


df_position = df_mvp_position.drop(columns=['Team','Weight','Age','Pre-Draft Team','Draft Yr','Player'],axis=1)
df_position['Season'] = [int(i.split('-')[0]) for i in df_position['Season']]
df_position[['Height','Inches']] = df_position['Height'].str.split('-',expand=True)
df_position[['Height','Inches']] = df_position[['Height','Inches']].apply(pd.to_numeric,errors='coerce',axis=1)
df_position['Height'] = df_position['Height']*12
df_position['Height'] = df_position['Height'] + df_position['Inches']
df_position = df_position.drop(columns=['Inches'])
df_position = df_position.rename(columns={'Height':'Height (in)'})
df_position


# In[15]:


df_position.to_csv("positions.csv")

