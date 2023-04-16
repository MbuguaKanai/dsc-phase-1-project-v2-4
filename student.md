## Final Project Submission

Please fill out:
* Student name: Antony Kanai
* Student pace: full time
* Scheduled project review date/time: 
* Instructor name: Noah Kandie
* Blog post URL:


# Project Overview
My task is to use explorative data analysis to analyze the movies dataset and recommend the course of action to be taken by Microsoft corportion

## Objectives

1. Ascertaain the most popular genre of movies
2. Establish the most popular publisher
3. Ascertain the  most popular rating for movies
4. Ascertain the relationship bwtween production budget and  profit realized from the movies

## Business Understanding

Microsoft sees all the big companies creating original video content and they want to get in on the fun. They have decided to create a new movie studio, but they don’t know anything about creating movies.

# Data Understanding

Before, I start the process of understanding my data,  I first import  the relevant librares that will enbale me read all my datasets.

These are Pandas,Sqlite and numpy


```python
import pandas as pd
import sqlite3
import numpy as np
import warnings
```

The next step is reading and having a feel of the datasets.


I begin with connecting to the database and viewing the tables  in the database


## im.db


```python

conn = sqlite3.connect('im.db') # Establishing connection to the database
data = pd.read_sql_query('SELECT name from sqlite_master where type= "table";',conn) # Viewing the tables in the database
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



 ## bom.movie_gross.csv


```python
bomovies_df = pd.read_csv("zippedData/bom.movie_gross.csv.gz") # reading the database
bomovies_df.head(2) # viewing the first two entries
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>studio</th>
      <th>domestic_gross</th>
      <th>foreign_gross</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Toy Story 3</td>
      <td>BV</td>
      <td>415000000.0</td>
      <td>652000000</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alice in Wonderland (2010)</td>
      <td>BV</td>
      <td>334200000.0</td>
      <td>691300000</td>
      <td>2010</td>
    </tr>
  </tbody>
</table>
</div>




```python
bomovies_df.info() # getting to know the number of entiries and columns and the datatypes of the coulumns
```

## rt.movie_info.tsv.gz"


```python
rt_df = pd.read_csv(("zippedData/rt.movie_info.tsv.gz"),delimiter = "\t") # reading the tsv data and assigning it to rt_df.
rt_df.head(3) #viewing the first three entries
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>synopsis</th>
      <th>rating</th>
      <th>genre</th>
      <th>director</th>
      <th>writer</th>
      <th>theater_date</th>
      <th>dvd_date</th>
      <th>currency</th>
      <th>box_office</th>
      <th>runtime</th>
      <th>studio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>This gritty, fast-paced, and innovative police...</td>
      <td>R</td>
      <td>Action and Adventure|Classics|Drama</td>
      <td>William Friedkin</td>
      <td>Ernest Tidyman</td>
      <td>Oct 9, 1971</td>
      <td>Sep 25, 2001</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>104 minutes</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>New York City, not-too-distant-future: Eric Pa...</td>
      <td>R</td>
      <td>Drama|Science Fiction and Fantasy</td>
      <td>David Cronenberg</td>
      <td>David Cronenberg|Don DeLillo</td>
      <td>Aug 17, 2012</td>
      <td>Jan 1, 2013</td>
      <td>$</td>
      <td>600,000</td>
      <td>108 minutes</td>
      <td>Entertainment One</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>Illeana Douglas delivers a superb performance ...</td>
      <td>R</td>
      <td>Drama|Musical and Performing Arts</td>
      <td>Allison Anders</td>
      <td>Allison Anders</td>
      <td>Sep 13, 1996</td>
      <td>Apr 18, 2000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>116 minutes</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
rt_df.info() #getting to know the number of rows and columns and the datatypes of the coulumns
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1560 entries, 0 to 1559
    Data columns (total 12 columns):
     #   Column        Non-Null Count  Dtype 
    ---  ------        --------------  ----- 
     0   id            1560 non-null   int64 
     1   synopsis      1498 non-null   object
     2   rating        1557 non-null   object
     3   genre         1552 non-null   object
     4   director      1361 non-null   object
     5   writer        1111 non-null   object
     6   theater_date  1201 non-null   object
     7   dvd_date      1201 non-null   object
     8   currency      340 non-null    object
     9   box_office    340 non-null    object
     10  runtime       1530 non-null   object
     11  studio        494 non-null    object
    dtypes: int64(1), object(11)
    memory usage: 146.4+ KB
    

## rt.reviews.tsv.gz


```python
# reading the data and assigning it to rv_df

rv_df = pd.read_csv(("zippedData/rt.reviews.tsv.gz"), delimiter = "\t", encoding = "Windows 1252") 

rv_df.tail(3) # viewing the last 3 entries
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>review</th>
      <th>rating</th>
      <th>fresh</th>
      <th>critic</th>
      <th>top_critic</th>
      <th>publisher</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54429</th>
      <td>2000</td>
      <td>NaN</td>
      <td>2/5</td>
      <td>rotten</td>
      <td>Emanuel Levy</td>
      <td>0</td>
      <td>EmanuelLevy.Com</td>
      <td>July 17, 2005</td>
    </tr>
    <tr>
      <th>54430</th>
      <td>2000</td>
      <td>NaN</td>
      <td>2.5/5</td>
      <td>rotten</td>
      <td>Christopher Null</td>
      <td>0</td>
      <td>Filmcritic.com</td>
      <td>September 7, 2003</td>
    </tr>
    <tr>
      <th>54431</th>
      <td>2000</td>
      <td>NaN</td>
      <td>3/5</td>
      <td>fresh</td>
      <td>Nicolas Lacroix</td>
      <td>0</td>
      <td>Showbizz.net</td>
      <td>November 12, 2002</td>
    </tr>
  </tbody>
</table>
</div>




```python
rv_df.info() 
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[11], line 1
    ----> 1 rv_df.info()
    

    NameError: name 'rv_df' is not defined


## tmdb.movies.csv.gz


```python
tmbd_df = pd.read_csv("zippedData/tmdb.movies.csv.gz") # Reading the tmdb data

tmbd_df.head(2) # viewing the first two entries
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>genre_ids</th>
      <th>id</th>
      <th>original_language</th>
      <th>original_title</th>
      <th>popularity</th>
      <th>release_date</th>
      <th>title</th>
      <th>vote_average</th>
      <th>vote_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>[12, 14, 10751]</td>
      <td>12444</td>
      <td>en</td>
      <td>Harry Potter and the Deathly Hallows: Part 1</td>
      <td>33.533</td>
      <td>2010-11-19</td>
      <td>Harry Potter and the Deathly Hallows: Part 1</td>
      <td>7.7</td>
      <td>10788</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>[14, 12, 16, 10751]</td>
      <td>10191</td>
      <td>en</td>
      <td>How to Train Your Dragon</td>
      <td>28.734</td>
      <td>2010-03-26</td>
      <td>How to Train Your Dragon</td>
      <td>7.7</td>
      <td>7610</td>
    </tr>
  </tbody>
</table>
</div>




```python
tmbd_df.info()
```

## tn.movie_budgets.csv.gz


```python
budgets= pd.read_csv("zippedData/tn.movie_budgets.csv.gz") 
budgets.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>release_date</th>
      <th>movie</th>
      <th>production_budget</th>
      <th>domestic_gross</th>
      <th>worldwide_gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Dec 18, 2009</td>
      <td>Avatar</td>
      <td>$425,000,000</td>
      <td>$760,507,625</td>
      <td>$2,776,345,279</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>May 20, 2011</td>
      <td>Pirates of the Caribbean: On Stranger Tides</td>
      <td>$410,600,000</td>
      <td>$241,063,875</td>
      <td>$1,045,663,875</td>
    </tr>
  </tbody>
</table>
</div>




```python
budgets.info()
```

# Data Preparation

After having a brief overview of the dataset, I started the data prepaation process  which invloved cleaning of the data with he following objectives:

1. Deal with the NaNs/ or missing data
2. Ensure that all columns are in the correct datatype
3. Deal with placeholders if any

In the cells taht follow i will conduct data cleaning and ETL  for each of the dataset.

## bomovies_df


#### Dealing with missing Values

The first step is to find the proportion of missing  values in each of the  columns of the bomovies_df


```python
bomovies_df.isnull().mean()*100
```




    title              0.000000
    studio             0.147623
    domestic_gross     0.826690
    foreign_gross     39.858282
    year               0.000000
    dtype: float64



From the results above, it seems that in the bomovies_df the proportion of missing values for all the columns except the foreign_gross is quite low at less than 1%. 

However for foreign gross, the missing value percentage  is almost 40%.
I assumed that the missing values in foreign_gross means that the movies were sold domestically and did not reach the international market hence their revenue from the international market is 0. Therefore,  I replace the missing values in the foreign_gross column by 0.
 
I also replaced missing values in domestic_gross column with zero since i assummed that these movies  did not sell  in the domestic market

The codes below  replaces the Nans  with 0 in the columns domestic_gross and foreign_gross respectively.



```python
bomovies_df["domestic_gross"].fillna(0, inplace= True) # replaces all NANs in the domestic_gross columns with 0
bomovies_df["foreign_gross"].fillna(0, inplace= True) # replaces all NANs in the foreign_gross columns with 0
```


```python
bomovies_df.isna().mean() # Check if the Nulls have disappeared.

```




    title             0.000000
    studio            0.001476
    domestic_gross    0.000000
    foreign_gross     0.000000
    year              0.000000
    dtype: float64



For the  studio column I replaced the missing values with the mode, which is the most occuring studio. 

To find the most occuring studio I used the following code:


```python
bomovies_df["studio"].value_counts().nlargest(1) # Checking for the most common studio
```




    IFC    166
    Name: studio, dtype: int64



Since IFC is the most common studio, i replaced the missing values in the studio column with it


```python
bomovies_df["studio"].fillna("IFC",inplace=True) # replacing missing values in studio column with IFC.
bomovies_df.isna().mean() # checking if the nulls have disappeared
```




    title             0.0
    studio            0.0
    domestic_gross    0.0
    foreign_gross     0.0
    year              0.0
    dtype: float64



I have now dealt with the missing values in the bomovies_df succesfully. 

#### Converting to the appropriate column datatypes
However, i I realized domestic-gross and foreign gross and year are in the  wrong datatype  and  therefore i cast them to the correct datatype


```python
bomovies_df = bomovies_df = bomovies_df.astype({"domestic_gross": int})

```


```python
bomovies_df.info() # checking column dataypes have converted succesfull
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3387 entries, 0 to 3386
    Data columns (total 5 columns):
     #   Column          Non-Null Count  Dtype 
    ---  ------          --------------  ----- 
     0   title           3387 non-null   object
     1   studio          3387 non-null   object
     2   domestic_gross  3387 non-null   int32 
     3   foreign_gross   3387 non-null   object
     4   year            3387 non-null   int64 
    dtypes: int32(1), int64(1), object(3)
    memory usage: 119.2+ KB
    

## rt_df

#### Dealing with missing values in rt_df


```python
rt_df.isna().mean()*100 # First find the proportion of missing  values in rt_df
```




    id               0.000000
    synopsis         3.974359
    rating           0.192308
    genre            0.512821
    director        12.756410
    writer          28.782051
    theater_date    23.012821
    dvd_date        23.012821
    currency        78.205128
    box_office      78.205128
    runtime          1.923077
    studio          68.333333
    dtype: float64



#### Dealing with the nulls;
 In the dataframe rt_df,  i realized that only to columns would be important for my analysis. These are the genre and rating columns.
 I sliced them from the main datframe as follows:



```python
rt_df = rt_df[["genre", "rating"]]
rt_df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>genre</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Action and Adventure|Classics|Drama</td>
      <td>R</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Drama|Science Fiction and Fantasy</td>
      <td>R</td>
    </tr>
  </tbody>
</table>
</div>



I then dealt with the missing values by droppping the rows that had missing values in the column


```python
rt_df = rt_df.dropna()
```


```python
rt_df.isna().mean()*100
```




    genre     0.0
    rating    0.0
    dtype: float64



## rv_df

#### Deal with the  missing values by  dropping all null vlaues in the rows


```python
rv_df.dropna(inplace =True) # dropping rows with missing values
```


```python
rv_df.isnull().mean()*100 # checking if the nulls have disappeared.
```




    id            0.0
    review        0.0
    rating        0.0
    fresh         0.0
    critic        0.0
    top_critic    0.0
    publisher     0.0
    date          0.0
    dtype: float64



The ratings column in the rt_reviews (rv_df) can be split into two columns so that we can be able to standardize ratings of all the enries throough feature engineering. The next cell splits the rating column ito two and displays them as separate columns 




```python

```


```python
new = rv_df["rating"].str.split(pat ="/", n = 1, expand=True) # splitting the ratin
rv_df["score"] = new[0]
rv_df["outof"] = new[1]
rv_df.drop(columns = ["rating"], inplace = True)
rv_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>review</th>
      <th>fresh</th>
      <th>critic</th>
      <th>top_critic</th>
      <th>publisher</th>
      <th>date</th>
      <th>score</th>
      <th>outof</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>A distinctly gallows take on contemporary fina...</td>
      <td>fresh</td>
      <td>PJ Nabarro</td>
      <td>0</td>
      <td>Patrick Nabarro</td>
      <td>November 10, 2018</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>Quickly grows repetitive and tiresome, meander...</td>
      <td>rotten</td>
      <td>Eric D. Snider</td>
      <td>0</td>
      <td>EricDSnider.com</td>
      <td>July 17, 2013</td>
      <td>C</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>Cronenberg is not a director to be daunted by ...</td>
      <td>rotten</td>
      <td>Matt Kelemen</td>
      <td>0</td>
      <td>Las Vegas CityLife</td>
      <td>April 21, 2013</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>While not one of Cronenberg's stronger films, ...</td>
      <td>fresh</td>
      <td>Emanuel Levy</td>
      <td>0</td>
      <td>EmanuelLevy.Com</td>
      <td>February 3, 2013</td>
      <td>B-</td>
      <td>None</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3</td>
      <td>Robert Pattinson works mighty hard to make Cos...</td>
      <td>rotten</td>
      <td>Christian Toto</td>
      <td>0</td>
      <td>Big Hollywood</td>
      <td>January 15, 2013</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>54419</th>
      <td>2000</td>
      <td>Sleek, shallow, but frequently amusing.</td>
      <td>fresh</td>
      <td>Gene Seymour</td>
      <td>1</td>
      <td>Newsday</td>
      <td>September 27, 2002</td>
      <td>2.5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>54420</th>
      <td>2000</td>
      <td>The spaniel-eyed Jean Reno infuses Hubert with...</td>
      <td>fresh</td>
      <td>Megan Turner</td>
      <td>1</td>
      <td>New York Post</td>
      <td>September 27, 2002</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>54421</th>
      <td>2000</td>
      <td>Manages to be somewhat well-acted, not badly a...</td>
      <td>rotten</td>
      <td>Bob Strauss</td>
      <td>0</td>
      <td>Los Angeles Daily News</td>
      <td>September 27, 2002</td>
      <td>1.5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>54422</th>
      <td>2000</td>
      <td>Arguably the best script that Besson has writt...</td>
      <td>fresh</td>
      <td>Wade Major</td>
      <td>0</td>
      <td>Boxoffice Magazine</td>
      <td>September 27, 2002</td>
      <td>3.5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>54424</th>
      <td>2000</td>
      <td>Dawdles and drags when it should pop; it doesn...</td>
      <td>rotten</td>
      <td>Manohla Dargis</td>
      <td>1</td>
      <td>Los Angeles Times</td>
      <td>September 26, 2002</td>
      <td>1.5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>33988 rows × 9 columns</p>
</div>




```python

    
```

Before I standardize the ratings, i willl first convert the column types from  string to integer to allow for mathematical computation.


```python

```

## tmbd_df

#### Check fo missing values


```python
tmbd_df.isna().mean()*100
```




    Unnamed: 0           0.0
    genre_ids            0.0
    id                   0.0
    original_language    0.0
    original_title       0.0
    popularity           0.0
    release_date         0.0
    title                0.0
    vote_average         0.0
    vote_count           0.0
    dtype: float64



Perfect! This data has no any missing value.


```python
tmbd_df["genre_ids"].value_counts() # check for  unique values of Genre_ids
```




    [99]                       3700
    []                         2479
    [18]                       2268
    [35]                       1660
    [27]                       1145
                               ... 
    [37, 12]                      1
    [10752, 878]                  1
    [28, 53, 10749, 18, 35]       1
    [99, 80, 53, 36]              1
    [10751, 12, 28]               1
    Name: genre_ids, Length: 2477, dtype: int64




```python

```

## budgets_df

Check for missing values


```python
budgets.isna().mean()*100  #checks for percentage of missing values. 
```

The budgets_df is also complete!

Since the domestic_gross,Production_budget and Worldwide_gross columns are strings, we needto convet them to inerger to faciltate feature engineering to make the data more insightful. 


```python
#The codes below convert  the columns with the $ sign into interger to facilitate feature engineering 

budgets['domestic_gross'] = budgets['domestic_gross'].apply(lambda x: int(''.join(filter(str.isdigit, x))))
budgets['production_budget'] = budgets['production_budget'].apply(lambda x: int(''.join(filter(str.isdigit, x))))
budgets["worldwide_gross"] = budgets['worldwide_gross'].apply(lambda x: int(''.join(filter(str.isdigit, x))))

```

Perfect! since we have our budget and gross columns as  intergers, it is possibe to create new  profit columns. Pofit is the difference between productioin cost and gross revenue


```python
budgets["Domestic_profit"] = budgets["domestic_gross"]- budgets["production_budget"]  # creates a new column Domestic_profit

```


```python
budgets["worldwide_profit"] = budgets["worldwide_gross"]-budgets["production_budget"]
budgets.info()  # checkig if  we have the correct datatypes
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5782 entries, 0 to 5781
    Data columns (total 8 columns):
     #   Column             Non-Null Count  Dtype 
    ---  ------             --------------  ----- 
     0   id                 5782 non-null   int64 
     1   release_date       5782 non-null   object
     2   movie              5782 non-null   object
     3   production_budget  5782 non-null   int64 
     4   domestic_gross     5782 non-null   int64 
     5   worldwide_gross    5782 non-null   int64 
     6   Domestic_profit    5782 non-null   int64 
     7   worldwide_profit   5782 non-null   int64 
    dtypes: int64(6), object(2)
    memory usage: 361.5+ KB
    

# Data Analysis

After prepaing the data and making sure that it is not dirty,  I delved into data analysis. In thi section i will try to make sense of the data. I will ty to merge datasets to come up with more insightful analysis and to create a story that microsoft would definitely buy in.

 My Data  Analysis will focus on Establishing the  following:
 
 1. Which is the  most popular genre of movies
 2. Which is the most popular studio 
 3. Which rating  is most prefered
 4. wh
 

### Most popular Genre of Movies 


From the rt_ movies dataset I can establish the  top 5 genres of movies


```python
rt_df.genre.value_counts().nlargest(5)
```




    Drama                                151
    Comedy                               110
    Comedy|Drama                          80
    Drama|Mystery and Suspense            67
    Art House and International|Drama     62
    Name: genre, dtype: int64



From the above code, the most popular genre of movies  is Drama, followed by Comedy, then comedy|Drama  and so on...
This can be better presetnteed in the visualization below:


```python

import matplotlib.pyplot as plt # Importing the library neccesaty to create visualizations
%matplotlib inline
import seaborn as sns

```


```python
# Getting the X and Y  values 
x = rt_df["genre"].value_counts().head().index.tolist()
y = list(rt_df["genre"].value_counts().nlargest(5))   


```


```python
# Ploting  Most popular  Genres and their frequencies
fig,ax = plt.subplots(figsize = (10,5))
plt.bar(x, y, color = "Purple", width = 0.5)
plt.xticks(rotation = 10);
plt.title(" Five Most Popular Movie Genres", fontsize = 20, fontweight = "bold");
```


    
![png](output_81_0.png)
    


### Most Popular studio

I can be able to find the most popular studio from the bomovies _df


```python
rt_df["rating"].value_counts()
```

These can be visually presented as:


```python
rating= rt_df["rating"].value_counts().head().index.tolist()
frequency=list(rt_df["rating"].value_counts().nlargest(5))
```


```python
fig, ax = plt.subplots(figsize= (10,6))
                       
plt.bar(rating, frequency, color = "green", width =0.5);

plt.title("Most Popular Rating", fontsize = 14, fontweight = "bold");

```


    
![png](output_87_0.png)
    


### Most Popular Rating 

### Is There a Relationship Bewteen Movie Prodcuction Budget and Profits Realised

Inorder to ascertain whether production budget affects profitability, I calculated correlation betweem production budget and profit realised domestically and worldwide


```python
budgets.corr()
```

    C:\Users\user\AppData\Local\Temp\ipykernel_10264\2354375143.py:1: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
      budgets.corr()
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>production_budget</th>
      <th>domestic_gross</th>
      <th>worldwide_gross</th>
      <th>Domestic_profit</th>
      <th>worldwide_profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id</th>
      <td>1.000000</td>
      <td>-0.035278</td>
      <td>0.008255</td>
      <td>-0.009422</td>
      <td>0.040832</td>
      <td>-0.001172</td>
    </tr>
    <tr>
      <th>production_budget</th>
      <td>-0.035278</td>
      <td>1.000000</td>
      <td>0.685682</td>
      <td>0.748306</td>
      <td>0.099742</td>
      <td>0.608752</td>
    </tr>
    <tr>
      <th>domestic_gross</th>
      <td>0.008255</td>
      <td>0.685682</td>
      <td>1.000000</td>
      <td>0.938853</td>
      <td>0.792663</td>
      <td>0.926605</td>
    </tr>
    <tr>
      <th>worldwide_gross</th>
      <td>-0.009422</td>
      <td>0.748306</td>
      <td>0.938853</td>
      <td>1.000000</td>
      <td>0.656626</td>
      <td>0.981811</td>
    </tr>
    <tr>
      <th>Domestic_profit</th>
      <td>0.040832</td>
      <td>0.099742</td>
      <td>0.792663</td>
      <td>0.656626</td>
      <td>1.000000</td>
      <td>0.756767</td>
    </tr>
    <tr>
      <th>worldwide_profit</th>
      <td>-0.001172</td>
      <td>0.608752</td>
      <td>0.926605</td>
      <td>0.981811</td>
      <td>0.756767</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



In the correlation matrix above, 
The correlation between Production budget  and worldwide_profit is positive and higgher than that between prodcution budget and domestic profit.
Below is scatter plot showing the relationsip 


```python
sns.set_style("darkgrid")
fig, axes = plt.subplots(1,2,figsize= (15,5))
sns.scatterplot(x= budgets["production_budget"], y =budgets["Domestic_profit"], data = budgets, ax= axes[0])
sns.scatterplot(x= budgets["production_budget"], y =budgets["worldwide_profit"], data = budgets, ax= axes[1]);


```


    
![png](output_93_0.png)
    



```python
sns.set_style("darkgrid")
fig, axes = plt.subplots(1,2,figsize= (15,5))
sns.scatterplot(x= budgets["production_budget"], y =budgets["domestic_gross"], data = budgets, ax= axes[0])
sns.scatterplot(x= budgets["production_budget"], y =budgets["worldwide_gross"], data = budgets, ax= axes[1]);


```

### Most Popular  Genre_ids

This insight can be obtained 


```python
grouped1= tmbd_df.groupby(["genre_ids"]).max().sort_values(by="popularity", ascending= False)
grouped1.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>id</th>
      <th>original_language</th>
      <th>original_title</th>
      <th>popularity</th>
      <th>release_date</th>
      <th>title</th>
      <th>vote_average</th>
      <th>vote_count</th>
    </tr>
    <tr>
      <th>genre_ids</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>[12, 28, 14]</th>
      <td>24034</td>
      <td>522417</td>
      <td>zh</td>
      <td>奇门遁甲</td>
      <td>80.773</td>
      <td>2018-10-23</td>
      <td>The Thousand Faces of Dunjia</td>
      <td>8.3</td>
      <td>13948</td>
    </tr>
    <tr>
      <th>[28, 53]</th>
      <td>26399</td>
      <td>569869</td>
      <td>th</td>
      <td>우는 남자</td>
      <td>78.123</td>
      <td>2018-12-20</td>
      <td>Your Move</td>
      <td>7.4</td>
      <td>10081</td>
    </tr>
    <tr>
      <th>[28, 12, 16, 878, 35]</th>
      <td>23812</td>
      <td>324857</td>
      <td>en</td>
      <td>Spider-Man: Into the Spider-Verse</td>
      <td>60.534</td>
      <td>2018-12-14</td>
      <td>Spider-Man: Into the Spider-Verse</td>
      <td>8.4</td>
      <td>4048</td>
    </tr>
    <tr>
      <th>[28, 12, 14]</th>
      <td>24318</td>
      <td>525135</td>
      <td>zh</td>
      <td>西游记之孙悟空三打白骨精</td>
      <td>53.783</td>
      <td>2018-12-21</td>
      <td>Warcraft</td>
      <td>7.3</td>
      <td>11991</td>
    </tr>
    <tr>
      <th>[878, 28, 12]</th>
      <td>24924</td>
      <td>521323</td>
      <td>en</td>
      <td>Wastelander</td>
      <td>50.289</td>
      <td>2018-02-02</td>
      <td>Wastelander</td>
      <td>8.0</td>
      <td>19673</td>
    </tr>
  </tbody>
</table>
</div>



### Popularity By Language


```python
grouped = tmbd_df.groupby(["original_language"]).sum().sort_values(by="popularity", ascending= False)
grouped.head()
```

    C:\Users\user\AppData\Local\Temp\ipykernel_10264\1549669306.py:1: FutureWarning: The default value of numeric_only in DataFrameGroupBy.sum is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
      grouped = tmbd_df.groupby(["original_language"]).sum().sort_values(by="popularity", ascending= False)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>id</th>
      <th>popularity</th>
      <th>vote_average</th>
      <th>vote_count</th>
    </tr>
    <tr>
      <th>original_language</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>en</th>
      <td>312028215</td>
      <td>7005029780</td>
      <td>71895.155</td>
      <td>138662.0</td>
      <td>4874990</td>
    </tr>
    <tr>
      <th>fr</th>
      <td>5744495</td>
      <td>118048030</td>
      <td>2155.574</td>
      <td>3130.8</td>
      <td>75337</td>
    </tr>
    <tr>
      <th>ja</th>
      <td>3769256</td>
      <td>70813222</td>
      <td>1513.434</td>
      <td>1809.1</td>
      <td>54774</td>
    </tr>
    <tr>
      <th>es</th>
      <td>6070196</td>
      <td>127264882</td>
      <td>1257.725</td>
      <td>2874.3</td>
      <td>29396</td>
    </tr>
    <tr>
      <th>ru</th>
      <td>2859417</td>
      <td>64494601</td>
      <td>708.220</td>
      <td>1579.4</td>
      <td>4901</td>
    </tr>
  </tbody>
</table>
</div>




```python
language =  ["en","fr","ja","es", "ru"]
Popularity= [71896,2155,1513,1257,708]
```


```python
grouped["popularity"].head()
```




    original_language
    en    71895.155
    fr     2155.574
    ja     1513.434
    es     1257.725
    ru      708.220
    Name: popularity, dtype: float64




```python
fig,ax = plt.subplots()
plt.pie(Popularity, labels = language)
plt.title("Most Prefered Languages");

```


    
![png](output_102_0.png)
    


### Merging Datasets


```python
Merged_df= pd.merge(rv_df, budgets)
Merged_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>review</th>
      <th>fresh</th>
      <th>critic</th>
      <th>top_critic</th>
      <th>publisher</th>
      <th>date</th>
      <th>score</th>
      <th>outof</th>
      <th>release_date</th>
      <th>movie</th>
      <th>production_budget</th>
      <th>domestic_gross</th>
      <th>worldwide_gross</th>
      <th>Domestic_profit</th>
      <th>worldwide_profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>A distinctly gallows take on contemporary fina...</td>
      <td>fresh</td>
      <td>PJ Nabarro</td>
      <td>0</td>
      <td>Patrick Nabarro</td>
      <td>November 10, 2018</td>
      <td>3</td>
      <td>5</td>
      <td>Jun 7, 2019</td>
      <td>Dark Phoenix</td>
      <td>350000000</td>
      <td>42762350</td>
      <td>149762350</td>
      <td>-307237650</td>
      <td>-200237650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>A distinctly gallows take on contemporary fina...</td>
      <td>fresh</td>
      <td>PJ Nabarro</td>
      <td>0</td>
      <td>Patrick Nabarro</td>
      <td>November 10, 2018</td>
      <td>3</td>
      <td>5</td>
      <td>Nov 21, 2018</td>
      <td>Ralph Breaks The Internet</td>
      <td>175000000</td>
      <td>201091711</td>
      <td>524283695</td>
      <td>26091711</td>
      <td>349283695</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>A distinctly gallows take on contemporary fina...</td>
      <td>fresh</td>
      <td>PJ Nabarro</td>
      <td>0</td>
      <td>Patrick Nabarro</td>
      <td>November 10, 2018</td>
      <td>3</td>
      <td>5</td>
      <td>Apr 8, 2005</td>
      <td>Sahara</td>
      <td>145000000</td>
      <td>68671925</td>
      <td>121671925</td>
      <td>-76328075</td>
      <td>-23328075</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>A distinctly gallows take on contemporary fina...</td>
      <td>fresh</td>
      <td>PJ Nabarro</td>
      <td>0</td>
      <td>Patrick Nabarro</td>
      <td>November 10, 2018</td>
      <td>3</td>
      <td>5</td>
      <td>Oct 5, 2018</td>
      <td>Venom</td>
      <td>116000000</td>
      <td>213511408</td>
      <td>853628605</td>
      <td>97511408</td>
      <td>737628605</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>A distinctly gallows take on contemporary fina...</td>
      <td>fresh</td>
      <td>PJ Nabarro</td>
      <td>0</td>
      <td>Patrick Nabarro</td>
      <td>November 10, 2018</td>
      <td>3</td>
      <td>5</td>
      <td>Feb 18, 2005</td>
      <td>Son of the Mask</td>
      <td>100000000</td>
      <td>17018422</td>
      <td>59918422</td>
      <td>-82981578</td>
      <td>-40081578</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
publisher= Merged_df["publisher"].value_counts().head().index.tolist()
frequncy=list(Merged_df["publisher"].value_counts().nlargest(5))
sns.barplot(x=publisher, y = frequncy, data = Merged_df, palette='OrRd')
plt.xticks(rotation = 30);
plt.title("TOP PUBLISHERS");
```


    
![png](output_106_0.png)
    


###  Summary

 The Visualizations above inform how microsoft will begin their movie-Production journey. With the insights we can be sure that Microsoft wil get it right in data analysis


```python
S
```
