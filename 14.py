# int as and int return
def add(a):
    return a+a
e = add(1)
print(e)

# float as parameter and float as return type
def addB(b):
    return b + b
e2 =addB(12.3)
print(e2)

# string as parameter and string as return type
def greet(word):
    return "hello" + word
e3 = greet("good morning")
print(e3)

# boolean as parameter and boolean as return type
def canDrive (age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True
    else:
        return False
e4=canDrive(18,True)
print(e4)

# list as parameter and list as return type
cities = ["nashik","sangamner","pune"]
def addElementTolist(lst):
    lst.append("mumbai")
    return lst
e5= addElementTolist(cities)
print(e5)

# dict as parameter and dict as return type
info ={"fn" : "vaibhav","ln" : "katwe"}
def addcity(dic):
    dic.update({"city":"nashik"})
    return dic
e6 = addcity(info)
print(e6)

# tuple as parameter and tuple as return tupe
tupleA = (11,22,33)

def addValueTuple(tupA):
    # (11,22,33)
    tupA = list(tupA)  #[11,22,33]
    print(tupA)
    tupA.append(44) #[11,22,33,44]
    f = tuple(tupA) # (11,22,33,44)
    return f
e7 = addValueTuple(tupleA)
print(e7)

# set as parameter and set as return type 
setA ={11,22,33}
def addelementtoset(setB):
    setB.add(44)
    return setB
e7 = addelementtoset(setA)
print(e7)

# default parameter 
def add(x=1,y=1):
    print(x+y)
add(12,3)
add()

# postional parameter 
def sub(x,y):
    print(x-y)
sub(500,50) #-450
sub(y=400,x= 300)

# args 
def addall(*args):
    print(args)
    print(sum(args))
    total = 0
    for x in args:
        total = total + x
    print(total)
addall(1,2,3,3,4,5,6,7,8,3,5,6,7,8,4,5)

# **kwargs
def showInfo(**kwargs):
    print(kwargs)
showInfo(name="chinmay",lastName="deshpande",age=23)

# lambda function

def add(a,b):
    print(a+b)
add(12,2)

add = lambda x,y:x+y
add(12,3)

x = 10
print(x)
q  = lambda x:x*x
print(q)
q(2)

# function as parameter 
add = lambda x,y:x+y
def addition(fn,x,y):
   fn = lambda x,y:x+y
   x = 10
   y = 10
   sum =  fn(x,y)
   return sum
s = addition(add,10,7)
print(s)

# function as return type
def subtraction():
    return lambda x:x-x
sub = subtraction()
print(sub)
e = sub(1)
print(e)
