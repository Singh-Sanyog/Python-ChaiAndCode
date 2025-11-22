# reversing a string

string=input("enter a string : ").strip()
reverse_string=""
l=len(string)
for char in string[l::-1]:
    reverse_string+=char
    
print(reverse_string)
    