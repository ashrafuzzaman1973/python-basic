class Student:
    roll = ""
    cgp = ""

rahim = Student()
#print(isinstance(rahim,Student))
rahim.roll=101
rahim.cgp = 3.50
print(f"Roll is :{rahim.roll},Gpa is : {rahim.cgp}")


karim = Student()
karim.roll=102
karim.cgp = 3.60
print(f"Roll is :{karim.roll},Gpa is : {karim.cgp}")