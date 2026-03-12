def pali(n):
    n=str(n)
    if len(n)<=1:
        return True
    if n[0]!=n[-1]:
        return False
    else:
        return pali(n[1:-1])
n=input("Enter a number:")
print(pali(n))