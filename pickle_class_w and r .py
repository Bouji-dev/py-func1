import pickle


class Person:
    def __init__(self,fname,lname,age):
        self.firstName = fname
        self.lastName = lname
        self.age = age

p = Person("Ehsan","Bouji",43)




with open("obj.pickle", "wb") as f:
    pickle.dump(p,f)

with open("obj.pickle", "rb") as f:
    p_read = pickle.load(f)

