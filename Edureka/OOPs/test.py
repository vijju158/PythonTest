class number():
    pass

x=number()
print(x)

class Edureka():
    def Hello(self):
        print("Happy Learning")
    empcount=0

ob=Edureka()
ob.Hello()
print("Edureka.__dict__:",Edureka.__dict__)
print("Edureka.__doc__:",Edureka.__doc__)
print("Edureka.__name__:",Edureka.__name__)
print("Edureka.__module__:",Edureka.__module__)
print("Edureka.__bases__:",Edureka.__bases__)


class test():
    def __init__(self):
        self.__pri=("I am Private")
        self._pro=("I am protected")
        self.pub=("I am public")
ob=test()
print(ob.pub)
print(ob._pro)
print(ob.__pri)