# create 
# update
# retrive
# delete

a = 10 
print(a)
print(type(a))

b = 20
print(b)
print(type(b))

c = "Vaibhav"
print(c)
print(type(c))

d = True
print(d)
print(type(d))

names = ["vaibhav","mayuri","ram"]
print(names)
print(type(names))

info ={
    "firstName" : "vaibhav",
    "lastName" : " katwe",
}
print(info)
print(type(info))

g = 12,3
print(g)
print(type(g))

# set 
numbers = {11,22,33,44,55,66,11}
print(numbers)

#print(numbers[0])  # error

# range()
numbersB = {22,33,44,55,66}
for x in numbersB:
    print(x)

# program 1

setB = {"ram","sham","vaibhav","darshan","gaurav","aditya"}
print("ram" in setB)
print("Ram" in setB)

# program 2
print(len("vaibhav"))
print(len([11,22,33]))
print(len({"fn" : "vaibhav", "ln" : "katwe"}))
print(len((11,22,33,44)))
print(len({11,22,33,44,55}))

setc = {"ram","sham","vaibhav","darshan","gaurav","aditya"}
print(len(setc))

# program 3
# setH = {11,22,33}
# setH[0] = 00
# print(setH)

# program 4
# delete the set
# del setc
#  print(setc)

# program 5
setA = {11,22,33}
setA.add(44)
print(setA) 

setA.clear()
print(setA)

setA = {99,88,77} 
setB = setA
setA.clear()
print(setA)
print(setB)

setD= {44,55,66}
setC  = setA.copy()
setC.clear()
print(setC)
print(setD)