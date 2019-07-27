class Name:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def printUser(self):
        return self
name = Name('huyan',age='18')
print(name.printUser().name)