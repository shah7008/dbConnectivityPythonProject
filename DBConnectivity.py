import mysql.connector

def fetchstudentData():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_managment_with_python"
        )
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM student_info")
        rows = mycursor.fetchall()
        print("Student data fetched successfully")
        return rows
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed")