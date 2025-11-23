username = "chaiaurcode"

def func():
    username="chai" # agar ya nhi specify hota to vo bhar defined value ko lekar hi bta deta chae iss line ko cmnt kar run kar le 
    print("funcrion ka andar : ",username)
    
print(username)
func()

x=99

# def func2(y):
#     z=x+y
#     return z

# result=func2(1)
# print(result)

# def func3():
#     x=88
    
# print(x)

# def func4():
#     global x #but always avoid these things global keyword ko avoid hi karna hai for beeterment of project removes conflict
#     x=12

# func4()
# print(x)

def f1():
    x=88
    def f2():
        print(x)
    return f2()
myResult = f1()

def chaicoder(num ):
    def actual(x):
        return x**num
    return actual

f = chaicoder(2)
g= chaicoder(3)

print(f(3))
print(g(2))