str1="Welcome"
str2="to"
str3="Edureka"
print(str1,str2,str3)
print(len(str1))    #length of string
print(str1[1:3])    #Indexing & Slicing operations
print('l' in str1)  #Membership Checking
print('t' in str1)

#String formatting Operations
print("Welcome to %s"%("Python"))
print("My name is %s and my age is %d"%("Annie",22))


#Build in String Methods
str="edureka"
print(str.capitalize()) #Capitalizes the first letter
print(str.count("e",0,len(str)))
s=str.encode('utf-8','strict')
print(s)
print(max(str))
print(min(str))
print(str.replace('e','---E---',1))
print(str.upper())
print(str.index('k'))
print(str[::-1])
print(str[1:5])
print(str.find('u'))
str2="Welcome"
print(str+str2)
print(str*3)

