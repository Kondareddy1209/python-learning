# def factorail(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorail(n-1)
# n=int(input("Enter a number : "))
# print("factorail of n is :", factorail(n))


n=int(input("Enter a number : "))
fact=1
if n<0:
    print("Factorial does not exist for negative numbers")
elif n==0 or n==1:
    print("Factorial of",n,"is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of",n,"is",fact)