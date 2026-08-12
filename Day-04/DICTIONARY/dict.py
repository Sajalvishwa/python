#dictionary is a collection of key-value pairs
#dictionary is mutable
#dictionary is indexed by keys
#syntax:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

#accessing values in a dictionary
print(my_dict["name"]) #Alice
print(my_dict["age"]) #30
print(my_dict["city"]) #New York

#methods of dictionary
my_dict["country"] = "USA" #adds a new key-value pair to the dictionary
print(my_dict) #{"name": "Alice", "age": 30, "city": "New York", "country": "USA"}

my_dict.pop("age") #removes the key-value pair with the specified key
print(my_dict) #{"name": "Alice", "city": "New York", "country": "USA"}

my_dict.clear() #removes all the key-value pairs from the dictionary
print(my_dict) #{}

#loops with dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key in my_dict:
    print(key) #prints each key in the dictionary

for value in my_dict.values():
    print(value) #prints each value in the dictionary

for key, value in my_dict.items():
    print(f"{key}: {value}") #prints each key-value pair in the dictionary


