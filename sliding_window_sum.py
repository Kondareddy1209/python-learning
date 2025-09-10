# sliding_window_sum.py

# Input list
n = [5, 9, 1, 8, 7]

# Variable to store the running sum
temp = 0

# Left pointer of the sliding window
l = 0

# Loop through each index of the list
for i in range(0, len(n)):
    # Add current element to the running sum
    temp += n[i]
    
    # If window size exceeds 3, remove the leftmost element
    if (i - l == 3):
        temp -= n[l]   # subtract element going out of the window
        l += 1         # move left pointer forward
        print(l, i)    # debug: show current left and right pointers
    
    # If window size becomes exactly 3, print the sum
    if (i - l + 1 == 3):
        print(temp)
