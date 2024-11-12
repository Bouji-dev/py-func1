from abc import ABC, abstractmethod


class Animal(ABC):

    @property
    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Cat(Animal):
    @property
    def age(self):
        return 2

    def run(self):
        print("cat is running")