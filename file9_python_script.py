#for removing comment in python script

org_file = input(" Enter the name of file : ")
copy_file = input(" Enter the name of duplicate file : ")
# comment
with open (org_file,"r") as org_obj:
    with open (copy_file,"w") as copy_obj:
        while True:                               # infinite loop
            line = org_obj.readline() 
            if len(line) != 0 :
                for char in line:
                        if(char in "#"):
                            copy_obj.write("\n")
                            break
                        else:
                            copy_obj.write(char)
            else:
                break
org_obj.close()
# comment
copy_obj.close()