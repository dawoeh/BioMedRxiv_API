import requests
import json

from time import sleep

import pandas as pd

def date_rxiv(server, from_date, to_date, result_start=1):
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