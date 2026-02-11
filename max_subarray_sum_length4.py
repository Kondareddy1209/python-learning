# max_subarray_sum_length4.py
# ------------------------------------
# Program to generate all subarrays of a list
# and find the maximum sum among subarrays of length 4.
#
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)
# ------------------------------------

# Input array
n = [5, 9, 1, 8, 7]

# Variables for maximum sum (m) and temporary sum (s)
m = 0
s = 0

# To store all possible subarrays
ans = []

# Generate all subarrays
for i in range(len(n)):                # Start index 
    for j in range(i, len(n)):         # End index
        temp = []
        for k in range(i, j + 1):      # Collect elements from i to j
            temp.append(n[k])
        ans.append(temp)               # Add subarray to ans list

# Print all subarrays
print("All subarrays:")
print(ans)

# Check subarrays of length 4 and calculate their sums
print("\nSubarrays of length 4 and their sums:")
for i in range(len(ans)):
    if len(ans[i]) == 4:               # Only consider subarrays of length 4
        s = sum(ans[i])                # Calculate sum
        m = max(m, s)                  # Update maximum sum
        print(ans[i], "Max so far:", m, "Sum:", s)

# Final maximum sum among subarrays of length 4
print("\nMaximum sum among subarrays of length 4:", m)
