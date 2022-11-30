# -*- coding: utf-8 -*-
import requests
import datetime
import json

def train_departure(train, station, date):
    url = f"https://rata.digitraffic.fi/api/v1/trains/{date}/{train}"

    ok  = True

    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        ok = False
        
    if ok:
        data = response.json()
        for j in data[0]["timeTableRows"]:
            if j["stationShortCode"] == station and j["type"] == "DEPARTURE":
                timestr = j["scheduledTime"]
                dtime = datetime.datetime.strptime(timestr, '%Y-%m-%dT%H:%M:%S.%fZ')
                print(dtime)
                
                
                return dtime
    
        
        
if __name__=='__main__':
    #Write test code here
    date=datetime.date(2021, 3, 21)
    departure=train_departure('56', 'OL', date)
    print(departure)


