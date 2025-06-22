fn = "vaibhav"
a = fn.upper()
print(a)

In = "Vaibhav"
s=In.lower()
print(s)

x = "mayuri"
y = x.capitalize()
print(y)

city ="NASHIK"
c = city.isupper()
print(c)

city = "Pune"
p = city.islower()
print(p)

info = " I Am Lerning Pyhton"
l = info.istitle()
print(l)

str1 = "1234567890"
s1=str1.isnumeric()
print(s1)

str2 = "vmk"
s2 = str2.isalpha()
print(s2)

str3 = "v123456" # only alpha , on;y numbers
s3=str3.isalnum()
print(s3)

country = "India"
c1= country.startswith("i")
c2 =country.startswith("india")

print(c1)
print(c2)

c3 = country.endswith("a")
c4 = country.endswith("ia")

print(c3)
print(c4)

print(" ".isspace())
print(len("  "))