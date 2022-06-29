choice ='Y'
while choice == 'Y':
    print("\n Enter the details of Student are as follows : \n")
    name = input (" Name of student : ")
    roll_no = int (input(" Roll no. : "))
    year = int (input(" Year : "))
    dept = input(" Department : ")

    print("\n Enter the marks obtained by the student in following subjects : \n")
    pp = int(input(" Python programming : "))
    sp = int(input(" Signal Proccessing : "))
    emf = int(input(" Eletromagnetic field : "))
    m4 = int(input(" Mathematics IV : "))
    ss = int(input(" Soft Skill-1 : "))
    oe= int(input(" Open elective - 1 : "))

    total_marks=pp+sp+emf+m4+ss+oe
    percentage = (total_marks / 6)

    if percentage > 85 :
        grade = 'A+'
    elif percentage >75 and percentage < 85 :
        grade = 'A'
    elif percentage > 60  and percentage < 75:
        grade = 'B'
    elif percentage > 50  and percentage < 60:
        grade = 'c'
    elif percentage > 40  and percentage < 50:
        grade = 'D'
    else:
        grade='F'

    print("\n########################################################")
    print("\tS B JAIN INSTITUDE OF TECHNOLOGY, NAGPUR")
    print("########################################################\n")
    print(" Name of Student\t:",name)
    print(" Year\t\t\t:",year)
    print(" Department\t\t: ",dept)
    print(" Roll No\t\t:",roll_no)
    print("\n########################################################")
    print(" \t\t\tMARKSHEET ")
    print("########################################################")
    print(" Subjects\t\t Marks \n")
    print(" Python programming\t: ",pp)
    print(" Signal Proccessing\t: ",sp)
    print(" Eletromagnetic field\t: ",emf)
    print(" Mathematics IV\t\t: ",m4)
    print(" Soft Skill-1\t\t: ",ss)
    print(" Open elective - 1\t: ",oe)
    print("---------------------------------------------------------")
    print(" Total Marks\t\t: ",total_marks)
    print(" Percentage\t\t: ",percentage)
    print(" Grade \t\t\t: ",grade)
    print("########################################################")
    choice = input(" Do want to continue Y/N : ")