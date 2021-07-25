#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from utils.utils import *

import pandas as pd


# In[2]:


server = 'biorxiv'
date_start = '2021-06-01'
date_end = '2021-06-30'
data_biorxiv = date_rxiv(server, date_start, date_end)
data_biorxiv.drop_duplicates(subset = ['doi'], keep = 'last', inplace = True)
data_biorxiv.reset_index(drop=True, inplace=True)
data_biorxiv


# In[3]:


doi_article = data_biorxiv.at[0, 'doi']
server = 'biorxiv'
data_doi = article_detail(server, doi_article)
data_doi


# In[4]:


date_start = '2021-06-01'
date_end = '2021-06-30'
server = 'medrxiv'
data_medrxiv = date_rxiv(server, date_start, date_end)
data_medrxiv.drop_duplicates(subset = ['doi'], keep = 'last', inplace = True)
data_medrxiv.reset_index(drop=True, inplace=True)
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


print(data_biorxiv.at[10, 'abstract'])


# In[9]:


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
    if sum([len(elem) for elem in hits]) > 0:
        for elem in hits:
            if len(elem) > 0:
                first_words.add(elem[0])
print(first_words)


# In[10]:


abstract_list = data_biorxiv['abstract'].tolist()
print(abstract_list[195])


# In[11]:


abstract_list = data_biorxiv['abstract'].tolist()

header_list = ['Results', 'Contribution', 'Highlights', 'Background', 'Conclusions', 'Introduction', 'Motivation', 'Methods', 'Teaser',             'Abstracts', 'Conclusion', 'IMPORTANCE', 'SUMMARY', 'Finding', 'Availability', 'Highlight', 'Importance', 'Summary', 'RESULTS',             'Rationale', 'Aim', 'Significance', 'Objectives', 'Purpose', 'Synopsis', 'METHODS', 'SIGNIFICANCE', 'Objectives', 'Design',             'Objective', 'Approach', 'Methodology', 'HIGHLIGHTS', 'INTRODUCTION', 'Abstract', 'CONCLUSIONS', 'Software', 'Interpretations',             'FUNDING', 'Summery', 'Perspective', 'Discussion', 'CONCLUSION', 'DISCUSSION', 'Funding', 'Advances', 'Classification', 'SYNOPSIS',             'BACKGROUND', 'Method', 'Innovation', 'PREMISE', 'Implications', 'STATEMENT', 'Contact', 'Location', 'Outlook', 'TEASER',             'Interpretation', 'eTOC', 'Result', 'TABLE', 'Taxon', 'Measurements', 'Participants', 'Sentence', 'Materials',             'PURPOSE', 'Context', 'SUMMMARY', 'Hypothesis', 'Keypoitns', 'Implementation', 'Limitations', 'OBJECTIVE', 'Statement',             'Precis', 'Questions', 'Database', 'Paragraph', 'PARAGRAPH', 'DECLARATIONS', 'ABSTRACT', 'HIGHLIGHT', 'Application',              'OUTCOME', 'Paragraph', 'Premise', 'Cover', 'Rational', 'ARTICLE', 'SETTING', 'RESUMEN', 'Repositories', 'SAMENVATTING',              'Animals', 'Disclaimer', 'Impact', 'Procedures', 'Foreword', 'EXPOSURES', 'FINDINGS', 'OBJECTIVES', 'Backgroud', 'Assessment',               'DESIGN', 'ABSRTRACT', 'License', 'SUMARY', 'Conclusions', 'ABSRACT', 'Originality/Value', 'Conclusions/interpretation', 'Problem',               'PURPOSE/HYPOTHESIS', 'RATIONALE', 'PARTICIPANTS', 'ASSESSMENT', 'Recommendations', 'Meaning', 'METHOD', 'LIMITATIONS', 'Category',               'Abbreviations', 'IMPRTANCE', 'Methos', 'Details', 'Reproducibility', 'Conclussion', 'Disclosures', 'Recommendation', 'Outcomes',               'REPOSITORIES', 'RESUME', 'IMPACT', 'Availablity', 'Intervention', 'Notice', 'Resources', 'Setting', 'Synthesis', 'Digest',               'SUPPORT', 'Abtsract', 'MANUSCRIPT', 'Blurp', 'ABSTACT', 'KEYPOINTS', 'ABSTARCT', 'Authorship', 'ABTRAST', 'Scope']

markup_list =  ['C_LIO_LI', 'O_LI', 'C_TABLECAPTION', 'C_LI', 'C_TEXTBOX', 'O_QD', 'C_QD', 'C_ST_ABSO_LI', 'O_TEXTBOX', 'O_SCPCAP', 'C_SCPCAP', 'HIGHLIGHTSO_LI', 'HIGHLIGHTO_LI', 'O_LST', 'C_LST'] 

statement_list = ['AUTHOR STATEMENT', 'IMPACT STATEMENT', 'SIGNIFICANCE STATEMENT', 'DATA STATEMENT', 'ARTICLE SUMMARY', 'AUTHOR SUMMARY',                   'CONFLICT OF INTEREST', 'IN BRIEF', 'METHODOLOGY/PRINCIPAL FINDINGS', 'ABSTRACT AND KEYWORDS', 'PROGRAM SUMMARY',                   'ARTICLE SUMMARY', 'NEW & NOTEWORTHY', 'Graphical abstract', 'GRAPHICAL ABSTRACT', 'HIGHLIGHT STATEMENT', 'Funding Information',                   'SUMMARY STATEMENT', 'DATA SUMMARY', 'SUMMARY PARAGRAPH', 'One Sentence Summary', 'CONDENSED ABSTRACT', 'Sentence Summary', 'Software Availability',                  'Statement of Significance', 'Summary statement', 'Summary Paragraph', 'SUBMISSION CATEGORY', 'eTOC Summary', 'Impact Summary', 'Summary sentence',                  'Impact statement', 'Method of Study', 'STATISTICAL TESTS', 'Statistical Tests', 'STUDY TYPE', 'Summary Sentence', 'Significance statement',                  'LIMITATIONS, REASONS FOR CAUTION', 'WIDER IMPLICATIONS OF THE FINDINGS', 'STUDY FUNDINGS/COMPETING INTEREST(S)', 'EXPERIMENTAL APPROACH',                  'KEY RESULTS', 'CONCLUSIONS and IMPLICATIONS', 'BACKGROUND AND PURPOSE', 'AUTHORS SUMMARY', 'DESIGN SETTINGS AND PARTICIPANTS',                  'MAIN OUTCOME AND MEASURES', 'CONCLUSION AND RELEVANCE', 'STRUCTURED ABSTRACT INTRODUCTION', 'SIGNIFICANCE STATMENT', 'Summary Statement',                  'Abstract Importance', 'Conclusions /Significance', 'Methodology / principal finding', 'Back ground', 'Highlight Summary',                  'AVAILABILITY AND IMPLEMENTATION', 'Highlights statement', 'MPACT SUMMARY', 'BACKGROUND & OBJECTIVES', 'BACKGROUND AND HYPOTHESIS',                  'BACKGROUND & AIMS', 'ABSTRACT BACKGROUND & AIMS', 'APPROACH AND RESULTS', 'ABSTRACT  OBJECTIVES', 'eTOC BLURB', 'Author Summary',                  'STATEMENT OF SIGNIFICANCE', 'Software availability', 'eTOC Blurb', 'GRAPHICAL SUMMARY', 'RESEARCH IN CONTEXT', 'CONTRIBUTION TO THE FIELD',                  'TRANSLATIONAL PERSPECTIVE', 'COMPARISON WITH EXISTING METHODS', 'MATERIALS & METHODS', 'EXPERIMENTAL RESULTS', 'SCIENCE FOR SOCIETY',                  'Method Summary', 'RESOURCE SHARING', 'TOC Graphic', 'CLINICAL SIGNIFICANCE', 'ETHICAL STATEMENT', 'Significance Statement',                  'Impact Statement', 'Data Summary']

markup_list.sort(key = len, reverse=True)
header_list.sort(key = len, reverse=True)
statement_list.sort(key = len, reverse=True)

markup_short_list = ['O_ST_ABS', 'C_ST_ABS', 'O_SCPLOW', 'C_SCPLOW']

for i, abstract in enumerate(abstract_list):
    for markup in markup_short_list:
        if markup == 'O_SCPLOW':
            abstract = abstract.replace(markup, '')
        else:
            abstract = abstract.replace(markup, ' ')
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
        if stop == 0:
            new_words.append(word)
        if 'C_FIG' in word:
            stop = 0
        if 'C_TBL' in word:
            stop = 0        
        if '\n' in word or 'C_FIG' in word or 'C_TBL' in word:
            pointer = 1
        else:
            pointer = 0
    abstract_list[i] = ' '.join(new_words)
    abstract_list
print(abstract_list[195])


# In[12]:


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
    if sum([len(elem) for elem in hits]) > 0:
        for elem in hits:
            if len(elem) > 0:
                first_words.add(elem[0])

term_list = []
for word in first_words:
    present = 0
    for term in term_list:
        if term in word:
            present = 1
            break
    if present == 0:
        print(word)


# In[13]:


data_biorxiv_curate = data_biorxiv.copy()
data_biorxiv_curate['abstract'] = abstract_list
data_biorxiv.to_csv('raw/biorxiv_june.csv', index=False)
data_medrxiv.to_csv('raw/medrxiv_june.csv', index=False)
data_biorxiv_curate.to_csv('processed/biorxiv_june_curate.csv', index=False)


# In[14]:


response = requests.get('https://api.biorxiv.org/details/biorxiv/2021-06-01/2021-06-30/0')
doc = response.json()
total_results = int(doc['messages'][0]['total'])
total_results


# In[ ]:




