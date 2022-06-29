roll_no = []
name = []
section = []
student = {}
#for x in range(0,len(roll_no)):
for x in range(0,5):
    roll_no.append(input("Enter the Roll no : "))
    name.append(input("Enter the Name : "))
    section.append(input("Enter the section : "))# OR
    #for x in range(0,len(roll_no)):
for x in range(0,len(roll_no)):
    student[x]=dict([('Roll no',roll_no[x]),('Name',name[x]),('Section',section[x])])

for x in range(0,len(roll_no)):
    print(student[x])





#    print(dict([('Roll no',roll_no[x]),('Name',name[x]),('Section',section[x])]))

