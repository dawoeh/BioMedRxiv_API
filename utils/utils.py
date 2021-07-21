import requests
import json

from time import sleep

import pandas as pd

def date_rxiv(server, from_date, to_date, result_start=0):
    data = pd.DataFrame()
    while True:
        response = requests.get(f'https://api.biorxiv.org/details/{server}/{from_date}/{to_date}/{result_start}')
        doc = response.json()	
        result_count = len(doc['collection'])
        if result_count == 0:
                break
        for article in doc['collection']:
            data_temp = pd.DataFrame(list(article.items()))
            data_temp = data_temp.transpose()
            data_temp.columns = article.keys()
            data_temp.drop(0, inplace=True)
            data = data.append(data_temp).reset_index(drop=True)
        result_start += 100
        sleep(1)
    return data

def article_detail(server, doi):
    data = pd.DataFrame()
    response = requests.get(f'https://api.biorxiv.org/details/{server}/{doi}')
    doc = response.json()   
    for article in doc['collection']:
        data_temp = pd.DataFrame(list(article.items()))
        data_temp = data_temp.transpose()
        data_temp.columns = article.keys()
        data_temp.drop(0, inplace=True)
        data = data.append(data_temp).reset_index(drop=True)
    return data

def date_published_article(from_date, to_date, result_start=0):
    data = pd.DataFrame()
    while True:
        response = requests.get(f'https://api.biorxiv.org/pub/{from_date}/{to_date}/{result_start}')
        doc = response.json()   
        result_count = len(doc['collection'])
        if result_count == 0:
                break
        for article in doc['collection']:
            data_temp = pd.DataFrame(list(article.items()))
            data_temp = data_temp.transpose()
            data_temp.columns = article.keys()
            data_temp.drop(0, inplace=True)
            data = data.append(data_temp).reset_index(drop=True)
        result_start += 100
        sleep(1)
    return data

def date_publisher_detail(publisher_id, from_date, to_date, result_start=0):
    data = pd.DataFrame()
    while True:
        response = requests.get(f'https://api.biorxiv.org/publisher/{publisher_id}/{from_date}/{to_date}/{result_start}')
        doc = response.json()   
        result_count = len(doc['collection'])
        if result_count == 0:
                break
        for article in doc['collection']:
            data_temp = pd.DataFrame(list(article.items()))
            data_temp = data_temp.transpose()
            data_temp.columns = article.keys()
            data_temp.drop(0, inplace=True)
            data = data.append(data_temp).reset_index(drop=True)
        result_start += 100
        sleep(1)
    return data

def biorxiv_stats(interval = 'm'):
    data = pd.DataFrame()
    response = requests.get(f'https://api.biorxiv.org/sum/{interval}')
    doc = response.json()   
    for element in doc['bioRxiv content statistics']:
        data_temp = pd.DataFrame(list(element.items()))
        data_temp = data_temp.transpose()
        data_temp.columns = element.keys()
        data_temp.drop(0, inplace=True)
        data = data.append(data_temp).reset_index(drop=True)
    return data
