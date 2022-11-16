# -*- coding: utf-8 -*-
import requests
import datetime
import json

def train_departure(train, station, date):
    url = 'https://rata.digitraffic.fi/api/v1/trains/2021-3-14/2'

    ok  = True

    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        ok = False
        
    if ok:
        data = response.json()
        print(data)
       # for j in data:
           # print(j["trainNumber"])
            
        out_file = open("trains.json", "w")
        
        json.dump(data, out_file, indent = 6)
        
        out_file.close()
        
        
if __name__=='__main__':
    #Write test code here
    date=datetime.date(2021, 3, 21)
    departure=train_departure('56', 'OL', date)
   # print(departure)