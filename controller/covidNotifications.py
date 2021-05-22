import requests
import smtplib
import json
from datetime import date

today = date.today()
dateToday = today.strftime("%d-%m-%Y")

def calcTimeCall(c):
    return c*0.05

def getUniquePincodes():
    #sql query to get distinct pincodes
    #sql query to get distinct district Ids
    for singlePin in pincodes:
        getDataByPincodeDaily(singlePin)
    countDistinctDis = "qyery"
    sleepTime = calcTimeCall(countDistinctDis)
    while True:
        for singleDistrict in districts:
            getDataByDistrictWeekly(singleDistrict)

        sleep(sleepTime)


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
    vaccineDataString = str(response.json())
    vaccineData = json.loads(vaccineDataString.replace("\'", "\""))
    availableCentres = []
    if vaccineData["sessions"] != "[]":
        vaccineCentreDicts = vaccineData["sessions"]
        for info in vaccineCentreDicts:
            if info['available_capacity'] > 0:
                availableCentres.append(info)

    if len(availableCentres) != 0:
        # sql to get all users under this pincode
        # address -
        emailMessage = """Dear user \n We have an important update for you. New vaccine slots have been added in your area. 
            \nThe information is as provided below. Please make sure to register right away before the slots get exhausted.\n"""
        for eachCentre in availableCentres:

            address = eachCentre['address'] + ','+eachCentre['block'] + ','+eachCentre['district'] + ',' + eachCentre['state'] + '-' + eachCentre['pincode'] + '\n'
            vaccine = eachCentre['vaccine'] + '\n'
            availableSlot = eachCentre['slots'] + '\n'
            capacity = eachCentre['available_capacity'] + '\n'
            fee = eachCentre['fee_type']
            ageLimit = eachCentre['min_age_limit']


        for eachMember in memberList:
            emailAlert(subject, emailMessage, to)

def getDataByDistrictWeekly(districtID):
    paramDict = {
        'district_id': districtID,
        'date': dateToday}
    my_headers = {
        'Accept-Language': 'hi_IN',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    response = requests.get(url, params=paramDict, headers=my_headers)
    print(response.json())
    vaccineDataString = str(response.json())
    vaccineData = json.loads(vaccineDataString.replace("\'", "\""))
    availableCentres = []
    if vaccineData["sessions"] != "[]" and response.status_code == 200:
        vaccineCentreDicts = vaccineData["sessions"]
        for info in vaccineCentreDicts:
            if info['available_capacity'] > 0:
                availableCentres.append(info)

    if len(availableCentres) != 0:
        # sql to get all users under this pincode
        # address -
        emailMessage = """Dear user \n We have an important update for you. New vaccine slots have been added in your area. 
                \nThe information is as provided below. Please make sure to register right away before the slots get exhausted.\n"""
        for eachCentre in availableCentres:
            address = eachCentre['address'] + ',' + eachCentre['block'] + ',' + eachCentre['district'] + ',' + \
                      eachCentre['state'] + '-' + eachCentre['pincode'] + '\n'
            vaccine = eachCentre['vaccine'] + '\n'
            availableSlot = eachCentre['slots'] + '\n'
            capacity = eachCentre['available_capacity'] + '\n'
            fee = eachCentre['fee_type']
            ageLimit = eachCentre['min_age_limit']

        for eachMember in memberList:
            emailAlert(subject, emailMessage, to)

def getDataByDistrictWeeklyDummy(disctrictId):
    callDict = {
        '230': 200,
        '210': 200,
        '211': 200,
        '212': 200,
        '213': 200,
        '214': 200,
        '215': 200,
        '216': 200,
        '217': 200
    }
    return callDict[disctrictId]

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
    vaccineDataString = str(response.json())
    vaccineData = json.loads(vaccineDataString.replace("\'", "\""))
    availableCentres = []
    if vaccineData["sessions"] != "[]" and response.status_code == 200:
        vaccineCentreDicts = vaccineData["sessions"]
        for info in vaccineCentreDicts:
            if info['available_capacity'] > 0 and info['min_age_limit'] == 18:
                availableCentres.append(info)

    if len(availableCentres) != 0:
        # sql to get all users under this pincode
        # address -
        emailMessage = """Dear user \n We have an important update for you. New vaccine slots have been added in your area. 
                \nThe information is as provided below. Please make sure to register right away before the slots get exhausted.\n"""
        for eachCentre in availableCentres:
            sessionList = []
            address = eachCentre['address'] + ',' + eachCentre['block'] + ',' + eachCentre['district'] + ',' + \
                      eachCentre['state'] + '-' + eachCentre['pincode'] + '\n'
            vaccine = eachCentre['vaccine'] + '\n'
            availableSlot = eachCentre['slots'] + '\n'
            capacity = eachCentre['available_capacity'] + '\n'
            fee = eachCentre['fee_type']
            ageLimit = eachCentre['min_age_limit']
            singleSession = [address, vaccine, availableSlot, capacity, fee, ageLimit]
            sessionList.append(singleSession)

        for eachMember in memberList:
            emailAlert(subject, emailMessage, to)


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
