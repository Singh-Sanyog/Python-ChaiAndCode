# function with *args
# write a function that takes variable number of arguments and returns their sum 

def sum_all(*args):  # *-ya lagna bhut jaruri kuki yahi arguments dekhega  args likhoge to good practice hai ( arguments hi handle karte hai ya )
    print("args",args)
    print("i*2")
    for i in args:
        print(i*2)
    print("*args",*args)
    return sum(args) 

print("sum",sum_all(1,2))
print()
print("sum",sum_all(1,2,3))
print()
print("sum",sum_all(1,2,4,7,5,9))