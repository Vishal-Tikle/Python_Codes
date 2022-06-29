org_file = input(" Enter the name of file : ")
copy_file = input(" Enter the name of duplicate file : ")

with open (org_file,"r") as org_obj:
    with open (copy_file,"w") as copy_obj:
        text = org_obj.read()
        for line in text:
            if(line[0]=="#"):
                continue
            else:
                copy_obj.write(line)
org_obj.close()
copy_obj.close()


# Sir
org_file = input(" Enter the name of file : ")
copy_file = input(" Enter the name of duplicate file : ")

with open (org_file,"r") as org_obj:
    with open (copy_file,"w") as copy_obj:
        while True:                               # infinite loop
            line = org_obj.readline() 
            if len(line) != 0 :
                if(line[0]=="#"):
                    continue
                else:
                    copy_obj.write(line)
            else:
                break
org_obj.close()
copy_obj.close()