from config.dbconn import connectDB
from config.dbconn import queryResult
from controller.covidNotifications import getDataByDistrictWeekly
offset = 4

queryCount = "select count(*) from myudata where flag_call = 0"
countFlagZero = queryResult(queryCount)[0][0]

queryDisCount = "select count(distinct district_id) from myudata"
countDistrict = queryResult(queryDisCount)[0][0]

if countFlagZero >= offset:
    disList1 = []
    disQuery1 = "SELECT DISTINCT district_id FROM myudata WHERE flag_call = 0 LIMIT " + str(offset)
    disObject1 = queryResult(disQuery1)

    for i in disObject1:
        disList1.append(i[0])
        print(i[0])

    if countDistrict != offset:
        queryUpFlagOne = "UPDATE myudata SET flag_call = 1 WHERE district_id IN ( SELECT DISTINCT district_id FROM myudata WHERE flag_call = 0 LIMIT " + str(offset) + ")"

    for districtId in disList1:
        #getDataByDistrictWeekly(districtId)



print(countFlagZero)
print(disList1)

# for x in myresult:
#     lastPos = x[0]
#     left = x[1]
#     print(lastPos, left)
#
# mycursor1 = myconn.cursor()
# mycursor1.execute("select count(*) from myudata")
# tcount = mycursor1.fetchall()
# totalItems = tcount[0][0]
#
# for i in range(10):
#     if left == totalItems:
#         limit = str(lastPos) + ',' + str(offset)
#         mycursor2 = myconn.cursor()
#         query = "SELECT * FROM ACESS_DATA LIMIT " + limit
#         mycursor2.execute(query)
#         myresult2 = mycursor2.fetchall()
#         for y in myresult2:
#             print(y)
#         lastPos = lastPos + offset
#         left = totalItems - offset
#     else:
#         limit = str(lastPos) + ',' + str(offset)
#         mycursor2 = myconn.cursor()
#         query = "SELECT * FROM ACESS_DATA LIMIT " + limit
#         mycursor2.execute(query)
#         myresult2 = mycursor2.fetchall()
#         for y in myresult2:
#             print(y)
#         query1 =
#
# print(query)
# #mycursor.execute()
#
