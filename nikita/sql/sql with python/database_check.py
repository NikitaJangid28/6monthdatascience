import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost")

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")



query = "show databases"
mycursor = conn.cursor()
mycursor.execute(query)
# cursor object ---> where temporary memory 
for db in mycursor:
    print(db)

mycursor.close()
conn.close()

