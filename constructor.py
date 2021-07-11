class Student:
    roll = ""
    cgp = ""

    def __init__(self,roll,gpa):
        self.roll=roll
        self.cgp=gpa


    def display(self):
        print(f"Roll is :{self.roll},Gpa is : {self.cgp}")


rahim = Student(101,3.45)
rahim.display()


karim = Student(102,3.60)
karim.display()
