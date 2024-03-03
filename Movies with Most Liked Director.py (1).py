#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


Movies = pd.read_csv('Downloads/First-Project-main (2)/movie_metadata.csv')

Movies


# In[12]:


Movies.head(50)


# In[14]:


Movies.shape


# In[15]:


Movies.columns


# In[13]:


Movies.info()


# In[16]:


Movies = Movies.loc[:,['director_name','director_facebook_likes']]


# In[17]:


Movies.head(50)


# In[18]:


Movies['director_facebook_likes'] = Movies['director_facebook_likes'].replace(np.nan, 'unknown')
Movies['director_name'] = Movies['director_name'].replace(np.nan, '17.0')


# In[19]:


Movies.head().plot(x='director_name', y='director_facebook_likes', title= 'Director with most likes')


# In[20]:


Movies.isnull().sum()


# In[ ]:





# In[ ]:





# In[ ]:





# tmdb['popularity']
# Ratings = tmdb['popularity']
# Ratings

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




