import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost",database='radhey')

if conn.is_connected():
    print("you are successully connected!")
else:
    print("unable to connect!")

mycursor = conn.cursor()

query = """
INSERT INTO userdata (name ,gmail, contact ,password)
VALUES ('Ranjit','ranjit654@gmail.com','9685654655','ranjit@123')
"""

mycursor.execute(query)
conn.commit()
print("your data is inserted")


mycursor.close()
conn.close()

