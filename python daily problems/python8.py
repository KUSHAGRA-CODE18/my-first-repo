                                    #Lists in Python:


'''Example: Creating a list with elements

names = ["Mohan", "Prasaad", "Ramesh", "Mohan", 10, 20, True, None]
print(names)

-->Creating a list in Python by using the list() function

We use this function for creating lists from other data types like `range`, `tuple`, etc. This is generally referred to as "type conversion." 

            #Accessing lists in Python 
'''

L1 = []
print(L1)
print(type(L1))

#Converting anything like `range` in a list.
r = range(0, 10)
r = list(r)
print(r)
# print(r[20]) --> out of range (Index Error)



# Accessing a list by using loops in Python 

'''We can also access the element of a list by using `for` and `while` loops. 
Example: accessing  list using a for loop 

'''

a = [100, 200, 300, 400]
for x in a:
    print(x)

#Example: accessing a list by using awhilw loop 





# Important Functions or methods of `list` in Python 

#1. 
# len():

n = [1, 2, 3, 4, 5, 6]
print(len(n))

#2.
# count():

n = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6]
print(n.count(5))
print(n.count(3))

#3.
# append(): This function, adds any element at the end of the list.

l= [] #empty list
l.append("Ramesh")
l.append("Suresh")
l.append("Mahesh")
print(l)

#4. 
# insert(): This function can add the element in between any indexing of the list.

n = [10, 20, 30, 40, 50]
n.insert(0, 76)
print(n)

l = [10, 20, 30, 40]
l.insert(1, 111)
print(l)
l.insert(-1, 222)
print(l)
l.insert(10, 333)
print(l)
l.insert(-10, 444)
print(l)

#5.
# extend():

#6.
# remove(): used to remove the value from the list. If you don't pass any value, it will give a `ValueError`. 
# Give a value in `remove`. If we don't give any value, it will give a `ValueError`. 
# Remove the value.

n = [10, 20, 30, 40, 50]
n.remove(10)
print(n)

#7.
# pop(): `pop` function used to remove the from the list by indexing.
# If we don't give any indexing in it, it will remove the last element of the list. 
# if we give wrong indexing in the `pop` function. It will give an indexing error. 

n = [10, 20, 30, 40, 50]
n.pop()
print(n)

n = [10, 20, 30, 40, 50]
n.pop(3)
print(n)

#8.
# reverse():
# this method in Python is used to reverse the order of the list elements.

n = [10, 20, 30, 40, 50]
print(n)
n.reverse()
print(n)

#9. 
# sort():
