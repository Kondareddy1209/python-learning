# Define a list of numbers (with some duplicates)
Arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 2, 3, 22, 55]

# Step 1: Remove duplicates by checking if item is already in the new list
new = []
for i in Arr:
    if i not in new:
        new.append(i)

# Step 2: Print unique values
print("Unique elements:", new)

# Step 3: Print the sorted version of unique values
print("Sorted unique elements:", sorted(new))

# Step 4: Initialize variables to track largest and second largest
large = small = float("-inf")

# Step 5: Loop through the list to find the largest and second largest values
for i in new:
    if i > large:
        small = large
        large = i
    elif i > small and i != large:
        small = i

# Step 6: Print the largest and second largest results
print("Largest:", large)
if small == float("-inf"):
    print("No second element")
else:
    print("Second Largest:", small)
