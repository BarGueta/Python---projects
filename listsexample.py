# Creating a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# append()
my_list.append(3)

# extend()
my_list.extend([8, 7])

# insert()
my_list.insert(2, 10)

# remove()
my_list.remove(1)

# pop()
popped_element = my_list.pop()

popped_element_at_index = my_list.pop(3)

# clear() - creating a new list to demonstrate
my_list_to_clear = [1, 2, 3]
my_list_to_clear.clear()

# index()
index_of_nine = my_list.index(9)

# count()
count_of_threes = my_list.count(3)

# sort()
my_list.sort()

# reverse()
my_list.reverse()

# copy()
my_list_copy = my_list.copy()

# list comprehension
squares = [x**2 for x in range(10)]




print("...")