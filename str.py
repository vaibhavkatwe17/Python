fn = "Vaibhav"
print(fn)

info = """
I am learning js and python for automation
and this is imp
"""
info = '''
I am learning js and python for automation
and this is imp
'''
print(type(fn))

# program 2 
city = "pune"
print(city)
h = len(city)
print(h)

# program 3
city = "nashik"
e = city[0]
print(e)

# program 4
# mutable ??
# city2 = "sinnar"
# city2[0] ="y"

# program 5 
city = "nashik"
print("n" in city)
print("na" in city)
print("n" in city)

#program 6
fn = "arna"
print(fn)

# program 8
city = "nashik"
#  0    1   2   3     4    5
#  n    a   s    h    i     k
print(city[0])
print("n" in city)
print("na" in city)
print("N" in city)


for a in range(len(city)):
    print(a)
    print(city[a])

for char in city:
    print(char)

k = 0
while(k < len(city)):
   # print(k)
    print(city[k])
    k = k + 1

# program 9

city2 = "Nagpur"

# 0   1   2   3   4   5   
# N   a   g   p   u   r   
# -6 -5  -4 -3   -2    -1

#slicing (startIndex:endIndex(not inclueded):step)
# len - 1 is always index

print(city2[:6])
print(city2[0:10])
print(city2[1:6])
print(city2[2:-1])
print(city2[-8:8])
print(city2[-1:-3])
print(city2[::2])
print(city2[::-1])


# my first name is vaibhav and lastName is katwe
fn = "vaibhav"
ln = "katwe"

print("My firstName is "+fn+" and my lastName is "+ln)
print(f"My firstName is {fn} and my lastName is {ln}")
