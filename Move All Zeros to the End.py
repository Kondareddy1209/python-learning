new = [0, 1, 0, 2, 4, 0, 0, 6]

new1 = []  # To store zeros
new2 = []  # To store non-zero elements

# Loop through the original list
for i in new:
    if i == 0:
        new1.append(i)   # Add zero to new1
    else:
        new2.append(i)   # Add non-zero to new2

# Combine non-zeros followed by zeros
combine = new2 + new1

# Print the final list
print(combine)
