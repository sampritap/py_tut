
#sum of natural numbers
sum=0
for i in range(11):
    sum = sum + i
print(sum)

#prime numbers
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

