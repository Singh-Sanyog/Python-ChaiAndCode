# password strength cheker 

password=input("enter your password: ").lower().strip()
check=len(password)
if check<6:
    print("weak password")
elif check<11:
    print("moderate password")
else:
    print("strong password")