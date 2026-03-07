n=int(input("Enter the length of array: "))
nums=[]
for i in range(n):
    num=int(input("Enter the Elements: "))
    nums.append(num)
i=float('inf')
j=float('inf')
for k in range(len(nums)):
    if nums[k]<=i:
        i=nums[k]
    elif nums[k]<=j:

        j=nums[k]
    else:
        print(True)
else:
    print(False)