
# coding: utf-8

# In[2]:


#import the packages "Pandas" and "MatPlotLib" into Jupyter Notebook
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


#import Facebook's stock data
fb = pd.DataFrame.from_csv('../data/facebook.csv')


# In[5]:


print(fb.head())


# In[6]:


print(fb.shape)


# In[7]:


# print summary statistics of Facebook
print(fb.describe())


# In[8]:


# select all the price information of Facebook in 2016.
fb_2015 = fb.loc['2015-01-01':'2015-12-31']


# In[9]:


# print the price of Facebook on '2015-03-16'
print(fb_2015.loc['2015-03-16'])


# In[13]:


# print the opening price of the first row
print(fb.iloc[0, 0])


# In[20]:


#Calculate moving average using .rolling()
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()


# In[12]:


plt.figure(figsize=(10, 8))
fb['Close'].plot()
plt.show()


# In[26]:


#Plot the graph of moving average 10 and 50
plt.figure(figsize=(10, 8))
fb['Close'].plot()
fb['MA10'].plot()
fb['MA50'].plot()
plt.show()


# In[34]:


#daily profit
fb['Close1'] = fb['Close'].shift(-1)
fb.iloc[500:505,:]


# In[35]:


fb['Shares'] = [1 if fb.loc[ei,'MA10']>fb.loc[ei,'MA50'] else 0 for ei in fb.index]


# In[38]:


fb['Profit'] = [fb.loc[ei,'Close1'] - fb.loc[ei,'Close'] if fb.loc[ei,'Shares'] == 1 else 0 for ei in fb.index]


# In[41]:


#plot Profit to analyse our situation
plt.figure(figsize=(10, 8))
fb['Profit'].plot()
plt.show()


# In[42]:


#create new variable 'Wealth' to calculate cumulative wealth
fb['Wealth'] = fb['Profit'].cumsum()


# In[43]:


#verify the tail of DataFrame to see if we are losing or earning money
fb.tail()


# In[ ]:




