"""
User Input
"""
# first_name=input("Enter your first name: ")
# days=input("How many days before your birthday: ")
# print(f"Hi {first_name}, only {days} days before your birthday!")

"""
String Assignment
Ask the user how many days untill their birthday and print an approx no of weeks untill their birthday
Weeks is 7days
"""
# convert string to integer
daysTillBirthday=int(input('Enter days until birthday'))
print('type(daysTillBirthday)',type(daysTillBirthday))
print('weeks is',round(daysTillBirthday/7))