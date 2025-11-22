# list uniquenees  checker 

#method-1 mera tareka 
items=["apple","banana","orange","mango","mango"]
# for item in items:
#     count=0
#     for checker in items:
#         if item==checker:
#             count+=1
#     if count>1:
#         print(item)
#         break

# sikha hua tareka method-2
unique_item=set()
for item in items :
    if item in unique_item:
        print("duplicate",item)
        break
    unique_item.add(item)
    # iss tareka sa ek hi vaar loop chala 

    