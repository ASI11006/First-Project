#!/usr/bin/env python
# coding: utf-8

# In[216]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[217]:


Movies = pd.read_csv('Downloads/First-Project-main (2)/movie_metadata.csv')

Movies


# In[218]:


Movies.head(10)


# In[219]:


Movies.shape


# In[220]:


Movies.columns


# In[221]:


Movies.info()


# In[222]:


Movies = Movies.loc[:,['director_name','director_facebook_likes']]


# In[223]:


Movies.head(25)


# In[224]:


Movies['director_facebook_likes'] = Movies['director_facebook_likes'].replace(np.nan, 'unknown')
Movies['director_name'] = Movies['director_name'].replace(np.nan, '17.0')


# In[225]:


Movies.head().plot(x='director_name', y='director_facebook_likes', title= 'Director with most likes')


# In[207]:


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




