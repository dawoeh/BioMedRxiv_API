#!/usr/bin/env python
# coding: utf-8

# In[35]:


import re
from utils.utils import *

import pandas as pd


# In[22]:


server = 'biorxiv'
date_start = '2021-05-01'
date_end = '2021-06-30'
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


# In[27]:


data_biorxiv.to_csv('processed/biorxiv_june.csv', index=False)
data_medrxiv.to_csv('processed/medrxiv_june.csv', index=False)


# In[9]:


print(data_biorxiv.at[5, 'abstract'])


# In[24]:


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


# In[28]:


term_list = ['Results', 'Contribution', 'Highlights', 'Background', 'Conclusions', 'Introduction', 'Motivation', 'Methods', 'Teaser',              'Abstracts', 'Conclusion', 'IMPORTANCE', 'SUMMARY', 'Finding', 'Availability', 'Highlight', 'Importance', 'Summary', 'RESULTS',             'Rationale', 'Aim', 'Significance', 'Objectives', 'Purpose', 'Synopsis', 'METHODS', 'SIGNIFICANCE', 'Objectives', 'Design',             'Objective', 'Approach', 'Methodology', 'HIGHLIGHTS', 'INTRODUCTION', 'Abstract', 'CONCLUSIONS', 'Software', 'Interpretations',             'FUNDING', 'Summery', 'Perspective', 'Discussion', 'CONCLUSION', 'DISCUSSION', 'Funding', 'Advances', 'Classification', 'SYNOPSIS',             'BACKGROUND', 'Method', 'Innovation', 'PREMISE', 'Implications', 'STATEMENT', 'Contact', 'Location', 'Outlook', 'TEASER',              'Interpretation', 'eTOC', 'Result', 'TABLE', 'Taxon', 'Measurements', 'Participants', 'Sentence', 'Materials',              'PURPOSE', 'Context', 'Setting', 'SUMMMARY', 'Hypothesis', 'Keypoitns', 'Implementation', 'Limitations', 'OBJECTIVE',              'Precis', 'Questions', 'Database',              'C_LIO_LI', 'O_LI', 'O_FIG_DISPLAY_L', 'O_SCPLOWBSTRACTC_SCPLOW', 'AO_SCPLOWUTHORC_SCPLOW', 'SO_SCPLOWUMMARYC_SCPLOW',             'C_TABLECAPTION', 'IO_SCPLOWMPORTANCEC_SCPLOW', 'C_LI', 'C_FIG_DISPLAY', 'C_TEXTBOX', 'O_SCPLOWLC_SCPLOW',             'SO_SCPLOWIGNIFICANCEC_SCPLOWO_SCPCAP', 'KO_SCPLOWEYC_SCPLOWO_SCPCAP', 'C_QD']
for word in first_words:
    present = 0
    for term in term_list:
        if term in word:
            present = 1
            break
    if present == 0:
        print(word)
###FIND GRAPHICAL ABSTRACT AND REMOVE! Remove after ToC! Remove between O_FIG/O_TBL and C_FIG/C_TBL
###AUTHOR STATEMENT, IMPACT STATEMENT, SIGNIFICANCE STATEMENT, DATA STATEMENT, ARTICLE SUMMARY, CONFLICT OF INTEREST, IN BRIEF, METHODOLOGY/PRINCIPAL FINDINGS
##ABSTRACT AND KEYWORDS, PROGRAM SUMMARY, ARTICLE SUMMARY, NEW & NOTEWORTHY


# In[85]:


abstract_list = data_biorxiv['abstract'].tolist()
print(abstract_list[4909])


# In[126]:


abstract_list = data_biorxiv['abstract'].tolist()

header_list = ['Results', 'Contribution', 'Highlights', 'Background', 'Conclusions', 'Introduction', 'Motivation', 'Methods', 'Teaser',              'Abstracts', 'Conclusion', 'IMPORTANCE', 'SUMMARY', 'Finding', 'Availability', 'Highlight', 'Importance', 'Summary', 'RESULTS',             'Rationale', 'Aim', 'Significance', 'Objectives', 'Purpose', 'Synopsis', 'METHODS', 'SIGNIFICANCE', 'Objectives', 'Design',             'Objective', 'Approach', 'Methodology', 'HIGHLIGHTS', 'INTRODUCTION', 'Abstract', 'CONCLUSIONS', 'Software', 'Interpretations',             'FUNDING', 'Summery', 'Perspective', 'Discussion', 'CONCLUSION', 'DISCUSSION', 'Funding', 'Advances', 'Classification', 'SYNOPSIS',             'BACKGROUND', 'Method', 'Innovation', 'PREMISE', 'Implications', 'STATEMENT', 'Contact', 'Location', 'Outlook', 'TEASER',              'Interpretation', 'eTOC', 'Result', 'TABLE', 'Taxon', 'Measurements', 'Participants', 'Sentence', 'Materials',              'PURPOSE', 'Context', 'Setting', 'SUMMMARY', 'Hypothesis', 'Keypoitns', 'Implementation', 'Limitations', 'OBJECTIVE',              'Precis', 'Questions', 'Database', 'Paragraph', 'PARAGRAPH']

markup_list =  ['C_LIO_LI', 'O_LI', 'O_SCPLOWBSTRACTC_SCPLOW', 'AO_SCPLOWUTHORC_SCPLOW', 'SO_SCPLOWUMMARYC_SCPLOW', 'SO_SCPLOWIGNIFICANCEC_SCPLOWO_SCPCAP',             'C_TABLECAPTION', 'IO_SCPLOWMPORTANCEC_SCPLOW', 'C_LI', 'C_TEXTBOX', 'O_SCPLOWLC_SCPLOW', 'C_SCPCAPO_SCPLOWPOINTSC_SCPLOW',             'SO_SCPLOWIGNIFICANCEC_SCPLOWO_SCPCAP', 'KO_SCPLOWEYC_SCPLOWO_SCPCAP', 'C_QD', 'C_ST_ABSO_LI', 'O_ST_ABS', 'C_ST_ABS',                'C_SCPCAPO_SCPLOWPOINTSC_SCPLOW', 'SO_SCPLOWIGNIFICANCEC_SCPLOWO_SCPCAP', 'C_SCPCAPO_SCPLOWC_SCPLOW', 'O_TEXTBOX', 'O_SCPCAP']

statement_list = ['AUTHOR STATEMENT', 'IMPACT STATEMENT', 'SIGNIFICANCE STATEMENT', 'DATA STATEMENT', 'ARTICLE SUMMARY',                   'CONFLICT OF INTEREST', 'IN BRIEF', 'METHODOLOGY/PRINCIPAL FINDINGS', 'ABSTRACT AND KEYWORDS', 'PROGRAM SUMMARY',                   'ARTICLE SUMMARY', 'NEW & NOTEWORTHY', 'Graphical abstract']


markup_list.sort(key = len, reverse=True)

for i, abstract in enumerate(abstract_list):
    for markup in markup_list:
        abstract = abstract.replace(markup, ' ')
    for statement in statement_list:
        abstract = abstract.replace(statement, ' ')
    words = re.findall(r'\S+|\n',abstract)
    pointer = 1
    stop = 0
    new_words=[]
    for k, word in enumerate(words):
        hit = []
        if pointer == 1:
            hit.append(re.findall(r'\w*[A-Z]\w*[A-Z]\w*', word))
            if len(hit) > 0:
                for header in header_list:
                    if header in word:
                        word = word.replace(header, '')               
        if 'O_FIG' in word:
            stop = 1
        if 'O_TBL' in word:
            stop = 1
        words[k] = word
        if stop == 0:
            new_words.append(word)
        if 'C_FIG' in word:
            stop = 0
        if 'C_TBL' in word:
            stop = 0        
        if '\n' in word:
            pointer = 1
        else:
            pointer = 0

    abstract_list[i] = ' '.join(new_words)
    abstract_list
print(abstract_list[4909])


# In[127]:


first_words = set()
for i, abstract in enumerate(abstract_list):
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

term_list = ['Statement',]
for word in first_words:
    present = 0
    for term in term_list:
        if term in word:
            present = 1
            break
    if present == 0:
        print(word)


# In[121]:


data_biorxiv_curate = data_biorxiv.copy()
data_biorxiv_curate['abstract'] = abstract_list
data_biorxiv_curate.to_csv('processed/biorxiv_june_curate.csv', index=False)

