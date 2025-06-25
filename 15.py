birthyear =[2000,2001,2002,2000]
ages =[]
for x in birthyear:
    age = 2025 - x
    ages.append(age)
print(ages)

ages2 = [2025-x for x in birthyear]
print(ages2)

ages = lambda x : 2025-x 
ages2 = list(map(ages,birthyear))
print(ages2)

# program 2
numbers = [1,2,3,4,5,6,7,8,9,10]
squrt = lambda x : x*x
squares = list(map(squrt,numbers))
print(squares)

# program 3
marks = [90,91,34,34,47,88,99,65,89]
above60 = []
for x in marks:
    if x > 60:
        above60.append(x)
print(above60)

above60 = [x for x in marks if x> 60]
print(above60)

above60 = lambda x : x > 60 
above601 = list(filter(above60,marks))
print(above601)

tran =[15,-45,96,-34,57,-54]
withd = lambda x: x < 0
dep = lambda x : x > 0
wr = list(filter(withd,tran))
print(wr)
dp = list(filter(dep,tran))
print(dp)

dp = [ x for x in tran if x > 0]
wr = [ x for x in tran if x < 0]

print(dp)
print(wr)

# program 4

numbers  = [11,22,33]
total = 0
for x in numbers:
    total = total + x
    print(total)

from functools import reduce
total3 = reduce(lambda x,y : x+y ,numbers,5)
print(total3)