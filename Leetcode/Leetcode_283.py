k=int(input("Enter length of Array: "))
nums=[]
for i in range(k):
    num=int(input("Enter the Elements in Array: "))
    nums.append(num)
n=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[i],nums[n]=nums[n],nums[i]
        n+=1
print(nums)