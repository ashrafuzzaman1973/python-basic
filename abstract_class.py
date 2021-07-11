from abc import ABC,abstractclassmethod


class Computer(ABC):

	@abstractclassmethod
	def proess(self):
		pass

class Laptop(Computer):

	def proess(self):
		print('its running')

#com = Computer()

com = Laptop()

com.proess()