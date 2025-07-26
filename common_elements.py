#code 1
# Define two lists
new = [1, 2, 3, 4]
new1 = [5, 6, 7, 4]

# Loop through each element of the first list
for i in range(len(new)):
    # Loop through each element of the second list
    for j in range(len(new1)):
        # Check if elements at current indices match
        if new[i] == new1[j]:
            # Print common element
            print("Common element is:", new[i])


#Code2 Approach:
# Define two lists
new = [1, 2, 3, 4]
new1 = [5, 6, 7, 4]

# Convert lists to sets and find common elements
common = list(set(new) & set(new1))  # '&' finds intersection

# Check if common elements exist and print result
if common:
    print("Common elements are:", common)
else:
    print("No common elements")
