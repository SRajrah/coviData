def vaccineNotification():

    if request.method == "POST":
        # i = 0
        # while i < 10:
        #     i = i+1
        #     message = "get data -" + str(i)
        #     time.sleep(10)
        print("sometin")
        myconn = connectDB()
        mycursor = myconn.cursor()

        mycursor.execute("SELECT * FROM myudata LIMIT 3,5")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    return render_template("VaccineNotification.html")

def notificationData():
    # i = 0
    # while True:
    #     i = i+1
    #     message = "get data -" + str(i)
    #     print(message)
    #     time.sleep(2)
    return render_template("VaccineNotification.html")