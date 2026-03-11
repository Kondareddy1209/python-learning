n="mom"
original=n
rever = ""
for i in n:
    rever=i+rever
print(rever)
if original==rever:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")