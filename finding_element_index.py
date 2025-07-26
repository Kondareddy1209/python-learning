new=[1,2,3,4,25,6,3,2,1,2,3,4,5,6]
target=30
for i in range(len(new)):
    if new[i]==target:
        print("target found at indext "+str(i))
        break
else:
    print("not found")
