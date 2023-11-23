#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 5.Draw a piechart analyze a dataset.


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


data={'Name':['Han','Lan','Nan','kia'],
     'Value':[29,43,43,43]}


# In[7]:


df=pd.DataFrame(data)
df


# In[9]:


plt.figure(figsize=(8, 8))
plt.pie(df['Value'], labels=df['Name'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Pie Chart: Distribution')
plt.show()


# In[ ]:




