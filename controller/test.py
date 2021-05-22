import urllib.request
from controller.covidNotifications import getDataByDistrictWeekly, getDataByDistrictWeeklyDummy

url = "https://www.google.com"

status_code = urllib.request.urlopen(url).getcode()
print(status_code)
website_is_up = status_code == 200

print(website_is_up)

dict1 = {"230": "", "210": ""}

dict2 = {"240": "", "250": ""}

calls = 5
countDistrict = 2
disObject1 = [1, 2]
newlist = []
print("----------------------",calls // countDistrict)
print("----------------------",calls % countDistrict)

for j in range(0, calls // countDistrict):
    print(j)
    newlist = newlist + disObject1
    print(newlist)

print(disObject1)

