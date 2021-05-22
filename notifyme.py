from localEmails import emailAlert

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
        subject = "Vaccine Slots available- Hurry!"
        # sql to get all users under this pincode
        # address -
        emailMessage = """Dear user \n We have an important update for you. New vaccine slots have been added in your area. 
                \nThe information is as provided below. Please make sure to register right away before the slots get exhausted.\n"""
        serial = 0
        for eachCentre in availableCentres:
            sessionList = []
            serial = serial + 1
            address = eachCentre['address'] + ',' + eachCentre['block'] + ',' + eachCentre['district'] + ',' + \
                      eachCentre['state'] + '-' + eachCentre['pincode'] + '\n'
            vaccine = eachCentre['vaccine'] + '\n'
            availableSlot = eachCentre['slots'] + '\n'
            capacity = eachCentre['available_capacity'] + '\n'
            fee = eachCentre['fee_type']
            ageLimit = eachCentre['min_age_limit']
            singleSession = [serial, address, vaccine, availableSlot, fee, capacity, ageLimit]
            sessionList.append(singleSession)

        for eachMember in memberList:
            emailAlert(subject, emailMessage, to, bcc)


if __name__ == "__main__":
    districtId = 219
    while True:
        getDataByDistrictDaily(districtId)