class Student:
    roll = ""
    cgp = ""

    def setValue(self,roll,gpa):
        self.roll=roll
        self.cgp=gpa


    def display(self):
        print(f"Roll is :{self.roll},Gpa is : {self.cgp}")


rahim = Student()
rahim.setValue(101,3.45)
rahim.display()


karim = Student()
karim.setValue(102,3.60)
karim.display()
