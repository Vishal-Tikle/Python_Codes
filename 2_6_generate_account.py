#first 3 of first name and first 3 of last name

def generate_account(first_name , last_name):
    return(first_name[0:3]+last_name[0:3])                      #                             VISTIK
    #return(first_name[0:3]+"_"+last_name[0:3])                 with underscoll(_)            VIS_TIK

first_name = input(" Enter the first name : ")            #VISHAL
last_name = input( " Enter the last name : ")             #TIKLE
account_name = generate_account(first_name , last_name)

print(" Account name is ",account_name)



# last 3 of first name and last 3 of last name

#def generate_account(first_name , last_name):
#    return(first_name[-3:]+last_name[-3:])                                                   