# prime no checker 

number=int(input("enter a no : "))
count=0
for i in range(2,number):
    if (number%i) == 0:
        count+=1
        break

if count==0:
    print("prime no. ")
else:
    print("not prime")


