#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bom = pd.read_csv('Downloads/dsc-project-template-template-mvp (1)/dsc-project-template-template-mvp/zippedData/bom.movie_gross.csv.gz')


# In[3]:


bom


# In[83]:


tmdb = pd.read_csv('Downloads/dsc-project-template-template-mvp (1)/dsc-project-template-template-mvp/zippedData/tmdb.movies.csv.gz')


# In[84]:


tmdb


# In[6]:


tn = pd.read_csv('Downloads/dsc-project-template-template-mvp (1)/dsc-project-template-template-mvp/zippedData/tn.movie_budgets.csv.gz')


# In[7]:


tn


# In[8]:


tn = tn.rename(columns={'movie': 'title'})


# In[ ]:


tn


# In[85]:


tmdb


# In[86]:


tmdb = tmdb.rename(columns={'original_title': 'Movies'})
tmdb


# In[108]:


tmdb


# In[102]:


import matplotlib

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[117]:


tmdb['Movies']
Movies = tmdb['Movies']
Movies


# tmdb['popularity']
# Ratings = tmdb['popularity']
# Ratings

# In[126]:


tmdb.head().plot(x='Movies', y='vote_average', title= 'Movie with most votes')


# In[ ]:





# In[ ]:




