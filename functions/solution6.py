# function with **kwargs
# function that accepts any no. of keyword arguments and prints them in the format key:value.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        

print_kwargs(power="lazer",name="shaktiman")
print_kwargs(power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(power="lazer",name="shaktiman",enenmy="dr. jackal")