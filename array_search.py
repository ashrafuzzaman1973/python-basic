from array import *

arr = array('i',[])

n = int(input("Enter the array length number:"))

for i in range(n):
	x= int(input("please enter number:"))
	arr.append(x)

print(arr)

val = int(input("Enter the value for search:"))

k=0

for e in arr:
	if e==val:
		print(k)
		break
	k +=1
print(arr.index(val))