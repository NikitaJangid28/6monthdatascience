import mysql.connector as mc 
conn = mc.connect(user='Admin',password="Pass@12345",host="13.61.11.40")

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")
