class Person:
    '''Person class acting as base for Student'''
    
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
class Student(Person):
    """Child class"""
    
    def __init__(self, fname,lname,student_id):
        Person.__init__(self, fname, lname)
        self.id = int(student_id)
        
        
    def calculate(self,grades):
        """This function calculates average grade"""
        average = ((sum(grades))/(len(grades)))
        print(average)
        
        
person1 = Student(str(input("First name: ")),str(input("Last name: ")), int(input("Student ID: ")))
grades = input("Enter a list of grades separated by space: ")
grades = list(map(int, grades.split()))
person1.calculate(grades)

 