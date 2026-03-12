def fibn(n):
    if n<=1:
        return n
    else:
        return fibn(n-1)+fibn(n-2)
n=int(input("Enter a number:"))
for i in range(n):
    print(fibn(i))