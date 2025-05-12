import mysql.connector



mydb = mysql.connector.connect(
  host="db4free.net",
  user="stdmgm",
  password="*$=VJ7\"xVw8b^}n",
  database="studentmanage"

)

def fetchstudentData():
  try:
    print(mydb)

    mycursor = mydb.cursor()
    mycursor.execute("select * from student")
    rows=mycursor.fetchall()
    for students in mycursor:
      print(students)
  except Exception as e:
    print(e)

  finally:
    mydb.close()
    return rows