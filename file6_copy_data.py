#copy data of file into another file
org_file = input(" Enter the name of file : ")
copy_file = input(" Enter the name of duplicate file : ")

with open (org_file,"r") as org_obj:
    with open (copy_file,"w") as copy_obj:
        text = org_obj.read()
        copy_obj.write(text)

org_obj.close()
copy_obj.close()


#org_file = input(" Enter the name of file : ")
#copy_file = input(" Enter the name of duplicate file : ")

#with open (org_file,"r") as org_obj:
#    text = org_obj.read()
#with open (copy_file,"w") as copy_obj:
#    for line in text:
#        copy_obj.write(line)
        
#org_obj.close()
#copy_obj.close()



# Code 2  :

org_file = input(" Enter the name of file : ")    #org_file = input(" Enter the name of file : ")
copy_file = input(" Enter the name of duplicate file : ")

with open (org_file,"r") as org_obj:
    with open (copy_file,"w") as copy_obj:
        text = org_obj.read()
        for line in text:
            if(line[0]=='#'):
                pass
            else:
                org_obj.readline()
                copy_obj.write(line)    #org_file = input(" Enter the name of file : ")
org_obj.close()
copy_obj.close()