import requests
import json

from time import sleep
import tqdm
import math

import pandas as pd

def date_rxiv(server, from_date, to_date, result_start=0):
    data = pd.DataFrame()
    pbar = None
    while True:
        response = requests.get(f'https://api.biorxiv.org/details/{server}/{from_date}/{to_date}/{result_start}')
        doc = response.json()   
        result_count = len(doc['collection'])
        batch = 100
        if pbar is None:
            pbar = tqdm.tqdm(total= math.ceil(int(doc['messages'][0]['total'])/batch))
        if result_count == 0:
                break
        data = data.append(pd.DataFrame(doc['collection'])).reset_index(drop=True)
        result_start += 100
        pbar.update(1)
        sleep(0.2)
    pbar.close()
    return data

def article_detail(server, doi):
    data = pd.DataFrame()
    response = requests.get(f'https://api.biorxiv.org/details/{server}/{doi}')
    doc = response.json()   
    data = data.append(pd.DataFrame(doc['collection'])).reset_index(drop=True)
    return data

def date_published_article(from_date, to_date, result_start=0):
    data = pd.DataFrame()
    pbar = None
    while True:
        response = requests.get(f'https://api.biorxiv.org/pub/{from_date}/{to_date}/{result_start}')
        doc = response.json()   
        result_count = len(doc['collection'])
        batch = 100
        if pbar is None:
            pbar = tqdm.tqdm(total= math.ceil(int(doc['messages'][0]['total'])/batch))
        if result_count == 0:
                break
        data = data.append(pd.DataFrame(doc['collection'])).reset_index(drop=True)
        result_start += batch
        pbar.update(1)
        sleep(0.2)
    pbar.close()
    return data

def date_publisher_detail(publisher_id, from_date, to_date, result_start=0):
    data = pd.DataFrame()
    pbar = None
    while True:
        response = requests.get(f'https://api.biorxiv.org/publisher/{publisher_id}/{from_date}/{to_date}/{result_start}')
        doc = response.json()   
        result_count = len(doc['collection'])
        batch = 100
        if pbar is None:
            pbar = tqdm.tqdm(total= math.ceil(int(doc['messages'][0]['total'])/batch))
        if result_count == 0:
                break
        data = data.append(pd.DataFrame(doc['collection'])).reset_index(drop=True)
        result_start += batch
        pbar.update(1)
        sleep(0.2)
    pbar.close()
    return data

def biorxiv_stats(interval = 'm'):
    data = pd.DataFrame()
    response = requests.get(f'https://api.biorxiv.org/sum/{interval}')
    doc = response.json()   
    data = data.append(pd.DataFrame(doc['bioRxiv content statistics'])).reset_index(drop=True)
    return data