import mysql.connector as mc 
conn = mc.connect(user='Admin',password="Password123!",host="16.171.3.98")

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")
