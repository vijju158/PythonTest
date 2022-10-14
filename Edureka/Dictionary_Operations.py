d={1:"Python",2:"Android"}
print(d)
print(d[1])
d[1]="Java"     #Updating dictionary elemnts
print(d)
#del (d[2])      #Deleting dictionary elements
#print(d)

#built in functions of dictionaries
print(len(d))       #prints lenghth of dictionary
print(str(d))       #returns the dictionary as string
print(type(d))      #returns type

rec={'name':{'first':'Bob', 'last':'smith'},'jobs':['dev','mgr'], 'age':40.5, 'degree':{'be','pg','ie'}, 'cash':(1,2,3)}
print(rec)
print(rec['degree'])
print(rec.get('name'))
print(rec['age'])


##Methods of Dictionaries
print(rec.items())
print(rec.keys())
print(rec.values())
print(rec.setdefault(1,4))
print(rec.copy())
rec.clear()
print(rec)

#Sorting keys
d={3:"Python",1:"Java",2:"Big Data"}
ks=list(d.keys())
print(ks)
sk=sorted(ks)
print(sk)

for key in sk:
    print(key,'=>',d[key])


##Tuple and List in dictionary
d={1:(1,2,3), 2:(3,4,5)}
print(d)
print(d[1][1])

d={1:[1,2,3], 2:["Java","Python"]}
print(d)
print(d[2][1])

