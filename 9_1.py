#implement constructor
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is %s and age is %d"%(self.name,self.age))
ob=person("karthikeya",18)
ob.display()
