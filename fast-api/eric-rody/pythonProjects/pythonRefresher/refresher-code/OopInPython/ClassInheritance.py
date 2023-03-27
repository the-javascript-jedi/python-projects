# Inheritance
class Student:
    number_of_students=0
    school='Online School'
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name = last_name

    def greetings(self):
        return f'Hello! I am {self.first_name} {self.last_name}'
# sub class
# CollegeStudent will inherit all methods of the parent class
class CollegeStudent(Student):
    # we type pass so no errors are thrown for an empty class
    # pass
    def __init__(self,first_name,last_name,major):
        # super() - call the parent class functions
        super().__init__(first_name,last_name)
        # add a new field to the class
        self.major = major
    # since same name as parent, the child method is executed
    def greetings(self):
        return f'{self.first_name} is a college student'
# sub class referring from clas Student
class NonCollegeStudent(Student):
    def __init__(self,first_name,last_name,future_adult_job):
        super().__init__(first_name,last_name)
        self.future_adult_job=future_adult_job
    def grow_up(self):
        return f'When I grow up, I want to be a {self.future_adult_job}'

# object of CollegeStudent will require a major variable
student_1 = CollegeStudent('Eric', 'Roby','Computer Science')
print("student_1.greetings()",student_1.greetings())

student_2 = NonCollegeStudent('John', 'Miller','Doctor')
print("student_2.greetings()",student_2.greetings())
print("student_2.grow_up()",student_2.grow_up())