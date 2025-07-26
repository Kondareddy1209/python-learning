# Define a list with some duplicate values
Arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 2, 3]

# Create an empty list to store unique elements
new = []

# Loop through each element in the original list
for i in Arr:
    # Check if the element is not already in the new list
    if i not in new:
        # If it's unique, add it to the new list
        new.append(i)

# Print the list of unique elements
print(new)
