#!/usr/bin/env python
# coding: utf-8

# In[23]:


import re
from utils.utils import *

import pandas as pd


# In[2]:


server = 'biorxiv'
date_start = '2021-06-01'
date_end = '2021-06-01'
data_biorxiv = date_rxiv(server, date_start, date_end)
data_biorxiv.drop_duplicates(subset = ['doi'], keep = 'last', inplace = True)
data_biorxiv


# In[3]:


doi_article = data_biorxiv.at[0, 'doi']
server = 'biorxiv'
data_doi = article_detail(server, doi_article)
data_doi


# In[4]:


server = 'medrxiv'
data_medrxiv = date_rxiv(server, date_start, date_end)
data_medrxiv.drop_duplicates(subset = ['doi'], keep = 'last', inplace = True)
data_medrxiv


# In[5]:


date_start = '2021-06-01'
date_end = '2021-06-01'
data_pub_biorxiv = date_published_article(date_start, date_end)
data_pub_biorxiv


# In[6]:


publisher_id = '10.15252'
date_start = '2020-06-01'
date_end = '2021-06-01'
data_pub_biorxiv = date_publisher_detail(publisher_id, date_start, date_end)
data_pub_biorxiv


# In[7]:


data_stats = biorxiv_stats()
data_stats


# In[8]:


data_biorxiv.to_csv('processed/biorxiv_june.csv', index=False)
data_medrxiv.to_csv('processed/medrxiv_june.csv', index=False)


# In[22]:


print(data_biorxiv.at[5, 'abstract'])


# In[40]:


first_words = set()
for i, abstract in enumerate(data_biorxiv['abstract'].tolist()):
    hits = []
    sentences = re.split('\n', abstract)
    for sent in sentences:
        try:
            first = sent.split()[0]
        except:
            first = ''
        hits.append(re.findall(r'\w*[A-Z]\w*[A-Z]\w*', first))
    #if hit:
    if sum([len(elem) for elem in hits]) > 0:
        for elem in hits:
            if len(elem) > 0:
                first_words.add(elem[0])
print(first_words)


# In[51]:


term_list = ['Results', 'Contribution', 'Highlights', 'Background', 'Conclusions', 'Introduction', 'Motivation', 'Methods', 'Teaser',              'Abstracts', 'Conclusion', 'IMPORTANCE', 'SUMMARY', 'Finding', 'Availability']
for word in first_words:
    present = 0
    for term in term_list:
        if term in word:
            present = 1
            break
    if present == 0:
        print(word)
###FIND GRAPHICAL ABSTRACT AND REMOVE!
###AUTHOR STATEMENT, IMPACT STATEMENT, SIGNIFICANCE STATEMENT, DATA STATEMENT


# In[ ]:




