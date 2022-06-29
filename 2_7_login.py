
def generate_login_id(f_name,l_name,dob):
    user_id = f_name[0:3]+"@"+l_name[-3:]
    password= f_name[0:4]+"_"+dob

    return user_id,password

first_name = input("Enter the first name : ")
last_name = input("Enter the last name : ")
dob = input("Enter the Date of birth : ")

user_id,password = generate_login_id(first_name,last_name,dob)

print("User ID : ",user_id)
print("Password : ",password)