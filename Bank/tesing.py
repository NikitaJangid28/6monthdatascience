# from branch.branch_details import branch_name
# from branch.branch_details import branch_address

# # from substaff.electrician_staff import * 
# from substaff.electrician_staff import electrician_name as el_name
# print(branch_name)
# print(branch_address)

# print(el_name)
# print(electrician_salary)



from branch.branch_details import branch_name 
from branch.sub_branch.sub_branch import sub_branch_name

from substaff.electrician_staff import electrician_name, electrician_salary


print("Your main branch is : ",branch_name)
print("your sub branch name is : ",sub_branch_name) 

print("your electrician name is : ",electrician_name)
print("salary of electrician is : ",electrician_salary)