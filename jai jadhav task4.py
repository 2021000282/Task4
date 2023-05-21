#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[5]:


#loading dataset
data=pd.read_csv("C:/Users/user14/Documents/terrorism.csv",encoding='latin1')
data.head()


# In[6]:


data.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City','latitude':'latitude',
    'longitude':'longitude','summary':'summary','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','weaptype1_txt':'Weapon','nkill':'kill',
     'nwound':'Wound'},inplace=True)


# In[8]:


data = data[['Year','Month','day','Country','State','Region','City','latitude','longitude',"Attacktype",'kill',
               'Wound','target1','summary','Group','Targettype','Weapon','motive']]


# In[9]:


data.head()


# In[10]:


data.shape #dimension of data


# In[11]:


data.isnull().sum() #check null values


# In[12]:


data['Wound'] = data['Wound'].fillna(0)
data['kill'] = data['kill'].fillna(0)


# In[14]:


data.describe()  #summary of data


# In[22]:


#obs 1
year = data['Year'].unique()
years_count = data['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year,y = years_count)
plt.xticks(rotation = 50)
plt.xlabel('Attacking Year')
plt.ylabel('Number of Attacks Each Year')
plt.show()


# Here,maximum number of attacks are found the year 2012-2017.

# In[23]:


#obs 2
attack = data.Country.value_counts()[:10]
attack  #gives total no of attacks w.r.t country


# In[27]:


data.Group.value_counts()[1:10]


# In[44]:


df=data[['Group','Country','kill']]
df=df.groupby(['Group','Country'],axis=0).sum().sort_values('kill',ascending=False).drop('Unknown').reset_index().head(10)
df      #gives no of peoples kill w.r.t countries and group.


# In[36]:


#obs 3
df = data[['Year','kill']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(15,8))
df.plot(kind='bar',alpha=0.7,ax=ax4)
plt.xticks(rotation = 50)
plt.ylabel("Number of killed peope")
plt.xlabel('Year')


# Here, most of the peoples died in the year 2012-2017.

# In[38]:


#obs 4
data['City'].value_counts().to_frame().sort_values('City',axis=0,ascending=False).head(10).plot(kind='bar',figsize=(15,8),color='grey')
plt.xticks(rotation = 50)
plt.xlabel("City")
plt.ylabel("Number of attack")
plt.show()


# Here,maximum number of attacks occured at the Unknown city.
# However, after then the Baghdad city was most affected w.r.t number of attacks.

# In[41]:


#obs 5
data['Attacktype'].value_counts().plot(kind='bar',figsize=(15,8),color='green')
plt.xticks(rotation = 50)
plt.xlabel("Attacktype")
plt.ylabel("Number of attack")
plt.show()


# Here,maximum number of attacks type is Armed assault but less as compared to Bombing/Explosion.

# In[43]:


#obs 6
data[['Attacktype','kill']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(15,8),color=['purple'])
plt.xticks(rotation=50)
plt.ylabel('Number of people')
plt.xlabel('Attack type')
plt.show()


# Here, maximum number of peoples are killed/died due to Armed assault and Bombing/explosion.

# In[51]:


#obs 7
data['Group'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='orange',figsize=(15,8))
plt.xlabel("terrorist group name")
plt.ylabel("Attack number")
plt.show()


# Here,above fig.shows the top 10 terrorist group which are attacked.
# The Taliban, ISIL, ISL are the top 3 groups which are attacked in a maximum number of time.

# In[49]:


#obs 8
data[['Group','kill']].groupby(['Group'],axis=0).sum().drop('Unknown').sort_values('kill',ascending=False).head(10).plot(kind='bar',color='yellow',figsize=(15,8))
plt.xlabel("terrorist group name")
plt.ylabel("No of killed people")
plt.show()


# Here,above fig.shows the top 10 terrorist group which are killed most of the people.
# The ISIS and Taliban are the top 3 groups which are killed maximum number of peoples.

# In[52]:


#obs 9
pd.crosstab(data.Year, data.Region).plot(kind='area',stacked=False,figsize=(15,8))
plt.ylabel('Number of Attacks')
plt.xlabel("Year")
plt.show()


# Here,above fig shows the yearwise number of attacks in w.r.t Region.
# The Most number of attcaks occured in the Middle East & North Africa as well as South Asian area during the year 2010.
