print("Hellow")
print("Vaibhav")

#        0  1  2
lista = [11,22,33]
# retrive
print(lista[0])
print(lista[1])


# updates

lista[0] =111
print(lista)

# in 
print(111 in lista) # True or False 

# length
w = len(lista)
print(w)

# del lista


# loop 
#            0       1        2
cities = ["pune","munbai","banglore"]

# for - range
for x in range(len(cities)) :
    print(x)
    print(cities[x])

# for
for x in cities:
    print(x)

## while
i1=0
while(i1<= len(cities)):
    print(cities[i1])
    i1=i1+1
