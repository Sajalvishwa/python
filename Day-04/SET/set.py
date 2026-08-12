#set is an unordered collection of unique elements
#sets are mutable
#sets are not indexed
#syntax:
my_set = {1, 2, 3, 4, 5}
print(my_set)

#methods of set
my_set.add(6) #adds an element to the set
print(my_set) #{1, 2, 3, 4, 5, 6}

my_set.remove(3) #removes the specified element from the set
print(my_set) #{1, 2, 4, 5, 6}

my_set.pop() #removes and returns an arbitrary element from the set
print(my_set) #{2, 4, 5, 6} - the output may vary as sets are unordered

my_set.clear() #removes all the elements from the set
print(my_set) #set() - an empty set

my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
union_set = my_set1.union(my_set2) #returns a new set that is the union of the two sets
print(union_set) #{1, 2, 3, 4, 5

intersection_set = my_set1.intersection(my_set2) #returns a new set that is the intersection of the two sets
print(intersection_set) #{3}

difference_set = my_set1.difference(my_set2) #returns a new set that is the difference of the two sets
print(difference_set) #{1, 2}

symmetric_difference_set = my_set1.symmetric_difference(my_set2) #returns a new set that is the symmetric difference of the two sets
print(symmetric_difference_set) #{1, 2, 4, 5}


#loops with set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item) #prints each item in the set - the order may vary as sets are unordered
