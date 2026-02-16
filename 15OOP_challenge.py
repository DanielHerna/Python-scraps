class Cars:
    def __init__(self, brand, plate, price):
        self.brand = brand
        self.plate = plate
        self.price = price
        self.available = True


    def rent_car(self):
        if self.available:
            self.available = False
            print(f"car {self.plate} rented")
        
        else: 
            print(f"car {self.plate} not available for rent")

    def ret_car(self):
        if self.available:
            print(f"car {self.plate} is not rented")
        else:
            self.available = True
            print(f"car {self.plate} returned to the dealer")

class User:
    def __init__(self, balance,uid):
        self.uid = uid
        self.balance = balance
        self.rented_cars = []

    
    def rent_user(self, car, balance):
        if car.available and balance >= car.price:
            car.rent_car()
            self.rented_cars.append(car)
            self.balance -= car.price
            print(f"Thanks for your purchase, your new balance is {self.balance}")
        else:
            print("Insuficient balance, please top up your account")

    
    def ret_user(self, car):
        if car in self.rented_cars:
            car.ret_car()
            self.rented_cars.remove(car)
            print("Thanks for use our services")
        else:
            print(f"user {self.uid} has not rented the car {car.plate}")


class Dealer:
    def __init__(self, users, cars):
        self.users = []
        self.cars = {}


    def add_user(self,user):
        if user not in self.users:  
            self.users.append(user)
            print(f"{user.uid} added")
        
        else:
            print(f"{user.uid} already exist")


    def add_car(self,car):
        if car.plate not in self.cars:
            self.cars[car.plate] = car
            print(f"{car.plate} added")
        else:
            print(f"Error, the car {car.plate} already exist")

