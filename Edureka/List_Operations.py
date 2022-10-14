#lists Indexing & Slicing

list=["Hadoop","Python","Android"]
print(list[1])
print(list[0:2])
print(list[-1])

#Updating & Deleting Elemnts
list[1]="Java"
print(list)
del(list[2])
print(list)

#remove & Pop functions
list=[1,2,3,4,5,'a','b','c']
print(list.pop(3))
list.remove('a')
print(list)

#Type
list=[1,2,5,'python','Hadoop']
print(type(list))
print([x**2 for x in[1,2,3,4,5]])

#Lists build in Functions
list=[1,2,3]
list.append('Machine Learning')
print(list)

list.extend(['g','h'])
print(list)

list.insert(5,'Scripting')
print(list)

list.remove(3)
print(list)
list1=['z','x','a']
print(sorted(list1)) #Sorts the list
print(list[::-1]) #Reverse the List


#Tuples inside a List
list=[(1,2,3),("Python", "Java", "hadoop")]
print(list)
print(len(list))
print(list[0][0:2])
print(list[1][0:2])
print("test")
list[1][0]=50
print(list)
