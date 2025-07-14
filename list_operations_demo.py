# list_operations_demo.py
# A demonstration of Python list methods including append, insert, remove, slicing, extend, sort, pop, membership check, and clear.

# Create an initial list
List = [10, 20, 30, 40, 50]
print(List)  # Output: [10, 20, 30, 40, 50]

# Append 60 to the list
List.append(60)
print(List)  # Output: [10, 20, 30, 40, 50, 60]

# Print the length of the list
print(len(List))  # Output: 6

# Insert 15 at index 2
List.insert(2, 15)
print(List)  # Output: [10, 20, 15, 30, 40, 50, 60]

# Remove the value 15
List.remove(15)
print(List)  # Output: [10, 20, 30, 40, 50, 60]

# Create a reversed version of the list
list_reverse = List[::-1]
print(list_reverse)  # Output: [60, 50, 40, 30, 20, 10]

# Find the index of value 40
print(List.index(40))  # Output: 3

# Extend the list with another list
new_List = [20, 30, 70, 60]
List.extend(new_List)
print(sorted(List))  # Output: [10, 20, 20, 30, 30, 40, 50, 60, 60, 70]

# Remove the first occurrence of 20
List.remove(20)
print(List)  # Output: [10, 30, 40, 50, 60, 20, 30, 70, 60]

# Remove the last item using pop()
List.pop()
print(List)  # Output: [10, 30, 40, 50, 60, 20, 30, 70]

# Check if 20 is still in the list
if 20 in List:
    print("Yes")  # Output: Yes

# Clear all elements from the list
List.clear()
print(List)  # Output: []
