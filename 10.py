# variable 
# int , float , boolean str
# type --- comparison , logical operator
# conditional statement , loops for while 
# list - CRUD  -- create , retrive , update ,delete / loop - methods
# dict - CRUD   --  loop - methods
# tuple - Cr - methods  CRUD
# str - CRUD , Methods

fn = "vaibhav"
a = fn.upper()
print(a)
 
In = "Katwe"
s=In.lower()
print(s)

x = "mayuri"
y = x.capitalize()
print(y)

info = " I Am Lerning Pyhton"
l = info.istitle()
print(l)

# string formate methods

f = " goa "
print(len(f))
e5 = f.strip()
print(e5)
print(len(e5))


f1 = "goa"
print(len(f1))
e6 = f.strip()
print(e6)
print(len(e6))

f3 = "  goa  "
print(len(f3))
e7 = f.strip()
print(e7)
print(len(e7))

s = "hello"
e8 = s.center(10,"_")
print(e8)

s1 = "hello"
e9 = s.rjust(10,"_")
print(e9)

#zfill
ide ="89"
e = ide.zfill(5)
print(e)

# String check methods 
print('abcdef'.isalpha())
print('123456'.isnumeric())
print('123456'.isalnum())
print('123aaabbb'.isalnum())
print('aaaaaa'.isalnum())
print(''.isalnum())
print('abc'.islower())
print('ABC'.isupper())
print(" ".isspace())
print("I Am Learning Python".istitle())

# search method
# 0123456
s = "hello world"
e = s.find("world")
print(e)

s2 = "hello world hellow"
e2 = s2.rfind("hellow")
print(e2)

city = "nashik"
# 0 1 3 4 5 6 
# n a s h i k

print("hellow")
d = city.index("n")
print(d)
print("bye")

s3 = "hello world hello"
y3 = s3.rindex("hello")
print(y3)

j = "hello hello hello"
h = j.count("l")
print(h)

info = "i am learning js"
e = info.replace("Python","js")
print(e)

# splitting and join methods
s1 = "apple,banana,grape"
e1 = s.split(',')
print(e1)


info = ["vaibhav","kawe","7745070870"]
r = "-".join(info) #vaibhave@7745070870
print(r)


h = "vaibhav"
e = h.startswith('va')
print(e)

f = h.startswith('v')
print(f)

b = "katwe"
f2 = b.endswith('e')
f3 = b.endswith('we')
print(f2)
print(f3)