#                                                   SETS IN PYTHON


#Sets in Python are also one of the data types, just like lists and tuples. If we want to represent a group of unique elements, then we can go for sets. Sets cannot store duplicate elements. 

# POINTS TO BE REMEMBERED ABOUT SET DATA STRUCTURE IN PYTHON.

# 1. Insertion order is not preserved.
# 2. Indexing and slicing are not allowed for the set.
# 3. Sets can store the same and different types of     elements or objects.
# 4. Set objects are mutable, which means once we create a set object, we can make perform any changes to it. You cannot change the existing objects, but you can add more objects.
# 5. It cannot store duplicate keys. 

s = {1, 2, 3, 4, 5, 6, 7}
print(type(s))

s = {} #you cannot make an empty set because Python will read it as an empty dictionary. 
print(type(s))

s = set() #This is the only way to create an empty set in Python. We have list(), tuple(), and dict().

l = [1, 2, 3, 4, 5, 6, 7]
s = set(l)
print(s)
print(type(s))

l1 = [1,2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8]
s1 = set(l1)
print(s) # Deduplication is not allowed in sets. 

l2 = [1, 2, 3, "Amit", 12.34, True, False]
s2 = set(l2)
print(s2) # Can store multiple data types at once.
          # But it cannot store boolean values, because it cannot considered as keys. 

s = set(range(0,10))
print(s)

l3 = [1, 2, 3, 4, 5.29, "Kushagra", "Om"]
s3 = set(l3)

#                               Functions of sets 