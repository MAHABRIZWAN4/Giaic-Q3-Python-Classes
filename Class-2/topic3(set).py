# The Set Data Type
# Set is one of 4 built-in data types in Python used to 
# store collections of data, the other 3 are List, 
# Tuple, and Dictionary, all with different qualities and usage.

# A set is:

# 1. unordered
# 2. unchangeable
# 3. unindexed
# An object cannot appear more than once in a set, whereas in List and 
# Tuple, same object can appear more than once.
 


my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])

print(my_set)
print(my_set2)
print(type(my_set))
print(type(my_set2))
print(len(my_set))
print(my_set == my_set2)




# 1. Unordered (Tarteeb Fix Nahi Hoti)

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output ka order alag ho sakta hai




# 2. Unchangeable (Set ki Values Directly Change Nahi Hoti)
# Ek baar set ban gaya, to uski values directly modify nahi kar sakte.
#  Aap naye elements add ya remove kar sakte ho, magar ek existing value ko update nahi kar sakte.


my_set = {10, 20, 30}
my_set.add(40)
print(my_set)
# my_set[1] = 50  # Error dega




# 3. Unindexed (Set me Indexing Nahi Hoti)
# set indexing support nahi karta, yani aap set[0], set[1] aise access nahi kar sakte.


my_set = {"apple", "banana", "cherry"}
# print(my_set[0])  # Error dega






# fronzenset
iftarItem_set = { "Rooh Afza","Rooh Afza", "Banana","Jalebi","Samosa","Samosa" }
iftarItem_frozenset = frozenset(iftarItem_set)


