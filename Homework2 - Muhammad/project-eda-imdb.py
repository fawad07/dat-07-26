#!/usr/bin/env python
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# # Project 2: Analyzing IMDb Data
# 
# _Author: Kevin Markham (DC)_
# 
# ---

# For project two, you will complete a series of exercises exploring movie rating data from IMDb.
# 
# For these exercises, you will be conducting basic exploratory data analysis on IMDB's movie data, looking to answer such questions as:
# 
# What is the average rating per genre?
# How many different actors are in a movie?
# 
# This process will help you practice your data analysis skills while becoming comfortable with Pandas.

# ## Basic level

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Read in 'imdb_1000.csv' and store it in a DataFrame named movies.

# In[2]:


movies = pd.read_csv('./data/imdb_1000.csv')
movies.head()


# #### Check the number of rows and columns.

# In[3]:


# Answer:
rows = movies.shape[0]
col = movies.shape[1]
print(f"Data Rows: {rows}\nData Columns: {col}")


# #### Check the data type of each column.

# In[4]:


# Answer:
movies.dtypes


# #### Calculate the average movie duration.

# In[5]:


# Answer:
movies['duration'].mean()


# #### Sort the DataFrame by duration to find the shortest and longest movies.

# In[6]:


# Answer:
movies.sort_values(by='duration',ascending=True)


# #### Create a histogram of duration, choosing an "appropriate" number of bins.

# In[7]:


# Answer:
plt.hist(movies['duration'], bins = 6)


# #### Use a box plot to display that same data.

# In[8]:


# Answer:
plt.boxplot(movies['duration'])
plt.show


# ## Intermediate level

# #### Count how many movies have each of the content ratings.

# In[9]:


# Answer:
rating_dict = {
    'R' : 0,
    'G' : 0,
    'PG-13:' : 0,
    'PASSED' : 0,
    'Approved' : 0,
    'NOT RATED' : 0,
    'GP' : 0,
    'TV-MA' : 0,
    'X' : 0,
    'PG' : 0,
    'NC-17' : 0,
    'UNRATED' : 0,
    'G' : 0,
    'TV_MA' : 0
}
for i in movies['content_rating']:
    if i in rating_dict:
        rating_dict[i] = rating_dict[i] + 1
print(rating_dict)


# In[10]:


movies['content_rating'].value_counts()


# #### Use a visualization to display that same data, including a title and x and y labels.

# In[11]:


# Answer:
#create bar chart
width = list(rating_dict)
height = list(rating_dict.values())
plt.bar(width, height)
#x-axis label
plt.xlabel('Rating')
#y-axis label
plt.ylabel('Number of Ratings')
#show
plt.show()


# #### Convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP.

# In[ ]:


# Answer:
movies = movies.replace(['NOT RATED', 'APPROVED', 'PASSED', 'GP'], 'UNRATED')
movies.head(50)


# #### Convert the following content ratings to "NC-17": X, TV-MA.

# In[ ]:


# Answer:
movies = movies.replace(['X', 'TV-MA'], 'NC-17')
movies.tail(50)


# #### Count the number of missing values in each column.

# In[18]:


# Answer:
isNull = movies[movies['content_rating'].isnull()]
isNull


# #### If there are missing values: examine them, then fill them in with "reasonable" values.

# In[22]:


# Answer:
isNull = movies.replace(['NaN'], 'UNKNOWN')
isNull.tail(50)


# #### Calculate the average star rating for movies 2 hours or longer, and compare that with the average star rating for movies shorter than 2 hours.

# In[ ]:


# Answer
str_rating_mov_2hrs_plus = movies[movies['duration'] > 120]['star_rating'].mean()
str_rating_mov_2hrs_less = movies[movies['duration'] < 120]['star_rating'].mean()
print(f"Average star rating for movies 2 hours or longer: {str_rating_mov_2hrs_plus}\nAverage star rating for movies shorter than 2 hours: {str_rating_mov_2hrs_less}")


# #### Use a visualization to detect whether there is a relationship between duration and star rating.

# In[23]:


# Answer:
relavent_data =  movies.groupby('star_rating')['duration'].mean().reset_index()
fig = px.bar(relavent_data, x='star_rating', y='duration', barmode='group')
fig.show()


# #### Calculate the average duration for each genre.

# In[30]:


# Answer:
#movies['genre']
#create dictionary with any values and genre as the keys
genre_dict = {}
for i in movies['genre']:
    genre_dict[i] = i
#genre_dict 
#for each genre (keys) values are the mean duration 
for i in movies['genre']:
    genre_dict[i] = movies[movies.genre == i]['duration'].mean()
    
print(f'Average duration of each Genre')
genre_dict
#movies[movies['genre']]['duration'].mean()    # <-- ask what i am doing wrong here 


# In[ ]:


movies.groupby('genre')['duration'].mean()


# ## Advanced level

# #### Visualize the relationship between content rating and duration.

# In[23]:


# Answer:

relavent_data = movies.groupby('content_rating')['duration'].mean().reset_index()
fig = px.bar(relavent_data, x='content_rating', y='duration', barmode='group')
fig.show()



#------INITIAL APPROACH-------------------------------------------------------------
#def values_toString(aDict):
#    temp_list = list(aDict.values())
#    values_list = []
#    for i in temp_list:
#        temp = str(i)
#        values_list.append(temp)
#    return values_list


#def keys_toString(aDict):
#    new_list = list(aDict)
#    for i in new_list:
#        temp = str(i)
#        new_list.append(temp)
#    return new_list



#keys:content_rating, values : mean duration
#content_rating_dict = {i : movies['duration'].mean() for i in movies['content_rating']} 

#dict keys list
#content_rating_list = list(content_rating_dict)

#movie_duration_dict = {i : 'time' for i in movies['duration']}
#content_rating_x_axis = list(content_rating_dict)                 #keys_toString(content_rating_dict) 
#Content_rating_values_y_axis = list(content_rating_dict.values())        #values_toString(content_rating_dict)


#Content_rating_values_y_axis = values_toString(content_rating_dict)   #DEBUGGING STATEMENT
#Content_rating_values_y_axis        #debugging statement REMOVE LATER!!


#y_axis

#plt.bar({'Content Rating' : content_rating_x_axis, 'Average Movie Content Duration' : Content_rating_values_y_axis})
#movies.plot.bar(x=content_rating_dict, y='y_axis', rot=0)

#fig = plt.figure()
#ax = fig.add_axes([0, 0, 1, 1])
#ax.bar(content_rating_x_axis, Content_rating_values_y_axis)



#------------BAR CHART CODE-------------------------------

#plt.bar(content_rating_x_axis, Content_rating_values_y_axis)   <--- TypeError: missing Height attribute ?

#x-axis label
#plt.xlabel('COntent Rating')
#y-axis label
#plt.ylabel('Average Movie Content Duration')
#show
#plt.show()

#----------------END OF INITIAL APPROACH--------------------------------


#DEBUGGING STATEMENTS : GooGLE SEARCHES APPROACHES
#width = list(rating_dict)
#height = list(rating_dict.values())

#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#langs = ['C', 'C++', 'Java', 'Python', 'PHP']plt.bar(content_rating_x_axis, Content_rating_values_y_axis)
#students = [23,17,35,29,12]
#ax.bar(langs,students)
#plt.show()


# #### Determine the top rated movie (by star rating) for each genre.

# In[41]:


# Answer:

#for each genre (keys) values are the mean duration 
for i in movies['genre']:
    genre_dict[i] = movies[movies.genre == i]['star_rating'].max()
    
print(f'Top rated movie by star rating of each Genre\n')
genre_dict


# In[53]:


group_values = movies.groupby('genre')['star_rating'].idxmax().values
movies.iloc[group_values]


# #### Check if there are multiple movies with the same title, and if so, determine if they are actually duplicates.
- Ask why does the for loop does not work
# In[25]:


# Answer:
'''
duplicates = movies[movies['title'].duplicated()]
duplicate_loc_dict = {}
#duplicates

#TODO - for titles is movies data
for i in movies['title']:
    #TODO - if i in the duplicate list
    #Set Dict key to title and set value to list of index
    if i in duplicates['title']:
        duplicate_loc_dict[i] = list(i).append(movies['title'].index())
duplicate_loc_dict
#duplicates


#movies[movies['title'] == 'True Grit']   ----DEBUGGING STATEMENT
'''


# In[43]:


movies[movies['title'].duplicated(keep=False)]   #shows duplicat titles


# #### Calculate the average star rating for each genre, but only include genres with at least 10 movies
# 

# #### Option 1: manually create a list of relevant genres, then filter using that list

# In[77]:


# Answer:
#CELL FILTERS OUT THE GENRE WITH 10 OR MORE MOVIES
'''
parameter: a dictionary
return: new dictionary with values greater than 10
Description: method takes a dictionary of all genres
            and return a new dictianary with the values greater than 
            10
'''
def genre_more_than_10(aDict):
    newDict = { }
    for i in aDict:
        if aDict[i] > 10:
            newDict[i] = aDict[i]
    return newDict

#dict key == genre, dict value == count of genre
#genre_dict has count of all genre greater and less than 10
#new_genre_dict has count of all genre > 10

genre_dict = dict(movies['genre'].value_counts())
new_genre_dict = genre_more_than_10(genre_dict)



#DEBUGGING STATEMENTS
#new_genre_dict
#movies['genre'].value_counts()
#movies[movies['genre'] == 'Crime']['genre'].value_counts()
#movies['genre'].value_counts() > 10


# In[80]:


#CONTINUE OF PREVIOUS CELL: TAKES THE KEYS FROM DICTIONARY
#CONVERT IN LIST AND LOOPS THROUGH THE LIST 
#COMPARES movies['genre'] WITH GENRE IN LIST
#TAKES THE VALUE COUNT AND MEAN OF THAT GENRE

#Collect only keys from genre dict
keys = list(new_genre_dict)

for i in keys:
    print(f'{i}')
    print(movies[ movies['genre'] == i]['star_rating'].value_counts().mean())
    #print()
    

#DEBUGGING STATEMENTS
#movies[ movies['genre'] == 'Crime']['star_rating'].value_counts()
#movies[ movies['genre'] == 'Crime']['genre'].value_counts()     #<-- 124 crimes


# #### Option 2: automatically create a list of relevant genres by saving the value_counts and then filtering

# In[82]:


# Answer:
movies[movies['star_rating'] < 10]['genre'].value_counts()
temp = {}
for i in movies['genre']:
    temp[i] = movies[movies.genre == i]['star_rating'].mean()
temp


# #### Option 3: calculate the average star rating for all genres, then filter using a boolean Series

# In[55]:


# Answer:
movies.groupby(['genre', 'star_rating']).mean() > 10


# #### Option 4: aggregate by count and mean, then filter using the count

# In[39]:


# Answer:
movies.agg({'star_rating' : 'mean' ,'genre' : 'count'})    #debugging Statement
genre_count = movies['genre'].value_counts()
genres = genre_count[genre_count >= 10].index
result_dict = {}
for i in movies['genre']:
    if i in genres:
       result_dict = dict(movies.groupby('genre')['star_rating'].agg(['mean', 'count'])) 
result_dict

#counts = movies['genre'].value_counts()
#idx = counts[counts >= 10].index
#movies[movies.genre.isin(idx)].groupby('genre')['star_rating'].agg(['mean', 'count'])
#movies[movies.genre.isin(idx)].groupby('genre')['star_rating'].agg(['mean', 'count'])


# ## Bonus

# #### Figure out something "interesting" using the actors data!

# In[106]:


# Answer
movies.sort_values("star_rating", inplace = True) 
filtering = movies['duration'] > 120
movies.where(filtering,inplace=True)
movies.dropna()


# In[107]:


movies.sort_values("title", inplace = True) 
filtering = movies['content_rating'] == 'R'
movies.where(filtering,inplace=True)
movies.dropna()

