n=int(input("Enter a number: "))
ori=n
rever=0
while n>0:
    num=n%10
    rever=rever*10+num
    n=n//10
if ori==rever:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")