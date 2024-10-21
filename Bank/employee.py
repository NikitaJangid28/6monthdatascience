# import manager
# import os 
# import csv 
# import json 
# import mysql 
# import sys  
# print("successfully imported!")


# import manager 

# manager.show_anshika_details()
# print()
# print(manager.employe_name)



# how we can define alias to the module 
# import manager as mng 
# print(mng.employe_name)



# import manager 
# print(manager.manager_id)
# print(manager.manager_password)




# how we can import specific content from the module 
# from manager import employe_name
# from manager import employee_id,employee_pass,employee_salary

# print(employe_name)
# print(employee_id)
# print(employee_pass)
# print(employee_salary)


from manager import employe_name as name 
from manager import employee_id as id 
from manager import employee_pass as password 
print(name,id,password )
