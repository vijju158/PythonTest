#Lists, Dictionaries & Sets are mutable Data Types
#Lists
List1 = ["Geeks", "For", "Geeks"]
List2 = [1,2,2.15, 'edureka',(1,2,3)]
print(List2)
print(List2[3])
List2[1]='Test'
print(List2[1])
print(List2[4][1])
print("Type of List: ", type(List1))

#Dictionaries
dic={'Age':24,'Name':'John'}
print(dic)
print(dic['Age'])
print(dic['Name'])
print("Type of dict: ",type(dic))

#Sets
sets={1,2,3,3}
print(sets)
print("Type of set: ",type(sets))

