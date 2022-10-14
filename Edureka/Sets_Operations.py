x=set('Welcome to Edureka')
print(x)

A={1,2,3,4}
B={3,4,5,6}
C={1,2}
print(A|B)      #union
print(A&B)      #Intersection
print(A-B)      #Difference
print(B-A)

print(1 in A)   #Membership Testing
print(B.issubset(A))
print(C.issubset(A))
print(5 not in A)
print(A.issuperset(B))
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

##Operations on Sets
A.add('c')      #Adds element to Set
print(A)
A.remove('c')   #removes element to set
print(A)

A.pop()
print(A)

A.clear()
print(A)
