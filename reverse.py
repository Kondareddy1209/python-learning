n=int(input("Enter a number: "))
rever=0
while n>0:
    num=n%10
    rever=rever*10+num
    n=n//10
print("The reverse of the number is: ",rever)