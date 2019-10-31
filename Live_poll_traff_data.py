#! python3

import pandas as pd
import requests
import json
import getpass

key=getpass.getpass(input("your pw"))
token=getpass.getpass()


def live_pollution(token,city):
    base=f"https://api.waqi.info/feed/{city}/?token={token}"
    response=requests.get(base)
    dicti=response.json()
    real_time=pd.DataFrame(dicti["data"]["iaqi"])
    col_to_keep=["co","no2","o3","pm10","pm25","so2","t"]
    col_to_drop=[col for col in real_time.columns if col not in col_to_keep]
    real_time.drop(col_to_drop,inplace=True,axis=1)
    real_time.reset_index(drop=True,inplace=True)
    real_time=real_time.assign(city=city)
    return real_time

def coordinates(city):
    link=f"https://nominatim.openstreetmap.org/search/{city}?format=json&limit=1&polygon_svg=1"
    response3=requests.get(link)
    dicti3=response3.json()
    lat=dicti3[0]["lat"]
    lon=dicti3[0]["lon"]
    coordinates=lat+","+lon
    return coordinates

def live_traffic(key,city):
    coors=coordinates(city)
    url=f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={coors}&unit=KMPH&key={key}"
    response2=requests.get(url)
    dicti2=response2.json()
    real_traffic=pd.DataFrame(dicti2["flowSegmentData"])
    col_to_keep2=["currentSpeed","freeFlowSpeed","currentTravelTime","freeFlowTravelTime"]
    col_to_drop2=[col for col in real_traffic.columns if col not in col_to_keep2]
    real_traffic.drop(col_to_drop2,inplace=True,axis=1)
    real_traffic.reset_index(drop=True,inplace=True)
    real_traffic=real_traffic.assign(city=city)
    return real_traffic

def live_info(city):
    pol=live_pollution(token,city)
    traf=live_traffic(key,city)
    def_df=pol.merge(traf, left_on='city',right_on='city')
    def_df.set_index("city",inplace=True)
    return def_df

live_info(input("what city you want to know available data? "))