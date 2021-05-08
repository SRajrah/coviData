import requests
import json
from config.db

def getDistrictData(stateName, stateId):
    my_headers = {
            'Accept-Language': 'hi_IN',
            'Accept': 'application/json',
            'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+stateId
    response = requests.get(url, headers=my_headers)
    districtDataString = str(response.json())
    districtData = json.loads(districtDataString.replace("\'", "\""))
    if districtData['districts']!='[]':
        districtInfo = districtData['districts']
        for eachDistrict in districtInfo:
            districtName = eachDistrict['district_name']
            districtID = eachDistrict['district_id']

            #stateId, stateName, districtName, DistrictId






def getStateData():
    my_headers = {
        'Accept-Language': 'hi_IN',
        'Accept': 'application/json',
        'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    response = requests.get(url, headers=my_headers)
    stateDataString = str(response.json())
    stateData = json.loads(stateDataString.replace("\'", "\""))
    if stateData["states"] != "[]":
        stateInfo = stateData["states"]
        for stateInfo in stateInfo:
            stateId = stateInfo['state_id']
            stateName = stateName['state_name']
            getDistrictData(stateName,stateId)


