#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from time import sleep

from utils.utils import *

import pandas as pd


# In[2]:


server = 'biorxiv'
date_start = '2021-06-01'
date_end = '2021-06-30'
data_biorxiv = date_rxiv(server, date_start, date_end)


# In[3]:


data_biorxiv


# In[6]:


data_biorxiv.loc[data_biorxiv['version'] != '1', 'version']


# In[7]:


server = 'medrxiv'
data_medrxiv = date_rxiv(server, date_start, date_end)
data_medrxiv


# In[9]:


data_medrxiv.loc[data_medrxiv['version'] != '1', 'version']


# In[10]:


data_biorxiv.to_csv('processed/biorxiv_june.csv', index=False)
data_medrxiv.to_csv('processed/medrxiv_june.csv', index=False)

