class Car:
    def __init__(self, brand, model, price, plate):
        self.brand = brand
        self.model = model
        self.price = price
        self.plate = plate
        self.available = True

    
    def sell(self, car):
        if self.available:
            print(f"Sucess: The car {car.brand} {car.model} was sold")
        else:
            print(f"ERROR: The car {car.brand} {car.model} is not available for sale")

    
    def get_availability(self):
        return self.available
    
    
    def get_price(self):
        return self.price
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.owned_cars = []

    
    def buy_car(self, car):
        if car.available:
            car.available = False
            self.owned_cars.append(car)
            print(f"Car {car.brand} sold to client {self.name}")
        else:
            print(f"Car {car.brand} was already pruchased by other client")


    def check_availability(self, car):
        availability = "available" if car.available else "not available" 
        print(f"The car {car.brand} is {availability} {f"and cost {car.price}" if car.available else " "}")
    

    def purcahsed_cars(self):
        return [car.brand for car in self.owned_cars]

class Dealership:
    def __init__(self):
        self.clients = []
        self.unique_plates = {}

    def add_client(self,client):
        self.clients.append(client)
        print(f"The client {client.name} was added")

    def add_car(self, car):
        if car.plate not in self.unique_plates:
            self.unique_plates[car.plate]=car
            print(f"Car {car.plate} added")
        else:
            print(f"Car {car.plate} already exist and cannot be added")

    def inventory(self):
        print("The available cars are: \n")
        unique_cars=[]
        
        for plate in self.unique_plates:
            unique_car = self.unique_plates.get(plate)
            if unique_car.available:  
                unique_cars.append(unique_car.brand)
        return unique_cars


CAR_1 = Car("Toyota", "1997",10000,"ABC123")
CAR_2 = Car("Renault", "2005", 2500,"ABC456")
CAR_3 = Car("Mazda", "2009", 3500,"ABC007")

CLIENT_1 = Customer("Daniel")
CLIENT_2 = Customer("Ana")

DEALERSHIP = Dealership()

# ---- Add cars and clients to the dealership
DEALERSHIP.add_client(CLIENT_1)
DEALERSHIP.add_client(CLIENT_2)
DEALERSHIP.add_car(CAR_1)
DEALERSHIP.add_car(CAR_2)
DEALERSHIP.add_car(CAR_1)

CLIENT_1.check_availability(CAR_1)
CLIENT_1.buy_car(CAR_1)
CLIENT_2.check_availability(CAR_2)
CLIENT_1.buy_car(CAR_2)
CLIENT_2.buy_car(CAR_2)

DEALERSHIP.add_car(CAR_3)
print(DEALERSHIP.inventory())