try:
    num = [20,0,30]
    result = num[0]/num[3]
    print(result)
    print("Done")
except ZeroDivisionError :
    print("Division by zero is not possible")

finally:
    print("Successful")
"""
except IndexError :
    print("Index Error")
"""
