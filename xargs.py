"""
def student(*details):
    print(details)

student(101,"ashraf",3.56)
student(101,"shahin",3.00)
"""
def add(*numbers):
    sum=0
    for n in numbers:
        sum = sum+n
    print(sum)
add(10,20)
add(10,20,30)
