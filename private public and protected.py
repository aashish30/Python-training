class Print():
    __name="Ash" #private member cannot be calles outside the class
    _name="pri"# protected member can be called from the inherited class made as _(variable name)
    def get_String(self,s):
        self.str1=s


    def print_String(self):
        print("the string is ",self.str1.upper())
        print(self.__name)#this privatte member can be called inside the class only

a=Print()
# print(a.__name)
a.get_String("ashish")
a.print_String()


class fun(Print):
    pass
a1=fun()
print(a1._name)#protected member of base class can only be used in the derived class
