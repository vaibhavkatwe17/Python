my_dict = {
    "name" : "vaibhav",
    "lastName" : "katwe",
    "age" : 22,
    "skills" :["pyhton" , "excel" , "power bi"]
}

print(type(my_dict))

# program 2

my_dict2 = {
    "name" : "vaibhav",
    "lastName" : "katwe",
    "age" : 22,
    "skills" :["pyhton" , "excel" , "power bi"]
}

# retrive
print(my_dict2["name"])
a = my_dict2.get("lastName")
print(a)


# program 3
# update

my_dict3 = {
    "name" : "vaibhav",
    "lastName" : "katwe",
    "age" : 22,
    "skills" :["pyhton" , "excel" , "power bi"],
    "age" : 25
}

my_dict3["name"] = "mayuri"
print(my_dict3)

# does not allow to store duplicate keys ?
my_dict3.update({"lastName" : "pati"})
print(my_dict3)

# Program 4
my_dict4 = {
    "name" : "vaibhav",
    "lastname" : "katwe",
    "age" : 25,
    "skill" : ["pyhton","Power bi", "excel"]
}

my_dict4["language"] = ["marathi"]
print(my_dict4)

my_dict4.update({"city": "nashik"})
print(my_dict4)

# program 5

my_dict5 = {
    "name" : "vaibhav",
    "lastname" : "katwe",
    "age" : 25,
    "skill" : ["pyhton","Power bi", "excel"]
}

# particular key exist or not ??
print("name" in my_dict5)
print("city" is not my_dict5)

# total number of keys and values
q1 = len(my_dict5)
print(q1)

print(len(my_dict5))

# program 6
my_dict6 = {
    "name" : "vaibhav",
    "lastname" : "katwe",
    "age" : 25,
    "skill" : ["pyhton","Power bi", "excel"]
}

# 3  ways
my_dict6.popitem()
print(my_dict6)
my_dict6.pop("age")
print(my_dict6)

# del my_dict6
del my_dict6["name"]
print(my_dict6)

# program 7 
# does dictionary store value by index
my_dict7 = {
    "name" : "vaibhav",
    "lastname" : "katwe",
    "age" : 25,
    "skill" : ["pyhton","Power bi", "excel"]
}

#print(my_dict7[0]) # error

# program 8 
my_dict8 = {
    "name" : "vaibhav",
    "lastname" : "katwe",
    "age" : 25,
    "skill" : ["pyhton","Power bi", "excel"]
}
for x in my_dict8:
    print(x)

for x in my_dict8.keys():
    print(x)

for x in my_dict8.values():
    print(x)

for x in my_dict8.items():
    print(x)

for k,v in my_dict8.items():
    print(k,v)

# program 9

my_dict9 = {
    "name" : "vaibhav",
    "lastname" : "katwe",
    "age" : 25,
    "skill" : ["pyhton","Power bi", "excel"]
}

my_dict9.clear()
print(my_dict9)

e = (["admin","costomer","manager"])
print(e)

vehicle ={
    "colour" : "red",
    "type" : "scv"
}
vehicle2=vehicle
vehicle["colour"] ="blue"
print(vehicle)
print(vehicle2)

vehicle2 = vehicle.copy()
vehicle2["colour"] ="red"

print(vehicle)
print(vehicle2)

# program 11
vehicle = {
    "color":"red",
    "type":"sedane"
}

for key in vehicle:
    print(key,vehicle[key])

#             0       1          2         3
names = ["vaibhav","mayuri","mahendra","jayashree"]
print(names)
print(names[0])

names[0] = "katwe"
print(names)

# allow duplicate value 

#          0       1       2       3      4 
fruit=["apple","mango","banana","mango","orange"]

print(fruit)

print("Apple" in fruit)
print(len(fruit))

numbers = [11,22,33,44]
print(len(numbers))

print(numbers[0])
print(numbers[4]) #ERROR