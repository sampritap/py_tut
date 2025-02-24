# set is a built in data type in python used to store collection of unique items.
# they are unordered 
# do not allow to duplicate items


# create a set 
list1= [1,2,3,4,5,2,3,4,6]
set1=set(list1) # 1,2,3,4,5,6 prints the unique elements


#basic set operations

#add
set1.add(7)
print(set1)

#remove
set1.remove(3)
print(set1)

#trying to remove an item which is not present in the set and should not throw an error
#discard
set1.discard(9)
print(set1)

#pop
set2 = set1.pop()
print(set1) #this will remove first element from the set and return the rest item i.1 1 is removed

#clear
#set1.clear()
#print(set1) 


#set membership test
print(7 in set1) #returns true or false
print(1 in set1)

#mathematical operation

# 1.union
set2 ={1,2,3}
union_set = set1.union(set2)
print(union_set)

 #2. intersect
intersect_set= set1.intersection(set2)
print(intersect_set)

#difference
print(set1.difference(set2))

#symmetric difference 
#only similar items will be removed
print(set1.symmetric_difference(set2))


#sets method
print(set1.issubset(set2))
print(set1.issuperset(set2))


#counting unique words in text
text = "hi this is samprita,and this is python tut"
words= text.split()

print(words)
#convert this list to set for unique words
unique= set(words)
print(unique)


name = "samprita"
uni = set(name)
print(uni)