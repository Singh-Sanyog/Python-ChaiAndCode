# find the first non repeated character

string=input("enter a string: ").strip().lower()
# dict={}
# a=0
# for checking_char in string:
#      dict.update(checking_char=a)
#      print(dict)
#      for checker in string:
#          if checking_char == checker:
#              a+=1
#              dict.update(checking_char=a)
    
#      if dict[checking_char]==1:
#           print(checking_char)
#      break

for checking_char in string:
   if string.count(checking_char)==1:
       print(checking_char)
       break

