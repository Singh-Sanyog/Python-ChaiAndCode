# ticket prices on the basis of age and day


age=int(input("enter your age: "))
day=input("enter day: ").lower()
price=12 if age>=18 else 8
if day=="wednesday":
    print(f"${price-2}")
else:
    print("$",price)