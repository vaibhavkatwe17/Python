# list comprehension
# list comprehensio  --ouput list

# program 1
for x in range(1,6):
    print(x)
e1 = [x * x for x in range(1,6)]
print(e1)

#[expression : loop : conditon]
#program 2 
lst = [2,3,44,555,66,88,99]
e2 = [x for x in lst if x % 2 == 0]
print(e2)

# program 3
lst=[4,66,77,88,44,12]
e3 = ["even" if x % 2 ==0 else "odd" for x in lst]
print(e3)

# program 4 
names = ["vaibhav", "mayri","myuresh","rajesh"]
e4 = [x.upper() for x in names ]
print(e4)

# program 5 
people = [
    {"name" : "vaibhav","age" : 22},
    {"name" : "myuresh" ,"age" : 43 },
    {'name' :'ravi' ,'age' : 25 }

]
# [ vaibhav , mayuesh, ravi ]
e5= [x['name'] for x in people ]
print(e5)

# only get me dict where age is between 25 - 45
e6 =[ x for x in people if x['age'] >= 25 and x['age'] <= 45]
print(e6)

# names of persone in list age above 35
e7 = [ x ['name'] for x in people if x['age'] <23 ]
print(e7)

