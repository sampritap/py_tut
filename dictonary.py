#dictionories are unordered collections of items. 
#they store in key-value pair 
#keys must be unique
#immutable 

#creating dictinories 
dict= {}
print(type(dict))


student={ 'name':'sam',
         'age':22,
         'grade':556
}

#accesing 
print(student['grade'])

#get()
print(student.get('grade'))

#modifying

#dictionary are mutable add, delete,update the elements
student['age']=33 #updated
student['adress']='banglore' #added
del student['grade'] #deleted

print(student)


#dictionary methods

key= student.keys()  #get keys
values= student.values()  #get values
items = student.items() #get all the pairs of values and key

#shallow copy 
student_copy = student
student['name']='sam'
#the name will be updated to both student and student copy in this case 
print(student)
print(student_copy)

#to overcome such cases we use shallow copy so that the updation only happens to the copies item since it creates a seperate memory for that copy 

student_copy1= student.copy()
student['name']='sam2'
print(student)
print(student_copy1)

#iteration over dict
for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

for key,value in student.items():
    print(f'{key}:{value}')

#nested dictionories
    
stu={
    "stud1":{'name':'a','age':'77'},
   "stud2":{'name':'hy','age':'90'},
    "stud3":{'name':'b','age':'7'},
}

print(stu)
{'stud1': {'name': 'a', 'age': '77'}, 'stud2': {'name': 'hy', 'age': '90'}, 'stud3': {'name': 'b', 'age': '7'}}


#accesing dic
print(stu['stud1']['name'])
print(stu['stud2']['age'])

#iterating nested dic

for i,j in stu.items():
    print(f'{i}:{j}')
    for key,value in j.items():
        print(f'{key}:{value}')

#dict comprehension
squares={x:x**2 for x in range(10)}
print(squares)


#frequemcy of a number

number=[1,2,2,3,1,5,8]
frq={}

for num in number:
    if num in frq:
        frq[num]+=1
    else:
        frq[num]=1

print(frq)


#merging dictionories

dic1= {'a':1,'b':2}
dic2= {'b':3,'c':4}
merge= {**dic1, **dic2}
print(merge)
