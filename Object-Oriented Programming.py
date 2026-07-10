class ElectricCar:
    def __init__(self, brand, model, battery_size):
        self.brand = brand
        self.model = model
        self.battery = battery_size

    def describe_car(self):
        return f"{self.brand} {self.model} with a {self.battery}kWh battery."

# Creating an instance (object) of the class
my_ev = ElectricCar("Tesla", "Model Y", 75)
print(my_ev.describe_car())
