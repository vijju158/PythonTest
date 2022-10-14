"""
Public

Protected  - _   _var, def _method()

Private - __var, def __method()


"""

class Car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside Car constructor")

    def publicMethod(self):
        print("Calling public method")


    def _protectedMethod(self):
        print("Calling protected method")



    def __privateMethod(self):
        print("Calling private method")

obj=Car()
print(obj.publicVar)
print(obj._protectedVar)
#print(obj.__privateVar)
obj.publicMethod()
obj._protectedMethod()
obj.__privateMethod()
