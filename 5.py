my_dict ={
    "Name": "Vaibhav",
    "Last Name " : "Katwe",
    "Age" :21
}

print(my_dict)
print(type(my_dict))

# Program 2
# Create / retrival / update / delete

my_dict ={
    "Name": "Vaibhav",
    "Last Name " : "Katwe",
    "Age" :21
}

print(my_dict)

# does dictinoary store the value by index ? - no
#print(my_dict[0]) -- no

# retrive
info = {
    "Name" : "Vaibhav",
    "Age" : 22,
    "City" : "Nashik"
}

print(info)
print(info["Name"])

e = info.get('Name')
print(e)

f = info.get("Age")
print(f)

# Program 2

info ={
    "name" : "Mayuri",
    "age"  : 26,
    "city" : "Mumbai"
}

print(type(info))
print(info["name"])

# update
info["name"] = "mayur"
print(info)

# add
info["language"] = "marathi"
print(info)

# search
print("name" in info)  # True
print("fname" in info)  # False

# program

info ={
    "name" : "ravi",
    "age"  : 45,
    "city" : "sinnar"
}

info.popitem()  # last key : value (delete)
print(info)

info.pop("age") # delect by key 
print(info)

info.clear() # ALLL  delect retrive empty dic {}
print(info)

# program
# does dictionary allow to store duplicate value

vehicle ={
    "colour" : "blue",
    "type"  : "suv"
}

for x in vehicle:
    print(x,vehicle[x])

for x in vehicle.keys():
    print(x)

for x in vehicle.values():
     print(x)

for x in vehicle.items():
    print(x)

# print(vehicle)
# print(vehicle.keys())
# print(vehicle.values())
# print(vehicle.items())

