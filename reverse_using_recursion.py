def recur(n,rev=0):
    if n==0:
        return rev
    else:
        num=n%10
        rev=rev*10+num
        n=n//10
        return recur(n,rev)
n=int(input("Enter a number:"))
print("The reverse of the number is:",recur(n))