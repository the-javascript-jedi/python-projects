# # class instantiation using an object
# class Student:
#     pass
#
# student_1 = Student()
# student_2 = Student()
#
# student_1.first_name='Eric'
# student_1.last_name='Roby'
# student_1.major='Computer Science'
#
# student_2.first_name='John'
# student_2.last_name='Miller'
# student_2.major='Math'
#
# print('student_1',student_1.first_name)
# print('student_2',student_2.first_name)

# Initialize a class with values when we create it
# self is the instance of itself
class Student:
    number_of_students=0
    school='Online School'
    def __init__(self,first_name,last_name,major):
        self.first_name=first_name
        self.last_name = last_name
        self.major = major
        # increment the no of students each time object is instantiated
        Student.number_of_students+=1
    #  define a function inside the class
    def fullname_with_major(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major!"
    def fullname_major_school(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major going to {self.school}"
    #change the variable specified inside the class
    @classmethod
    def set_online_school(cls,new_school):
        cls.school=new_school
# change no of students
print(f'Before Initiation--Number of students={Student.number_of_students}')
student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John','Miller','Math')
print(f'After Initiation--Number of students={Student.number_of_students}')
# change school string specified in class for all instances
print('student_1.school',student_1.school)
Student.set_online_school('I use google hangouts')
print('student_1.school',student_1.school)

# print('student_1.fullname_major_school()',student_1.fullname_major_school())
# print('student_2.fullname_major_school()',student_2.fullname_major_school())

# pass values to the class
# student_1 = Student('Eric','Roby','Computer Science')
# student_2 = Student('John','Miller','Math')
# print('student_1.first_name',student_1.first_name)
# print('student_1.fullname_with_major()',student_1.fullname_with_major())
# print('student_2',student_2.first_name)
# # we can also pass the data to the function to be executed
# # instead of creatng a class we directly pass the data to the class
# print('Student.fullname_with_major(student_2)',Student.fullname_with_major(student_2))

