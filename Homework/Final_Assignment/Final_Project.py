# Student Class:
print()
class Student:
    #Our constructor.
    def __init__(self):
        #Storing the student's name.
        name=input("What is the student's name? ")
        self.name=name
        #Storing the school's name.
        schoolName=input("What is the school's name?  ")
        self.schoolName=schoolName
    #Our function to get a student's grade.
    def get_grade(self):
        #Our list of all possible grades.
        grades=['K','1','2','3','4','5']
        #We keep asking the user for their grade if it isn't K-5.
        self.grade=""
        while(self.grade not in grades):
            grade=input("What grade is the student in? [K,1-5] ")
            self.grade=grade
    #Our function to print a student's info.
    def print_student(self):
        print()
        print(f"Name:   {self.name}")
        print(f"School: {self.schoolName}")
        print(f"Grade:  {self.grade}")
#Driver code:
student_info=Student()
#Storing and checking a student's grade.
student_info.get_grade()
#Printing the student's info.
student_info.print_student()
        
