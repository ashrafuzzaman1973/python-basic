
class Student:

	def __init__(self,m1,m2):
		self.m1 = m1
		self.m2 = m2

	def show(self):
		print("show in A")


	#method overloading
	def sum(self,a=None,b=None,c=None):
		s=0
		if a!=None and b!=None and c!=None:
			s=a+b+c
		elif a!=None and b!=None:
			s= a+b
		else:
			s=a
		return s

class B(Student):
  	def show(self):
  		print("show in B")



s1= Student(11,12)
a1 = B(1,2);
print(a1.show())

#print(s1.sum(2))
