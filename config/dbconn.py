import MySQLdb
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
    try:
        mycursor.execute(query)
        result = mycursor.fetchall()
        myconn.commit()
        print(mycursor.rowcount, "record(s) affected")
        myconn.close()
        return result
    except mysql.connector.Error as err:
        print(err)
