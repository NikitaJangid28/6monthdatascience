import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost",database='radhey')

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")

mycursor = conn.cursor()

query = """
create table userdata 
(name varchar(30),gmail varchar(30),contact varchar(14),password varchar(30))
"""


mycursor.execute(query)
print("your table is  created!")



mycursor.close()
conn.close()

