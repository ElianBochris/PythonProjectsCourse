class Person():
    def __init__(self,name,lastName):
        self.name=name
        self.lastName=lastName
    def FullName(self):
        print(self.name+" "+self.lastName)

new_person=Person("elian","bochris")
new_person.FullName()