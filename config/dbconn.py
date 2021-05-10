import mysql.connector

def connectDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="MARVEL"
    )
    return mydb

def queryResult(query):
    myconn = connectDB()
    mycursor = myconn.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

