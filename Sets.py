# -****************************** Python Sets
print("-********************** Python Sets")
# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# -****************************** Access Items
print("-********************** Access Items")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# -****************************** Add Set Items
print("-********************** Add Set Items")
# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# -****************************** Remove Set Items
print("-********************** Remove Set Items")
# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) #remove random item

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset

# -****************************** Loop Sets
print("-********************** Loop Sets")

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# -****************************** Join Sets
print("-********************** Join Sets")
# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

# -****************************** Set Methods
print("-********************** Set Methods")

# add()
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)

# clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# copy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

# difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)