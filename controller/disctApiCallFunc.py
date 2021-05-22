from config.dbconn import queryResult
from controller.covidNotifications import getDataByDistrictWeekly, getDataByDistrictWeeklyDummy
from time import sleep

def realCall():
    calls = 10
    #get flag zero count
    queryCount = "select count(*) from my_udata where flag_call = 0 and status = 0"
    countFlagZero = queryResult(queryCount)[0][0]

    #get distinct district count
    queryDisCount = "select count(distinct district_id) from my_udata where status = 0"
    countDistrict = queryResult(queryDisCount)[0][0]
    print("Count DIS-", countDistrict)
    print("count Flag zero-", countFlagZero)

    if countFlagZero >= calls:
        disList1 = []
        disQuery1 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 0 and status = 0 LIMIT " + str(calls)
        disObject1 = queryResult(disQuery1)

        for i in disObject1:
            disList1.append(i[0])
            #print(i[0])
        print("if LIST1", disList1)

        leftQuery = []
        if countDistrict != calls:
            for districtId in disList1:
                status = getDataByDistrictWeeklyDummy(districtId)
                print(status)
                if status == 200:
                    leftQuery.append("'" + districtId + "'")

            print(leftQuery)
            leftQueryString = ",".join(leftQuery)
            print(leftQueryString)
            if len(leftQuery) != 0:
                queryUpFlagOne = "UPDATE my_udata SET flag_call = 1 WHERE status = 0 and district_id IN ( " + leftQueryString + " )"
                print(queryUpFlagOne)
                queryUpFlagResult = queryResult(queryUpFlagOne)
                print(queryUpFlagResult)

        else:
            for districtId in disList1:
                status = getDataByDistrictWeeklyDummy(districtId)
                print("first else status-", status)
    else:
        if countDistrict > calls:
            # get List1
            disList1 = []
            disQuery1 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 0 and status = 0"
            disObject1 = queryResult(disQuery1)
            for i in disObject1:
                disList1.append(i[0])
                print(i[0])

            # get List2
            disList2 = []
            disQuery2 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 1 and status = 0 LIMIT " + str(calls - countFlagZero)
            disObject2 = queryResult(disQuery2)
            for i in disObject2:
                disList2.append(i[0])
                print(i[0])

            finalDisList = disList1 + disList2
            print("dis>calls -> finalList", finalDisList)
            leftQuery = []
            # for all elements in final list call api
            for districtId in finalDisList:
                status = getDataByDistrictWeeklyDummy(districtId)
                print(status)
                if status == 200:
                    leftQuery.append("'" + districtId + "'")

            print(leftQuery)
            leftQueryString = ",".join(leftQuery)
            print(leftQueryString)
            if len(leftQuery) != 0:
                queryUpFlagOne = "UPDATE my_udata SET flag_call = 0 WHERE status = 0 and district_id NOT IN ( " + leftQueryString + " )"
                print(queryUpFlagOne)
                queryUpFlagResult = queryResult(queryUpFlagOne)
                print(queryUpFlagResult)

        if countDistrict < calls:

            #check if count of calls is more than twice the districts
            if calls > 2*countDistrict:
                disList1 = []
                multiDisList1 = []
                disQuery1 = "SELECT DISTINCT district_id FROM my_udata WHERE status = 0"
                disObject1 = queryResult(disQuery1)
                for i in disObject1:
                    disList1.append(i[0])
                    print(i[0])
                for j in range(0, calls // countDistrict):
                    multiDisList1 = multiDisList1 + disList1

                disList2 = []
                disQuery2 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 0 and status = 0 LIMIT " + str(calls % countDistrict)
                disObject2 = queryResult(disQuery2)
                for i in disObject2:
                    disList2.append(i[0])
                    print(i[0])

                if len(disObject2) == 0:
                    queryUpFlagZero = "UPDATE my_udata SET flag_call = 0 WHERE status = 0"
                    print(queryUpFlagZero)
                    queryUpFlagZeroResult = queryResult(queryUpFlagZero)
                    sleep(5)
                    disQuery2 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 0 and status = 0 LIMIT " + str(calls % countDistrict)
                    disObject2 = queryResult(disQuery2)
                    for i in disObject2:
                        disList2.append(i[0])
                        print(i[0])

                finalDisList = multiDisList1 + disList2
                print("dis<calls -> finalList", finalDisList)
                leftQuery = []
                # for all elements in final list call api
                for districtId in finalDisList:
                    status = getDataByDistrictWeeklyDummy(districtId)
                    print(status)
                    if status == 200:
                        if districtId in disList2:
                            leftQuery.append("'" + districtId + "'")

                print(leftQuery)
                leftQueryString = ",".join(leftQuery)
                print(leftQueryString)
                if len(leftQuery) != 0:
                    queryUpFlagOne = "UPDATE my_udata SET flag_call = 1 WHERE status = 0 and district_id IN ( " + leftQueryString + " )"
                    print(queryUpFlagOne)
                    queryUpFlagResult = queryResult(queryUpFlagOne)
                    print(queryUpFlagResult)

            #if calls is less than twice the districs
            else:
                # get dictionary1
                disList1 = []
                disQuery1 = "SELECT DISTINCT district_id FROM my_udata WHERE status = 0"
                disObject1 = queryResult(disQuery1)
                for i in disObject1:
                    disList1.append(i[0])
                    print(i[0])

                # get dictionary2
                disList2 = []
                disQuery2 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 0 and status = 0 LIMIT " + str(calls - countDistrict)
                disObject2 = queryResult(disQuery2)
                for i in disObject2:
                    disList2.append(i[0])
                    print(i[0])

                if len(disList2) == 0:
                    queryUpFlagZero = "UPDATE my_udata SET flag_call = 0 WHERE status = 0"
                    print(queryUpFlagZero)
                    queryUpFlagZeroResult = queryResult(queryUpFlagZero)
                    sleep(5)
                    disQuery2 = "SELECT DISTINCT district_id FROM my_udata WHERE flag_call = 0 and status = 0 LIMIT " + str(calls - countDistrict)
                    disObject2 = queryResult(disQuery2)
                    for i in disObject2:
                        disList2.append(i[0])
                        print(i[0])

                finalDisList = disList1 + disList2
                print("dis<calls -> finalList", finalDisList)
                leftQuery = []
                # for all elements in final list call api
                for districtId in finalDisList:
                    status = getDataByDistrictWeeklyDummy(districtId)
                    print(status)
                    if status == 200:
                        if districtId in disList2:
                            leftQuery.append("'" + districtId + "'")

                print(leftQuery)
                leftQueryString = ",".join(leftQuery)
                print(leftQueryString)
                if len(leftQuery) != 0:
                    queryUpFlagOne = "UPDATE my_udata SET flag_call = 1 WHERE status = 0 and district_id IN ( " + leftQueryString + " )"
                    print(queryUpFlagOne)
                    queryUpFlagResult = queryResult(queryUpFlagOne)
                    print(queryUpFlagResult)




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
