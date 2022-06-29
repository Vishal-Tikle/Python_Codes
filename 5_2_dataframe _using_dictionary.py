import pandas as pd
student = {"Name":["Vishal","Atharv","Sanket"],
            "Roll No ":[44,57,43],
            "Year":[2,2,2],
            "section":['A','A','B']}
student_details = pd.DataFrame(student)
print(student_details)