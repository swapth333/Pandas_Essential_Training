#!/usr/bin/env python
# coding: utf-8

# # Pandas Essential Training

# In[ ]:


import pandas as pd


# In[270]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('/Users/swapnilthorat/Desktop/DA/Python/Ex_Files_Pandas_EssT/ExerciseFiles/data/olympics.csv', skiprows=4)


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df['NOC']


# In[57]:


df.NOC


# In[49]:


type(df.NOC)


# In[54]:


df[['Edition','City','Athlete','Medal']]


# In[55]:


type(df[['Edition','City','Athlete','Medal']])


# In[65]:


df.shape


# In[67]:


df.info()


# # Basic Analysis

# Value_counts()

# In[75]:


df.Edition.value_counts(ascending=False)


# In[76]:


df.Gender.value_counts(ascending=True, dropna = False)


# Sort_Values()

# In[77]:


df.sort_values(['Athlete'])


# In[79]:


df.City.sort_values


# In[192]:


df1= df.sort_values(by=['Edition','NOC','Sport','Athlete'])


# In[86]:


df1.head(151)


# Boolean Indexing

# In[88]:


df.Medal=='Gold'


# In[89]:


df[df.Medal=='Gold']


# String Handling
# 1. series.str.contains()
# 2. series.str.startswith()
# 3. series.str.isnumeris()

# In[7]:


df[df.Athlete.str.contains('Florence')]


# In[17]:


djo= df[df.Athlete.str.contains('OWENS')]
djo


# In[19]:


djo.Event.value_counts()


# In[24]:


df.Sport.value_counts()


# In[35]:


bgm = df[(df.Medal == 'Gold') & (df.Gender == 'Men') & (df.Sport == 'Badminton')]
bgm.sort_values(by = 'Athlete')


# In[27]:


df.head()


# In[40]:


df[df.Edition >= 1984].NOC.value_counts().head(5)


# * Display the male Gold medal winners for the 100m track & field sprint event over the years. List the result starting with the most recent. Show the olympic city, edition, athlete and the country they represent. 

# In[46]:


gmh = df[(df.Gender == 'Men') & (df.Medal == 'Gold') & (df.Event == '100m')]
gmh.sort_values('Edition',ascending=False)[['City','Edition','Athlete','NOC']]


# Basic Plotting
# Plot()
# Plot(Kind='line')
# Plot(Kind='bar')
# Plot(Kind='barh')
# Plot(Kind='pie')

# In[48]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# What are the different sports in first olympics, plot them using different graph

# In[50]:


fo = df[(df.Edition == 1896)]
fo.head(10)


# Line Graph

# In[52]:


fo.Sport.value_counts()


# In[53]:


fo.Sport.value_counts().plot()


# In[90]:


fo.Sport.value_counts().plot(kind='bar', colormap='RdBu', figsize=(5,5))


# In[55]:


fo.Sport.value_counts().plot(kind='barh')


# In[56]:


fo.Sport.value_counts().plot(kind='pie')


# In[87]:


fo.NOC.value_counts().plot(kind='pie', colormap='BuPu');


# Countplot()
# 
# -- seaboard.countplot(x=None,y=None,hue=None,data=None,order=None,hue_order=None,orient=None,color=None,palette=None....)

# --data: dataframe or source of data
# 
# --hue: categorical variable
# 
# --order: sequence when using categorical variable 
# 
# --palette: colors to use for the different levels of hue variable

# # When to use
# 
# Matplotlib()
# 
# Short scripts and in conjunction with pyplot 
# 
# simple plot- line bar
# 
# Seaborn()
# 
# dealing with statistical,categorical data,or requirimng more advance plots

# In[94]:


import seaborn as sns


# How many medals have been won by men and women in the History of olympics. How many gold, silver and bronz medals were won for each gender.

# In[97]:


sns.countplot(x='Medal',data=df, hue='Gender')


# In[105]:


chb = df[(df.NOC =='CHN') & (df.Edition ==2008)]
chb


# In[107]:


chb.Gender.value_counts().plot(kind='bar')


# In[108]:


sns.countplot(data=df,x='Gender')


# Indexing

# In[109]:


type(df.index)


# In[111]:


df.index[100]


# set_index()
# 
# dataframe.set_index(keys,drop=True,append=False,implace=False,verify_integrity=False)
# 
# Set dataframes using one or more columns
# 

# In[112]:


df.head()


# In[113]:


df.set_index('Athlete')


# In[114]:


df.head()


# In[115]:


df.set_index('Athlete',inplace=True)


# In[116]:


df.head()


# In[117]:


df.reset_index(inplace=True)


# In[118]:


df.head()


# In[119]:


ath=df.set_index('Athlete')


# In[121]:


ath.head(3)


# In[122]:


ath.reset_index(inplace=True)


# In[123]:


ath.head(3)


# sort_index()
# 
# sort_index(axis=0,level=None,ascending=True,inplace=False....by=None)
# 
# helps during sorting large data

# In[124]:


ath.set_index('Athlete',inplace=True)


# In[125]:


ath.head()


# In[127]:


ath.sort_index(inplace=True,ascending=False)
ath.head()


# loc[]
# 
# label based indexer for selection by label
# 
# loc[] will raise key error when items are not found

# In[130]:


ath.loc['BOLT, Usain']


# In[133]:


ath.reset_index(inplace=True)
ath.head()


# In[137]:


ath.iloc[[1000,1300,1549,2467,5001,10000]]


# In[138]:


df.iloc[[1000,1300,1549,2467,5001,10000]]


# In[142]:


df.iloc[0:6]


# In[ ]:





# Challenge

# In[165]:


df.Edition.value_counts().sort_index().plot(kind='bar', figsize=(14,7))


# In[162]:


from matplotlib import rcParams

# figure size in inches
rcParams['figure.figsize'] = 16,7


# In[163]:


sns.countplot(x='Edition',data=df, hue='Gender')


# groupby

# In[167]:


df.groupby('Edition')


# In[169]:


type(df.groupby('Edition'))


# In[170]:


list(df.groupby('Edition'))


# In[171]:


for group_key, group_value in df.groupby('Edition'):
    print(group_key)
    print(group_value)


# groupby computations

# In[172]:


df.groupby('Edition').size()


# In[173]:


df.groupby('NOC').size()


# In[177]:


df.groupby(['Edition','NOC','Medal']).agg(['count'])


# In[178]:


df.groupby(['Edition','NOC','Medal']).size()


# In[191]:


df.groupby(['NOC','Edition','Sport','Medal']).agg({'Edition': ['count']})


# In[196]:


df.loc[df.Athlete =='LEWIS, Carl'].groupby('Athlete').agg({'Edition': ['min','max','count']})


# Using groupby() function plot the total number of medals awarded at each of the olympic games throughout history.

# In[201]:


df.groupby('Edition').size().plot(kind='bar')


# In[ ]:





# Create a list showing total number of medals won for each country over the history of the olympics. For each country include the year of the first and the most recent olympic medal win. 

# In[205]:


df.groupby(['NOC']).agg({'Edition': ['min','max','count']})


# In[209]:


df.stack()


# In[212]:


r= df.groupby(['NOC']).agg({'Edition': ['min','max','count']}).stack()
r


# In[213]:


r.unstack()


# In[215]:


usg = df[(df.Medal == 'Gold') & (df.NOC == 'USA')]
usg


# In[220]:


usg.Gender.value_counts().plot(kind='bar',figsize=(5,3))


# In[225]:


usg.groupby(['Edition','Gender']).size()


# In[228]:


usg.groupby(['Edition','Gender']).size().unstack('Gender',fill_value=0)


# In[231]:


usg.groupby(['Edition','Gender']).size().unstack('Gender',fill_value=0).plot(figsize=(8,5))


# In[240]:


gold = df.groupby(['Athlete','Medal']).size().unstack('Medal',fill_value=0)
gold


# In[248]:


gold.sort_values(['Gold','Silver','Bronze'], 
                 ascending=False)[['Gold','Silver','Bronze']].head(5).plot(kind='bar', 
                                                                           figsize=(8,5))


# In[258]:


fg= df.groupby(['NOC','Medal']).size().unstack('Medal',fill_value=0)[['Gold','Silver','Bronze']]
fg1=fg.sort_values(['Gold','Silver','Bronze'],ascending=False).transpose()
fg1


# In[260]:


df.head(5)


# In[261]:


lo = df[df.Edition==2008]
lo


# In[262]:


lo1= lo.groupby(['NOC','Medal']).size().unstack('Medal',fill_value=0)[['Gold','Silver','Bronze']]
lo2=lo1.sort_values(['Gold','Silver','Bronze'],ascending=False).transpose()
lo2


# In[267]:


sns.heatmap(lo2)


# In[276]:


plt.figure(figsize=(16,5))
sns.heatmap(lo2,cmap="BuPu")


# In[285]:


gold = df.groupby(['Athlete','Medal']).size().unstack('Medal',fill_value=0)
gold
gold.sort_values(['Gold','Silver','Bronze'], ascending=False)[['Gold','Silver','Bronze']].head(5).plot(kind='bar', 
                                                                           figsize=(8,5))


# In[287]:


from matplotlib.colors import ListedColormap


# In[288]:


sns.color_palette()


# In[289]:


sns.palplot(sns.color_palette())


# In every olympics which US athlete has won most total number of medals? Include the athletes discipline.

# In[327]:


us=df[df.NOC=='USA']
us


# In[328]:


us1 = us.groupby(['Edition','Athlete','Medal']).size().unstack('Medal',fill_value=0)

us1


# In[329]:


us1['Total'] = us1['Gold'] + us1['Silver'] + us1['Bronze']


# In[330]:


us1


# In[337]:


us2 = us1.sort_values(['Edition'])
us2.reset_index(inplace=True)
us2


# In[ ]:





# In[ ]:




