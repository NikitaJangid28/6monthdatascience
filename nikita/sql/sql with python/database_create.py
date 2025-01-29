import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost")

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")

mycursor = conn.cursor()


mycursor.execute("create database radhey")
print("your database is  created!")


mycursor.close()
conn.close()

