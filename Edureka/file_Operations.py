import os

newfile=open("Edureka.txt","r")
print(newfile.name)
print(newfile.mode)
#for i in range(0,10):
#    newfile.write("\n Hello, Welcome to Python:")
#print(newfile.softspace)

#
#for i in range(0,10):
#    newfile.write("\n Hello, Welcome to Python:")

#for i in range(1,10):
#    print(newfile.read(500))

#os.rename("Edureka.txt","new.txt")
#os.remove("new.txt")

newfile.seek(5)
print(newfile.read(50))
print(newfile.tell())
