#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo


# In[27]:


superstore=pd.read_csv('Sample - Superstore.csv',encoding='Windows-1252')
superstore.head()


# In[8]:


superstore.dtypes


# In[10]:


superstore['Order Date']=pd.to_datetime(superstore['Order Date'])
from_=superstore['Order Date'].min()
to_=superstore['Order Date'].max()


# In[11]:


from_


# In[12]:


to_


# In[14]:


superstore=superstore.sort_values(by='Order Date')
superstore.head()


# In[15]:


superstore['year']=pd.DatetimeIndex(superstore['Order Date']).year
superstore['month']=pd.DatetimeIndex(superstore['Order Date']).month
superstore['day']=pd.DatetimeIndex(superstore['Order Date']).day
superstore.head()


# In[16]:


superstore['Category'].unique()


# In[20]:


superstore_yearly_profit=superstore.groupby(['year','Category']).agg({'Profit':'sum'}).reset_index()
superstore_yearly_profit


# In[22]:


sns.barplot(superstore_yearly_profit['year'],superstore_yearly_profit['Profit'])


# In[23]:


sns.barplot(superstore_yearly_profit['Category'],superstore_yearly_profit['Profit'])


# In[31]:


px.line(superstore_yearly_profit,x='year',y='Profit',color='Category',title='profit vs year')


# In[20]:


superstore_monthly_profit=superstore.groupby(['year','month','Category']).agg({'Profit':'sum'}).reset_index()
superstore['Date']=superstore_monthly_profit.year.astype(str) +'-'+ superstore_monthly_profit.month.astype(str)
px.line(superstore_monthly_profit,x='Date',y='Profit',color='Category',title='month vs profit')


# In[21]:


#top 10 customers

#top10=superstore.sort_values(by='Profit',ascending=False)
#top10=top10.head(10)
#print(top10['Customer Name'])

top10=superstore.groupby('Customer Name').agg({'Profit':'sum'}).reset_index().sort_values(by='Profit', ascending=False).head(10)
px.bar(top10,x='Customer Name',y='Profit',title='top 10 customer')


# In[52]:


geo_data=superstore.groupby('State').agg({'Profit':'sum'}).reset_index()
geo_data


# In[53]:



state_codes = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'District of Columbia': 'DC',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


# In[58]:


geo_data.State=geo_data.State.map(state_codes)
geo_data.head()


# In[61]:


px.choropleth(geo_data,locations='State',color='Profit',locationmode='USA-states',scope='usa',title='Profit By State')


# In[66]:


superstore


# In[10]:


superstore['customerid2']=superstore['Customer ID'].apply(lambda x:x.split('-')[0])


# In[12]:


superstore.head()


# In[13]:


superstore.drop(columns='customerid2')


# In[15]:


data1=superstore.groupby('Region').agg({'Profit':'sum'}).reset_index()
data1


# In[34]:


#best region
px.bar(data1,x='Region',y='Profit')


# In[24]:


#top 10 cietis

#data2=superstore.sort_values(by='Profit',ascending=False)
#data2=data2.head(10)
#print(data2['City'])

data2=superstore.groupby('City').agg({'Profit':'sum'}).reset_index().sort_values(by='Profit',ascending=False).head(10)
data2


# In[30]:


px.bar(data2,x='City',y='Profit')


# In[33]:


data3=superstore[['Ship Mode','Sales','Profit']]
data3=data3.groupby(['Ship Mode']).sum().reset_index()
plt.figure(figsize=(15,8))
plt.subplot(1,1,1)
plt.bar(x=data3['Ship Mode'],height=data3['Sales'],color='#F05454')
plt.bar(x=data3['Ship Mode'],height=data3['Profit'],bottom=data3['Sales'],color='#30475E')
plt.legend(['sales','profit'])
plt.title('sales & profit across ship mode')


# In[39]:


data4=superstore[['Region','Sales','Profit']]
data4=data4.groupby(['Region']).sum().reset_index()
plt.figure(figsize=(15,8))
plt.subplot(2,1,1)
plt.bar(x=data4['Region'],height=data4['Sales'],color='#F05454')
plt.bar(x=data4['Region'],height=data4['Profit'],bottom=data4['Sales'],color='#30475E')
plt.title('sales& profit across region')
plt.legend(['sales','profit'])


# In[ ]:





# In[ ]:




