#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. How do you select specific rows and columns from
# a DataFrame in pandas?write an example program.
# import numpy as np
# import pandas as pd
# data={'Name':['Nia','Mia','Lis','Ana'],
#      'Age':[21,22,23,24],
#      'City':['Kannur','Ernakulum','Calicut','Banglore']}


# In[3]:


# df=pd.DataFrame(data)


# In[5]:


# print("ori dataset")
# df


# In[7]:


# sel_columns=df[['Name','Age']]
# print(sel_columns)


# In[8]:


# sel_rows=df.loc[df['Age']>18,['Name','Age']]


# In[9]:


# sel_rows


# In[10]:


# 4.Using Seaborn module Draw a Scatterplot Using
# sample dataset.and also draw heatmap.


# In[12]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[13]:


df=pd.read_csv("C:/Users/afsha/Videos/Salaries.csv")


# In[14]:


df


# In[15]:


df.head(10)


# In[24]:


df.fillna(0, inplace=True)



# In[25]:


df


# In[26]:


sns.scatterplot(x='BasePay', y='TotalPay', data=df)
plt.title('Scatter Plot of BasePay vs TotalPay')
plt.show()


# In[29]:





# In[ ]:




