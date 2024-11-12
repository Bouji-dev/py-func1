from heater import Heater
class Car:
    def __init__(self,model , color, year):
        self.model = model
        self.color = color
        self.year = year
        self.heater = Heater()


    def break_(self):
        print(f"the car with model{self.model} stopped")

    def turnHeaterOn(self,temp = 25):
        self.heater.on()
        self.heater.reachRequestedTemp(temp)

    def move_(self):
        print(f"The car{self.model} with color:{self.color} is moving")

