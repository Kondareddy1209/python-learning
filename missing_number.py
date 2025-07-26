# Initialize the list with some numbers (some numbers might be missing in the sequence)
new = [1, 2, 4, 6]

# Loop through numbers starting from 1 up to the maximum number in the list (inclusive)
for i in range(1, max(new) + 1):
    
    # Check if the current number 'i' is NOT in the list
    if i not in new:
        
        # If it's missing, print it
        print("Missing number is", i)
