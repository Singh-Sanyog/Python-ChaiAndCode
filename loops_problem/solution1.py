# multipication taBLE printer skipping the 5th term
no=int(input("enter a no: "))
for i in range(1,11):
    if i==5:
        continue
    print(f"{no} * {i} = {no*i}")


    