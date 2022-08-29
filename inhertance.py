# class Animal:
#     def Print_name(self,name):
#         self.name=name
#         print("name",self.name)
#
#
# class dog(Animal):
#     def bark(self):
#         print("dog barkks")
#
#
# a=dog()
# a.Print_name("Ashish")
# a.bark()
# print(a.name)



# class Animal:
#     def Print_name(self,name):
#         self.name=name
#         print("name",self.name)
#
# class dog(Animal):
#     def __init__(self, breed):
#         self.breed=breed
#     def bark(self):
#         print("dog barkks")
#     def Print_breed(self):
#         print(self.breed)
#
# a=dog("german")
# a.Print_breed()
# a.bark()
# a.Print_name("ashish")


class Animal:
    def __init__(self,name):
        self.name=name
    def Print_name(self,):
        print("name",self.name)

class dog(Animal):
    def __init__(self, breed,name):
        self.breed=breed
        Animal.__init__(self,name)
    def bark(self):
        print("dog barkks")
    def Print_breed(self):
        print(self.breed)

a=dog("german","ashish")
a.Print_breed()
a.bark()
a.Print_name()

