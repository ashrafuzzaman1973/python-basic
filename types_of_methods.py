
class Student:

	#Class Variable
	school = "Dhanmondi"

	def __init__(self,m1,m2,m3):
		#Instance variale
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	#instance method and accessor method
	def avg(self):
		return (self.m1+self.m2+self.m3)/3

	#class Method
	@classmethod
	def getSchool(cls):
		return cls.school

	#static mehtod
	@staticmethod
	def info():
		print("This is student class .. in abc module")



s1 = Student(23,22,30)
s2 = Student(35,40,60)


print(s1.avg())
print(Student.getSchool())

Student.info()