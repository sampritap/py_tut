list=['b','a',1,1.2,]
print(list)


# list comprehension
lst = [x**2 for x in range(10)]
print(lst)


# list comprehension with if condition
a=[num for num in range(10) if num%2==0]
print(a)

#nested list comprehension
pair =[(i,j) for i in lst for j in a]
print(pair)