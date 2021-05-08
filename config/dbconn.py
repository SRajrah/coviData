import mysql.connector

def connectDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="MARVEL"
    )
    return mydb


