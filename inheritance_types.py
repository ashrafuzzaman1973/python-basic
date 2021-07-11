class A:
	def display1(self):
		print("I am A class")

class B(A):
	#display1
	def display2(self):
		print("I am B class")

class C(B):
	#display1
	#display2
	def display3(self):
		print("I am C class")


obj = C()
obj.display1()
obj.display2()
obj.display3()


		