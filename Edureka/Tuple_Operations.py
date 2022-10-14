t=("Hadoop","Python","Java")
print(len(t))
print(max(t))
print(min(t))

t1=(1,3,2,5)
print(sorted(t1))
print(t1[::-1])
print(t1[1])
print(t1[0:2])


t=("Hadoop","Python","Java")
print(t*2)
print("Java" in t)

t2=(1,3,5,7)
t3=(2,4,6,8)
t4=t2+t3
print(t4)

#del (t2[2])
print(t2)

#List inside a Tupe
t=([1,2,3],[3,4,5],[5,6,7])
print(t)
print(len(t))
print(t[0][0:2])    #Slicing

t[1][0]=90
print(t)
del (t[1][2])
print(t)

#Converting Tupes into List & back to Tuples
tup=(1,2,3,4,'a','b','c')
print(tup)
lst=list(tup)
print(lst)
lst[1]='Python'
print(lst)

tup=tuple(lst)
print(tup)



