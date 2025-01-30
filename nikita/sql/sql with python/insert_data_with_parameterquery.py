import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost",database='radhey')

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")

mycursor = conn.cursor()

# parameterized 
query = """
INSERT INTO userdata (name ,gmail, contact ,password)
VALUES (%s,%s,%s,%s)
"""

userdata = ('nikita jangid', 'nikki@gmail.com','4654879446','nikk@43')

mycursor.execute(query,userdata)
conn.commit()
print("your data is inserted")


mycursor.close()
conn.close()

