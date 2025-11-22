# pet food recommendation 

pet_species=input("enter your pet species: ").lower().strip()
pet_age=int(input("enter your pet age: "))
if pet_species=="dog": 
    if pet_age>=2:
        print("puppy food")
if pet_species=="cat":
    if pet_age>=5:
        print("senior cat food")
else:
    print("no suggestion ")