class Vehicle:
    """"Creating a car"""
    def __init__(self, model, year, engine, price, mileage):
        """"Initialization of attributes"""
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def getVehicleDescription(self):
        """"Getting information about vehicle"""
        description = "Car model: " + self.model + "\n" + "Year: " + str(self.year) + "\n"\
        + "Engine: " + str(self.engine) + "L" + "\n" + "Price: " + str(self.price) + " £" + "\n"\
        + "Mileage: " + str(self.mileage) + " Miles" + "\n" + "Wheels: " + str(self.wheels)
        print(description)

    def changeAmountOfWheels(self, amount):
        self.wheels = amount


vehicle1 = Vehicle("Audi RS7", 2012, 5.5, 185999, 1050)
vehicle1.getVehicleDescription()


class Truck(Vehicle):
    """"Creating new class Truck"""
    def __init__(self, model, year, engine, price, mileage):
        """"Initialization attributes of parental class"""
        super().__init__(model, year, engine, price, mileage)


vehicle_2 = Truck("MAN", 1999, 8.5, 199000, 250000)
vehicle_2.changeAmountOfWheels(8)
vehicle_2.getVehicleDescription()





