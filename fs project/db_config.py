import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # use your MySQL username
        password="yourpass", # use your MySQL password
        database="attendance_db"
    )
