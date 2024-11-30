my_list = [] 

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert value at second position
my_list.insert(1, 15) 

# Extend list
my_list.extend([50, 60, 70])

# Remove last element
my_list.pop()

# Sort list in ascending order
my_list.sort()

# Find index of 30
index_of_30 = my_list.index(30)

# Print the sorted list and index
print(my_list)
print(f"Index of 30: {index_of_30}")