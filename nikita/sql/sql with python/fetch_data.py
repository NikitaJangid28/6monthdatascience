import mysql.connector as mc 
conn = mc.connect(user='root',password="Radhey254875",host="localhost",database='radhey')
mycursor = conn.cursor(buffered=True)

query = "select * from userdata"

mycursor.execute(query) 

# mycursor.fetchall()
# mycursor.fetchmany()
# mycursor.fetchone()    

# single_row  = mycursor.fetchone()
# print(single_row)



# all_rows = mycursor.fetchall() 

# for row in all_rows:
#     print(row)

multiple_row = mycursor.fetchmany(3)
print(multiple_row)


mycursor.close()
conn.close()
