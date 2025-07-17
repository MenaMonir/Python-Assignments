                                    #   Name  : -     Mena Monir Helal
                                    #   Course: -       Python & AI
                                    #             The 6th Assignment (Pandas)

# Task No.(1) Basic Operations with Pandas
#             Objective:
#                       Practice creating DataFrames, accessing data, and performing basic operations using Pandas.

print("---/ (Import Pandas) /---")                      # ---/ (Import Pandas) /---
import pandas as pd

print("---/ (Create a DataFrame) /---")                 # ---/ (Create a DataFrame) /--- 
import pandas as pd
data = [["Alice",20,'A',85],["Bob",22,'B',78],["Charlie",19,'A',92],["David",21,'C',65],["Eva",20,'B',74]]
students_data = pd.DataFrame(data,columns=["Name","Age","Grade","Marks"]) 
print(students_data)


print("---/ (Access Data) /---")                        # ---/ (Access Data) /---

print("--/Display the first 3 rows of the DataFrame/--")
print(students_data.head(3))

print("--/Select and display only the (Name) and (Marks) columns./--")
print(students_data[['Name','Marks']])

print("--/Filter and show the students who have a grade of 'A'/--")

Students_Grade_A = students_data[students_data['Grade']=='A']  # Filter
print(Students_Grade_A)