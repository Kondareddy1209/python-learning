# max_sliding_window_sum.py

# Input list
n = [5, 9, 1, 8, 7]

# Running sum of current window
temp = 0

# Left pointer of sliding window
l = 0

# Variable to store the maximum sum of any window
ans = 0

# Iterate through the list
for i in range(0, len(n)):
    # Add the current element to running sum
    temp += n[i]
    # If window size exceeds 3, remove the leftmost element
    if (i - l == 3):
        temp -= n[l]   # remove element going out of window
        l += 1         # move left pointer
        print(l, i)    # debug: shows window boundaries
    
    # If window size is exactly 3, check window sum
    if (i - l + 1 == 3):
        print(temp)        # print the current window sum
        ans = max(ans,temp)  # update maximum window sum

# Print the maximum sum found
print(ans)
