"""

Polymorphism:

    1. Operator Overloading
    2. Method Overloading / Overriding
    3. Constructor Overloading / Overriding

1. Operator Overloading

<operand><operator><operand>
1 + 2 = -1

"""

class OperatorOverloading:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages - other.pages
        return total_pages

obj1 = OperatorOverloading(10)
obj2 = OperatorOverloading(5)

print(obj1 + obj2)


#Method Overloading
class A:
    def add(self):
       print("Addition of X and Y")


class B(A):
    def add(self):
        print("different defination")

obj=B()
obj.add()



#Method Overloading
class MethodOverloading:

    def __init__(self):
        print("Inside default constructor")

    def __init__(self,name):
        self.name = name
        print("Inside parametrized constructor")

    def add(self,a,b):
        return a+b

   # def add(self,a,b,c):
    #    return a+b+c


#obj3 = MethodOverloading()
#print(obj3.add(10,20))
#print(obj3.add(10,20,30))
obj4 = MethodOverloading("Rahul")
print(obj4.add(10,20))