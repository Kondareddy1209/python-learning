# list_operations_demo.py
# This script demonstrates basic list operations in Python such as append, insert, remove, reverse, extend, sort, and pop.

# Initial list
List = [10, 20, 30, 40, 50]
print(List)  # Output the original list

# Append 60 to the end of the list
List.append(60)
print(List)  # List becomes: [10, 20, 30, 40, 50, 60]

# Print the length of the list
print(len(List))  # Output: 6

# Insert 15 at index 2
List.insert(2, 15)
print(List)  # List becomes: [10, 20, 15, 30, 40, 50, 60]

# Remove the first occurrence of 15
List.remove(15)
print(List)  # List becomes: [10, 20, 30, 40, 50, 60]

# Create a reversed copy of the list using slicing
list_reverse = List[::-1]
print(list_reverse)  # Output: [60, 50, 40, 30, 20, 10]

# Find the index of the first occurrence of 40
print(List.index(40))  # Output: 3

# Create a new list and extend the original list with it
new_List = [20, 30, 70, 60]
List.extend(new_List)
print(sorted(List))  # Print a sorted version of the list (does not modify original)

# Remove the first occurrence of 20
List.remove(20)
print(List)  # 20 is removed from the first match only

# Remove the last element from the list using pop
List.pop()
print(List)  # Last element (60) is removed
