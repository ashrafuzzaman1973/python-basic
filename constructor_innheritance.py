
class A:

	def __init__(self):
		print("in A init")

	def feature1(self):
		print("feature1 is here")

	def feature2(self):
		print("feature2 is here")

class B:

	def __init__(self):
		#super().__init__()
		print("in B init")

	def feature3(self):
		print("feature3 is here")

	def feature4(self):
		print("feature4 is here")


class C(A,B):

	def __init__(self):
		print("in c init")

	def feature5(self):
		print("feature5 is here")

	def feature6(self):
		print("feature6 is here")


s1 = C()

