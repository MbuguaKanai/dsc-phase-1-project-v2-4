#!/usr/bin/env python
# coding: utf-8

# ## Final Project Submission
# 
# Please fill out:
# * Student name: Antony Kanai
# * Student pace: full time
# * Scheduled project review date/time: 
# * Instructor name: Noah Kandie
# * Blog post URL:
# 

# # Project Overview
# My task is to use explorative data analysis to analyze the movies dataset and recommend the course of action to be taken by Microsoft corportion
# 
# ## Objectives
# 
# 1. Ascertain the most popular genre of movies
# 2. Establish the most popular publisher
# 3. Ascertain the  most popular rating for movies
# 4. Ascertain the relationship bwtween production budget and  profit realized from the movies

# ## Business Understanding
# 
# Microsoft sees all the big companies creating original video content and they want to get in on the fun. They have decided to create a new movie studio, but they don’t know anything about creating movies.

# # Data Understanding

# Before, I start the process of understanding my data,  I first import  the relevant librares that will enbale me read all my datasets.
# 
# These are Pandas,Sqlite and numpy

# In[5]:


import pandas as pd
import sqlite3
import numpy as np
import warnings


# The next step is reading and having a feel of the datasets.
# 
# 
# I begin with connecting to the database and viewing the tables  in the database
# 
# 
# ## im.db

# In[79]:


conn = sqlite3.connect('im.db') # Establishing connection to the database
data = pd.read_sql_query('SELECT name from sqlite_master where type= "table";',conn) # Viewing the tables in the database
data


#  ## bom.movie_gross.csv

# In[4]:


bomovies_df = pd.read_csv("zippedData/bom.movie_gross.csv.gz") # reading the database
bomovies_df.head(2) # viewing the first two entries


# In[ ]:


bomovies_df.info() # getting to know the number of entiries and columns and the datatypes of the coulumns


# ## rt.movie_info.tsv.gz"

# In[6]:


rt_df = pd.read_csv(("zippedData/rt.movie_info.tsv.gz"),delimiter = "\t") # reading the tsv data and assigning it to rt_df.
rt_df.head(3) #viewing the first three entries


# In[7]:


rt_df.info() #getting to know the number of rows and columns and the datatypes of the coulumns


# ## rt.reviews.tsv.gz

# In[12]:


# reading the data and assigning it to rv_df

rv_df = pd.read_csv(("zippedData/rt.reviews.tsv.gz"), delimiter = "\t", encoding = "Windows 1252") 

rv_df.tail(3) # viewing the last 3 entries


# In[86]:


rv_df.info() 


# ## tmdb.movies.csv.gz

# In[10]:


tmbd_df = pd.read_csv("zippedData/tmdb.movies.csv.gz") # Reading the tmdb data

tmbd_df.head(2) # viewing the first two entries


# In[ ]:


tmbd_df.info()


# ## tn.movie_budgets.csv.gz

# In[9]:


budgets= pd.read_csv("zippedData/tn.movie_budgets.csv.gz") 
budgets.head(2)


# In[ ]:


budgets.info()


# # Data Preparation

# After having a brief overview of the dataset, I started the data prepaation process  which invloved cleaning of the data with he following objectives:
# 
# 1. Deal with the NaNs/ or missing data
# 2. Ensure that all columns are in the correct datatype
# 3. Deal with placeholders if any
# 
# In the cells taht follow i will conduct data cleaning and ETL  for each of the dataset.

# ## bomovies_df

# 
# #### Dealing with missing Values
# 
# The first step is to find the proportion of missing  values in each of the  columns of the bomovies_df

# In[13]:


bomovies_df.isnull().mean()*100


# From the results above, it seems that in the bomovies_df the proportion of missing values for all the columns except the foreign_gross is quite low at less than 1%. 
# 
# However for foreign gross, the missing value percentage  is almost 40%.
# I assumed that the missing values in foreign_gross means that the movies were sold domestically and did not reach the international market hence their revenue from the international market is 0. Therefore,  I replace the missing values in the foreign_gross column by 0.
#  
# I also replaced missing values in domestic_gross column with zero since i assummed that these movies  did not sell  in the domestic market

# The codes below  replaces the Nans  with 0 in the columns domestic_gross and foreign_gross respectively.
# 

# In[14]:


bomovies_df["domestic_gross"].fillna(0, inplace= True) # replaces all NANs in the domestic_gross columns with 0
bomovies_df["foreign_gross"].fillna(0, inplace= True) # replaces all NANs in the foreign_gross columns with 0


# In[15]:


bomovies_df.isna().mean() # Check if the Nulls have disappeared.


# For the  studio column I replaced the missing values with the mode, which is the most occuring studio. 
# 
# To find the most occuring studio I used the following code:

# In[16]:


bomovies_df["studio"].value_counts().nlargest(1) # Checking for the most common studio


# Since IFC is the most common studio, i replaced the missing values in the studio column with it

# In[17]:


bomovies_df["studio"].fillna("IFC",inplace=True) # replacing missing values in studio column with IFC.
bomovies_df.isna().mean() # checking if the nulls have disappeared


# I have now dealt with the missing values in the bomovies_df succesfully. 
# 
# #### Converting to the appropriate column datatypes
# However, i I realized domestic-gross and foreign gross and year are in the  wrong datatype  and  therefore i cast them to the correct datatype

# In[20]:


bomovies_df = bomovies_df = bomovies_df.astype({"domestic_gross": int})


# In[21]:


bomovies_df.info() # checking column dataypes have converted succesfull


# ## rt_df

# #### Dealing with missing values in rt_df

# In[22]:


rt_df.isna().mean()*100 # First find the proportion of missing  values in rt_df


# #### Dealing with the nulls;
#  In the dataframe rt_df,  i realized that only to columns would be important for my analysis. These are the genre and rating columns.
#  I sliced them from the main datframe as follows:
# 

# In[80]:


rt_df = rt_df[["genre", "rating"]] # to  slice relevant columns from the rt_df dataframe
rt_df.head(2)


# I then dealt with the missing values by droppping the rows that had missing values in the column

# In[24]:


rt_df = rt_df.dropna()


# In[25]:


rt_df.isna().mean()*100


# ## rv_df

# #### Deal with the  missing values by  dropping all null vlaues in the rows

# In[26]:


rv_df.dropna(inplace =True) # dropping rows with missing values


# In[27]:


rv_df.isnull().mean()*100 # checking if the nulls have disappeared.


# The ratings column in the rt_reviews (rv_df) can be split into two columns so that we can be able to standardize ratings of all the enries throough feature engineering. The next cell splits the rating column ito two and displays them as separate columns 
# 
# 

# In[ ]:





# In[28]:


new = rv_df["rating"].str.split(pat ="/", n = 1, expand=True) # splitting the ratin
rv_df["score"] = new[0]
rv_df["outof"] = new[1]
rv_df.drop(columns = ["rating"], inplace = True)
rv_df


# In[ ]:



    


# Before I standardize the ratings, i willl first convert the column types from  string to integer to allow for mathematical computation.

# In[ ]:





# ## tmbd_df

# #### Check fo missing values

# In[81]:


tmbd_df.isna().mean()*100 # checking proportion of missing values


# Perfect! This data has no any missing value.

# In[30]:


tmbd_df["genre_ids"].value_counts() # check for  unique values of Genre_ids


# In[ ]:





# ## budgets_df

# Check for missing values

# In[ ]:


budgets.isna().mean()*100  #checks for percentage of missing values. 


# The budgets_df is also complete!

# Since the domestic_gross,Production_budget and Worldwide_gross columns are strings, we needto convet them to inerger to faciltate feature engineering to make the data more insightful. 

# In[31]:


#The codes below convert  the columns with the $ sign into interger to facilitate feature engineering 

budgets['domestic_gross'] = budgets['domestic_gross'].apply(lambda x: int(''.join(filter(str.isdigit, x))))
budgets['production_budget'] = budgets['production_budget'].apply(lambda x: int(''.join(filter(str.isdigit, x))))
budgets["worldwide_gross"] = budgets['worldwide_gross'].apply(lambda x: int(''.join(filter(str.isdigit, x))))


# Perfect! since we have our budget and gross columns as  intergers, it is possibe to create new  profit columns. Pofit is the difference between productioin cost and gross revenue

# In[32]:


budgets["Domestic_profit"] = budgets["domestic_gross"]- budgets["production_budget"]  # creates a new column Domestic_profit


# In[33]:


budgets["worldwide_profit"] = budgets["worldwide_gross"]-budgets["production_budget"]
budgets.info()  # checkig if  we have the correct datatypes


# # Data Analysis

# After prepaing the data and making sure that it is not dirty,  I delved into data analysis. In thi section i will try to make sense of the data. I will ty to merge datasets to come up with more insightful analysis and to create a story that microsoft would definitely buy in.

#  My Data  Analysis will focus on Establishing the  following:
#  
#  1. Which is the  most popular genre of movies
#  2. Which is the most popular studio 
#  3. Which rating  is most prefered
#  4. wh
#  

# ### Most popular Genre of Movies 
# 

# From the rt_ movies dataset I can establish the  top 5 genres of movies

# In[34]:


rt_df.genre.value_counts().nlargest(5) 


# From the above code, the most popular genre of movies  is Drama, followed by Comedy, then comedy|Drama  and so on...
# This can be better presetnteed in the visualization below:

# In[35]:


import matplotlib.pyplot as plt # Importing the library neccesaty to create visualizations
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[36]:


# Getting the X and Y  values 
x = rt_df["genre"].value_counts().head().index.tolist()
y = list(rt_df["genre"].value_counts().nlargest(5))   



# In[37]:


# Ploting  Most popular  Genres and their frequencies
fig,ax = plt.subplots(figsize = (10,5))
plt.bar(x, y, color = "Purple", width = 0.5)
plt.xticks(rotation = 10);
plt.title(" Five Most Popular Movie Genres", fontsize = 20, fontweight = "bold");


# ### Most Popular studio

# I can be able to find the most popular studio from the bomovies _df

# In[ ]:


rt_df["rating"].value_counts()


# These can be visually presented as:

# In[38]:


rating= rt_df["rating"].value_counts().head().index.tolist()
frequency=list(rt_df["rating"].value_counts().nlargest(5))


# In[39]:


fig, ax = plt.subplots(figsize= (10,6))
                       
plt.bar(rating, frequency, color = "green", width =0.5); # plotting ratings and their frequencies.

plt.title("Most Popular Rating", fontsize = 14, fontweight = "bold");


# ### Most Popular Rating 

# ### Is There a Relationship Bewteen Movie Prodcuction Budget and Profits Realised

# Inorder to ascertain whether production budget affects profitability, I calculated correlation betweem production budget and profit realised domestically and worldwide

# In[40]:


budgets.corr()


# In the correlation matrix above, 
# The correlation between Production budget  and worldwide_profit is positive and higgher than that between prodcution budget and domestic profit.
# Below is scatter plot showing the relationsip 

# In[82]:


sns.set_style("darkgrid")
fig, axes = plt.subplots(1,2,figsize= (15,5))
sns.scatterplot(x= budgets["production_budget"], y =budgets["Domestic_profit"], data = budgets, ax= axes[0])
sns.scatterplot(x= budgets["production_budget"], y =budgets["worldwide_profit"], data = budgets, ax= axes[1]); # plotting scatter plots  between prodcution_budget and profits



# In[ ]:


sns.set_style("darkgrid")
fig, axes = plt.subplots(1,2,figsize= (15,5))
sns.scatterplot(x= budgets["production_budget"], y =budgets["domestic_gross"], data = budgets, ax= axes[0])
sns.scatterplot(x= budgets["production_budget"], y =budgets["worldwide_gross"], data = budgets, ax= axes[1]);



# ### Most Popular  Genre_ids

# In[84]:


# grouping by genre-ids and aggregating by max()

grouped1= tmbd_df.groupby(["genre_ids"]).max().sort_values(by="popularity", ascending= False)
grouped1.head()


# ### Popularity By Language

# In[85]:


# Grouping by  Original _language
grouped = tmbd_df.groupby(["original_language"]).sum().sort_values(by="popularity", ascending= False) 
grouped.head()


# In[63]:


language =  ["en","fr","ja","es", "ru"]
Popularity= [71896,2155,1513,1257,708]


# In[60]:


grouped["popularity"].head()


# In[72]:


fig,ax = plt.subplots()
plt.pie(Popularity, labels = language)
plt.title("Most Prefered Languages");


# ### Merging Datasets

# In[83]:


Merged_df= pd.merge(rv_df, budgets) #Merging datasets with common columns
Merged_df.head()


# In[ ]:





# In[77]:


publisher= Merged_df["publisher"].value_counts().head().index.tolist()
frequncy=list(Merged_df["publisher"].value_counts().nlargest(5))
sns.barplot(x=publisher, y = frequncy, data = Merged_df, palette='OrRd')
plt.xticks(rotation = 30);
plt.title("TOP PUBLISHERS");


# ###  Summary

#  The Visualizations above inform how microsoft will begin their movie-Production journey. With the insights we can be sure that Microsoft wil get it right in data analysis

# In[ ]:




