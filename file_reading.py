file = open("student.txt","r")
#print(file.readable())
text = file.read()
print(text)
file.close()