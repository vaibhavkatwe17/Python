#             0       1          2         3
names = ["vaibhav","mayuri","mahendra","jayashree"]
print(names)
print(type(names))

# program 2 
names[0] ="mayuresh"
print(len(names))
print(names)

# program 3
name = ["vaibhav","mayuri","mahendra","jayashree"]
# del names
print("mayuri" in names)

# loop
cities = ["nashik","pune","mumbai","sangamner"]
for x in range(len(cities)):
#    print(x)
    print(cities[x])

i1 = 0 
while (i1 < len(cities)):
    print(i1)
    print(cities[i1])
    i1 = i1+ 1

# methods
#action and retrun type

friuts = ["mango", "apple", "banana","orange"]
#insert()
friuts.insert(2,"chikoo")
print(friuts)

# append()
friuts.append('grapes')
print(friuts)

# remove()
# pop()

vegetable =["brinjal","cauliflower","ladyfingur","tamato"]
vegetable.pop()
print(vegetable)
vegetable.pop(1)
print(vegetable)
vegetable.remove("ladyfingur")
print(vegetable)

# program 3
country = ["india","srilanka","japan","cuba","india","USA"]
e = country.count("india")
print(e)

country.reverse()
print(country)

country.sort()
print(country)

country.clear()
print(country)

numbers = [11,22,33,44]
numberB=numbers
print(numbers)
print(numberB)

numB = numbers.copy()
numB[0]=0
print(numB)
print(numbers)