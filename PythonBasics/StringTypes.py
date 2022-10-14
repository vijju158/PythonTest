print(type("This is a String"))

#String can be in double quote
a="Welcome to W2A"
print(a)

#String can be in single quote
b='Welcome to W2A'
print(b)

##Multi Line Comment
'''
Hey
My Name is "Vijay"

'''

print('Hey, My Name is "Vijay"')

e = "Hey" \
    "My name is" \
    "Vijay"
print(e)

#print in different lines
g = """
Hey
My Name is:
Vijay
"""
print(g)

print("This is Vijay's \"New\" house")

#Accessing String
name="Vijay"
print(name[0])  #first value
print(name[4])  #last value
print(name[1:4])  #prints from and to the given index
print(name[1:4:2])
print(name[::])
print(name[::2])
print(name[::1])
print(name[::-1])   #Reverse a String
print(name[::-2])

print(len(name))

#Strip - Removes white spaces
abc=" Hello, World "
print(abc)
print(abc.strip())

#Lower and upper case conversion
print(name.lower())
print(name.upper())

#Split String
abc="Hello, World "
b=abc.split(",")
print(b)
print(b[0])
print(b[1])
print(b[1].strip())

#Concatention
ab="Hi"
cd=" Vijay"
print(ab+cd)

#Concatention - can be done with similar data types only
print("1j"+"2j")
print("10"+"10")

#repitetion
print("10"*4)
print("ba"+"na"*2)


city="New Delhi"

print("Hey, I live in ",city)

# f-Strings
# format()
# %
Age=35
id=10.12

print(f"Hey, I live in {city}, My Age is {Age} and id is {id}")


print("Hey, I live in {}, My Age is {} and id is {}".format(city,Age,id))


print("Hey, I live in %s, My Age is %d and id is %f"%(city,Age,id))