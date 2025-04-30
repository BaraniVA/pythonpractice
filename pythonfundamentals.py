#Variables
#Variable Naming Conventions
#Variables are case-sensitive
#Variable names can only contain letters, numbers, and underscores

print("Variables")
a=1
print(a)

_a=2
print(_a)

A=3
print(A)

#Data Types
print("Data types")
b="Hi" #string
c=20 #integer
d=3.14 #float
e=True #boolean
f=None #NoneType
g={1:"mango",2:"banana",3:"apple"} #dictionary
h=[1,2,3,4,5] #list
i=(1,2,3,4,5) #tuple

print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

#Set

print("Set Data type")
j=set("1")
print(type(j))
print(j)

#Tuple

print("Tuple Data type")
k=(1,2,3,4,5)
print(type(k))
print(k[1])

#Dictionaries

print("Dictionary Data type")
l={"A":"Apple", "B":"Ball"}
print(type(l))
print(l["A"])


#Operators
#Arithmetic Operators

add = 1+2
sub = 5-10
mul = 20*10
div = 100/10
mod = 100%3

print(add)
print(sub)
print(div)
print(mul)
print(mod)

#Assignment Operators
Leo="Leo Das"
print(Leo).rstrip()

#Boolean Operators

print(1==1)
print(1!=1)
print(1>1)
print(1<1)
print(1>=1)
print(1<=1)

#Logical Operators

print(1 and 2)
print(1 or 2)
print(not 1)

#Bitwise Operators

print(1 & 2)
print(1 | 2)
print(1 ^ 2)
print(~1)
print(1 << 2)


#Membership Operators

print(1 in k)
print(1 not in k)

print("apple" in g)


#Input / output

Name = input("Enter your Name: ")
print("Hello", Name)
Age = int(input("Enter your Age: "))
print("Your Age is", Age)

print(f"Hello {Name}, Your Age is {Age}")

print("Hello {}, Your Age is {}".format(Name, Age))

print("Hello %s, Your Age is %d" % (Name, Age))

#file read/write
# Writing to a file
with open("filename.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("filename.txt", "r") as file:
    content = file.read()
    print(content)


