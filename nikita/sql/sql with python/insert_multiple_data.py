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
# [() , ()  , ()]

userdata = [('rajendra jangid', 'rajend@gmail.com','546679446','raj@43'),
            ('sachin','sachin@gmail.com','54464652','sachin@3r34'),
            ('rahul','rahul@gmail.com','654646545','rahul3434')]

mycursor.executemany(query,userdata)
conn.commit()
print("your data is inserted")


mycursor.close()
conn.close()

