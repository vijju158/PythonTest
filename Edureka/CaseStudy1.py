'''
1. What is the output
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

Output:4
'''


''' 
2. What is the output
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

Output:['john', 'peter']
'''

#3.Password validity
'''
import re
u = input("Enter username : ")
p = input("Enter Password : ")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
'''

#4.Write a for loop that prints all elements of a list and their position in the list
'''
a = [4,7,3,2,5,9]

for i in a:
    print("Element: " + str(i) + ", Index: "+ str(a.index(i)))
'''

#5.Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes
'''
str = input("Enter a string : ")
modified_string = str[::2]
print(modified_string)
'''
#6 Print string in revrese order
'''
str = input("Enter a string : ")
print(str[::-1])
'''
#7. Print count of each charatcter in a string
'''
string=input("Enter the string : ")
newstr=list(string)
newlist=[]
for j in newstr:
    if j not in newlist:
        newlist.append(j)
        count=0
        for i in range(len(newstr)):
            if j==newstr[i]:
                count+=1
        print("{},{}".format(j,count))
'''

#8.Intersection if lists
'''
A=[1,3,6,78,35,55]
B=[12,24,35,24,88,120,155]
print(list(set(A).intersection(set(B))))
'''

#9.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
'''
mylist = [12,24,35,24,88,120,155,88,120,155]
print("Original List: ", mylist)
mylist = list(dict.fromkeys(mylist))
print("List after removing duplicate elements: ",mylist)
print(mylist[::-1])
'''

#10.List comprehension
'''
test_list = [12,24,35,24,88,120,155]
print( "The original list is: "+ str(test_list))
res = []
[res.append(x) for x in test_list if x not in res]
print("The list after removing duplicates: "+str(res))
'''

#11. Remove from list
'''
test_list = [12,24,35,24,88,120,155]
del test_list[0]
del test_list[3]
del test_list[4]
print(test_list)
'''

#12.delete numbers in list
'''
lst = [12,24,35,70,88,120,155]
lst = [x for x in lst if x%5!=0 and x%7!=0]
print(lst)
'''

#13. Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are divisible by 5 and 7 , between 1 and 1000 inclusive
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

#14.
n=int(input("Enter the number : "))
sum=0
for i in range(1,n+1):
    sum=sum+(i/(i+1))
print("The sum of series is: ",round(sum,2))