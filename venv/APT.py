from urllib.parse import urlencode, unquote
import requests
import json
import urllib.request
import pandas as pd
from pandas.io.json import json_normalize

url = "https://data.myhome.go.kr:443/rentalHouseList"
queryString = "?" + urlencode(
{
  "ServiceKey": unquote("4xDvOpaV7CpTr1bm%2BC%2BzeisR0P3e35qVobSYmlq6Eu32Q2%2Bz78dS9nkGq%2BzsjsostMyGPaccfoFY4dxlwq65Ow%3D%3D"),
  "brtcCode": "26",
  "signguCode": "710",
  "numOfRows": "10000000000",
  "pageNo": 1,
  "dataType": "JSON"
}
)

queryURL = url + queryString
response = urllib.request.urlopen(queryURL)
json_str = response.read().decode("utf-8")
json_object = json.loads(json_str)
hsmpList = [json_object['hsmpList']]

df_house = pd.DataFrame(json_object['hsmpList'])
df_house.to_csv('house_기장군.csv',encoding=' utf-8-sig')


