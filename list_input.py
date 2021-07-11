n= input("Enter text number : ")
"""
list = n.split()
sum=0
for num in list:
	sum = sum+ int(num)
print(sum)
"""
numOfLetter = 0
numOfWords = 0
numOfDigits = 0

for x in n:
	x = x.lower()
	if x>='a' and x<='z':
		numOfLetter = numOfLetter+1
	elif x >='0' and x<='9':
		numOfDigits = numOfDigits+1
	elif x == ' ':
		numOfWords = numOfWords+1
print("Total Letter number :",numOfLetter)
print("Total digits number : ",numOfDigits)
print("Total words number :",numOfWords+1)
