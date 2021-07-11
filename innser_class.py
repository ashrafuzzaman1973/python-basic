
class Student:

	def __init__(self,name,rollNo):
		self.name = name
		self.rollNo = rollNo
		self.lap = self.Laptop()

	def show(self):
		print(self.name,self.rollNo)
		self.lap.show()

	class Laptop:

		def __init__(self):
			self.brand = "Hp"
			self.cpu = "i5"
			self.ram = 8

		def show(self):
			print(self.brand,self.cpu,self.ram)




s1 = Student("Ashraf",1)
s2 = Student("juwel",2)


s1.show()

l1 = s1.lap
l2 = s2.lap

