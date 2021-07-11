from functools import reduce

def all_add(a,b):
	return a+b

num = [1,2,3,4]
result = list(filter(lambda x:x%2==0,num))
print(result)

sum = reduce(all_add,result)

print(sum)