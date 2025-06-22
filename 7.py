info = [
    {
    "firstName" : "vaibhav",
    "lastName" : "katwe",
    "age" : 25,
    "city" : "nashik",
    "skill" : ["python","sql,excel"]

},
{
    "firstName" : "mayuri",
    "lastName" : "pati",
    "age" : 29,
    "city" : "mumbai",
    "skill" : ["js","automation","excel"]
},
{
    "firstName" : "prashant",
    "lastName" : "nathe",
    "age" : 31,
    "city" : "nashik",
    "skill" : ["python","sql,excel"]
},
{
    "firstName" : "darshan",
    "lastName" : "lonare",
    "age" : 17,
    "city" : "sinnar",
    "skill" : ["excel","js","pandas"]
},
{
    "firstName" : "gaurav",
    "lastName" : "jadhav",
    "age" : 18,
    "city" : "sangamner",
    "skill" : ["python","sql,excel"]
}

]

# program 1
total = 0
for person in info:
   total = total + person["age"]

print(total/len(info))
 
# proram 2
# first name with city nashik

for person in info:
    if person ["city"] == "nashik":
     print(person["firstName"])

# program 3
for person in info:
   person["skill"].append("genAI")

for persone in info:
   print(person["skill"])

# program 4
# print name and number of skill
for person in info:
   print(f'{person["firstName"]}:{len(person["skill"])}')

# program 5
# list of firstName and LastName

for person in info:
   print(person["firstName"])
   print(person.get("lastName"))