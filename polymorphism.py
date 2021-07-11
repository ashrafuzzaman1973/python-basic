#build in polymorphic function

print(len("Ashrafuzzaman"))
print(len([10,20,30]))


#user define polymorphic functtion

def add(x,y,z=0):
	return x+y+z

print(add(10,20))
print(add(10,20,30))