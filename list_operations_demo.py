# list_operations_demo.py
# Demonstrates basic list operations in Python

# Create an initial list
List = [10, 20, 30, 40, 50]
print(List)  # [10, 20, 30, 40, 50]

# Append a value
List.append(60)
print(List)  # [10, 20, 30, 40, 50, 60]

# Print the length of the list
print(len(List))  # 6

# Insert 15 at index 2
List.insert(2, 15)
print(List)  # [10, 20, 15, 30, 40, 50, 60]

# Remove 15
List.remove(15)
print(List)  # [10, 20, 30, 40, 50, 60]

# Reverse the list using slicing
list_reverse = List[::-1]
print(list_reverse)  # [60, 50, 40, 30, 20, 10]

# Get index of value 40
print(List.index(40))  # 3

# Extend list with new values
new_List = [20, 30, 70, 60]
List.extend(new_List)
# List is now: [10, 20, 30, 40, 50, 60, 20, 30, 70, 60]

# Print sorted version of the list
print(sorted(List))  # [10, 20, 20, 30, 30, 40, 50, 60, 60, 70]

# Print third largest element (from sorted list)
print(sorted(List)[-3])  # 60

# Remove the first occurrence of 20
List.remove(20)
print(List)  # one 20 is removed

# Remove last element using pop
List.pop()
print(List)  # last value (60) removed

# Check if 20 is still in the list
if 20 in List:
    print("Yes")

# Print maximum value in the list
print(max(List))  # e.g., 70

# Calculate sum of all elements
Sum = 0
for i in range(len(List)):
    Sum += List[i]
print(Sum)

# Clear the list
List.clear()
print(List)  # []
