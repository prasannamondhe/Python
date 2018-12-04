#List and its operations


#Append to the list

list1 = [1,2,3,4,5,6]
list1.append(7)             #Appending single element to list
list1.append(8)             #Appending single element to list  
print("Single element append", list1)

list2 = [9,10,11]           
list1.append(list2)         #Appending one list to other list
print("List2 appended to list1", list1)

tup = (1,2,3,4)
list1.append(tup)           #Appending tuple to list
print("Tuple is appended to list", list1)

diction = {"a":1,"b":2,"c":3}
list1.append(diction)       #Appending dictionary to list
print("Dictionary appended to", list1)


#Extend the list

list3 = [7,8,9]
list1.extend(list3)                         #Extend list by list
print("Extended list with list ", list1)

tup1 = (99,100,111)
list1.extend(tup1)                          #Extend list with tuple
print("Extended list with tuple", list1)

diction2 = {"p":1,"q":2,"r":3}
list1.extend(diction2)                      #Extend list with dictionary
print("Extend list with dictionary", list1)


#insert 

list1 = [11,22,33,44]
list1.insert(2,'22..22')
list1.insert(len(list1),55)
print(list1)

#Remove 

list1 = [22,33,44,55]
print("Before removing 22", list1)
list1.remove(33)
list1.remove(22)
list1.remove(44)
print("After removing 22", list1)

#Pop

list1 = [22,33,44,55]
print("Poped ele is ",list1.pop(1))
print("Poped ele is ", list1.pop(0))

#Clear
list1 = [22,34,5,5]
list1.clear()
print("Cleared list1", list1)

#Count
list1 = [1,2,2,3,4,5,4,4]
print("Count of 2 is", list1.count(2))
print("Count of 4 is ", list1.count(4))


#Reverse 
list4 = [4,3,2,1]
print("Reversed list is", list1.reverse())


#Slicing

list5 = [1,2,3,4,5,6]
print("list is ",list5[::])
print("list with slice ", list5[2:5:3])

######################################################################################################################

#Tuple (Tuple packing)

tup = (11,22,33,44,55)
print("tuple element 1:", tup[0])
print("tuple element 2:", tup[1])
print("tuple element 1:", tup[2])

#Tuple unpacking

x,y,z,q,w = tup
print("x is ",x)
print("y is ",y)
print("z is ",z)
print("q is ",q)
print("w is ",w)

######################################################################################################################

#Dictionaries

dict = {'name':"David","job":"IT","weight":76,"married":True}
print("Married?",dict["married"])
print("name is ", dict["name"])
print("weight is ", dict["weight"])

print("\nKeys are :::")
for v in dict.keys():
    print(v)

print("\nValues are:::")
for k in dict.values():
    print(k)

print("\nItems is dictionary::")
for i in dict.items():
    print(i)

print("check key exists", "name" not in dict.values())   
