from threading import *
from time import sleep

class Hello(threading.Thread):
	def run(self):
		for i in range(100):
			print('Hello')
			sleep(1)

class Hi(threading.Thread):
	def run(self):
		for i in range(100):
			print('Hi')
			sleep(1)
	

t1 = Hello()
t2 = Hi()
		
t1.start()
t2.start()