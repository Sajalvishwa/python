#list is a collection of items that are ordered and changeable. Lists are written with square brackets.
#list is mutable
#list is indexed

#syntax:
my_list = [1, 2, 3, 4, 5]
print(my_list)

#list indexing
print(my_list[0]) #1
print(my_list[1]) #2
print(my_list[2]) #3
print(my_list[3]) #4
print(my_list[4]) #5

#list slicing
print(my_list[0:3]) #[1, 2, 3]
print(my_list[2:5]) #[3, 4, 5]
print(my_list[:3]) #[1, 2, 3]
print(my_list[3:]) #[4, 5]
print(my_list[-2:]) #[4, 5]

#methods of list
my_list.append(6) #adds an item to the end of the list
print(my_list) #[1, 2, 3, 4, 5, 6]

my_list.insert(0, 0) #inserts an item at a specified position
print(my_list) #[0, 1, 2, 3, 4, 5, 6]

my_list.remove(3) #removes the first item with the specified value
print(my_list) #[0, 1, 2, 4, 5, 6]

my_list.pop() #removes the last item of the list
print(my_list) #[0, 1, 2, 4, 5]

my_list.sort() #sorts the list in ascending order
print(my_list) #[0, 1, 2, 4, 5]

my_list.reverse() #reverses the order of the list
print(my_list) #[5, 4, 2, 1, 0]

my_list.clear() #removes all the items from the list
print(my_list) #[]

#loops with list
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item) #prints each item in the list


