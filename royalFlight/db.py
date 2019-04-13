import mysql.connector

mydb = mysql.connector.connect(
    database='royalflight',
    host="localhost",
    port="3307",
    user="root",
    passwd=""
)
