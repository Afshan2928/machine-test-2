#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 4.Using Seaborn module draw heatmap.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:/Users/afsha/Videos/Salaries.csv")


# In[3]:


df


# In[4]:


df.fillna(0)


# In[8]:


columns_for_heatmap = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits', 'Year']


df_heatmap = df[columns_for_heatmap]


df_heatmap = df_heatmap.apply(pd.to_numeric, errors='coerce')

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df_heatmap.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Heatmap')
plt.show()


# In[ ]:




