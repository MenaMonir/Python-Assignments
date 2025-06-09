                                    #   Name  : -     Mena Monir Helal
                                    #   Course: -       Python & AI
                                    #                The 2st Assignment

# Task No.(1) Create a Contact Book
# This is a Python program that Print all the names in the contact book
# and allow the user to search for a contact by name and print the associated phone

contacts = {
             "Ali":"01221138560",
             "Mena":"01221138561",
             "Mohand":"01221138562",
             "Mark":"0121138563",
             "Malek":"01221138564"
}
print(contacts)
# Now we will make an another dictionary for (3) new contacts
new_contacts = {
             "Lyla":"01221138565",
             "Malak":"01221138566",
             "Moka":"01221138567"             
}
print(new_contacts)

# We will add them to the first dictionary
contacts.update(new_contacts) 
print("This is the new contacts book \n",contacts)

# To print all contacts in the book
print("These are all contacts in the book \n", contacts.keys())

# Now you can select any contact to get his phone number
req_phone = input("Please, select the contact that you need (his/her) phone number \n")
print(contacts[req_phone])

#.........................................................................................................
print("Sloution of task (2)")

# Task No.(2) Student Grades

# This program Creates a list of dictionaries where each dictionary represents a student with:
#           o A name key (string) for the student's name.
#           o A grades key (list of integers) for their grades in three subjects.

# Write a script to:
#           o Calculate the average grade for each student.
#           o Print the name and average grade for each student.

# First we will Create a list of student dictionaries
students = [
    {"name": "Alic", "grades": [87, 95, 73]},
    {"name": "Lina", "grades": [80, 89, 92]},
    {"name": "Tiffany", "grades": [93, 80, 96]}
]

# then we will Calculate and print average grade for each student
for student in students:
    name = student["name"]
    grades = student["grades"]
    avg = sum(grades) / len(grades)
    print(f"{name}'s avg grade is {avg}")