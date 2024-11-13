class Employee():
    def __init__(self,fname , lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def access(self):
        print( "General access")


class It(Employee):
    def __init__(self,fname,lname,age,id):
        Employee.__init__(self,fname , lname, age)
        self.id = id

    def welcome(self):
        print(f"Welcome to {self.fname,self.lname}for choosing our university")