import requests
import smtplib
import json
pincodes = [""]

def getUniquePincodes():
    #sql query to get distinct pincodes
    for singlePin in pincodes:
        getDataByPincodeDaily(singlePin)



def getDataByPincodeDaily(pincode = 180001):
    paramDict = {
        'pincode': pincode,
        'date': '10-05-2021'}
    my_headers = {
        'Accept-Language': 'hi_IN',
        'Accept': 'application/json',
        'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
    response = requests.get(url, params=paramDict, headers=my_headers)
    vaccineDataString = str(response.json())
    vaccineData = json.loads(vaccineDataString.replace("\'", "\""))
    availableCentres = []
    if vaccineData["sessions"]!="[]":
        vaccineCentreDicts = vaccineData["sessions"]
        for info in vaccineCentreDicts:
            if info['available_capacity'] > 0:
                availableCentres.append(info)

    if len(availableCentres)!=0:
        #sql to get all users under this pincode
        # address -
        for eachMember in memberList:
            emailAlert(subject,message,to)













def getDataByPincodeWeekly(pincode):
    paramDict = {
        'pincode': '180001',
        'date': '10-05-2021'}
    my_headers = {
        'Accept-Language': 'hi_IN',
        'Accept': 'application/json',
        'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
    response = requests.get(url, params=paramDict, headers=my_headers)
    print(response.json())

def getDataByDistrictDaily(districtID):
    paramDict = {
        'district_id': '180001',
        'date': '10-05-2021'}
    my_headers = {
        'Accept-Language': 'hi_IN',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
    response = requests.get(url, params=paramDict, headers=my_headers)
    print(response.json())

def getDataByDistrictWeekly(districtID):
    paramDict = {
        'district_id': '180001',
        'date': '10-05-2021'}
    my_headers = {
        'Accept-Language': 'hi_IN',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    response = requests.get(url, params=paramDict, headers=my_headers)
    print(response.json())

getDataByPincodeDaily()

