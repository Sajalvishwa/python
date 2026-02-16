#tuple is sequence of immutable objects
#syntax:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#tuple indexing
print(my_tuple[0]) #1
print(my_tuple[1]) #2
print(my_tuple[2]) #3
print(my_tuple[3]) #4
print(my_tuple[4]) #5

#tuple slicing
print(my_tuple[0:3]) #(1, 2, 3)
print(my_tuple[2:5]) #(3, 4, 5)
print(my_tuple[:3]) #(1, 2, 3)

#methods of tuple
print(my_tuple.count(2)) #1 - counts the number of times a specified value appears in the tuple
print(my_tuple.index(3)) #2 - returns the index of the first occurrence of a specified value in the tuple

