n=153
sum=0
temp=n
while n>0:
    num=n%10
    sum+=num**3
    n=n//10
if sum==temp:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")