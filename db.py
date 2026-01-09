import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AsUsZeNSHOR2026#",
        database="todo_app"
    )
