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
    def __init__(self, uid, balance):
        self.uid = uid
        self.balance = balance
        self.rented_cars = []

    
    def rent_user(self, car):
        if car.available:
            if self.balance >= car.price:
                car.rent_car()
                self.rented_cars.append(car)
                self.balance -= car.price
                print(f"Thanks for your purchase, your new balance is {self.balance}")
            
            else: 
                print("ERROR: Insuficient balance, please top up your account")
                
        else:
            print(f"ERROR: the car {car.plate} is not available")

    
    def ret_user(self, car):
        if car in self.rented_cars:
            car.ret_car()
            self.rented_cars.remove(car)
            print("Thanks for use our services")
        else:
            print(f"ERROR: user {self.uid} has not rented the car {car.plate}")


class Dealer:
    def __init__(self):
        self.users = []
        self.cars = {}


    def add_user(self,user):
        if user not in self.users:  
            self.users.append(user)
            print(f"{user.uid} added")
        
        else:
            print(f"ERROR: user {user.uid} already exist")

    
    def add_car(self, car):
        if car.plate not in self.cars:
            self.cars[car.plate] = car
            print(f"the car {car.plate} was added")
        
        else: 
            print(f"ERROR: The car {car.plate} already exist")


    def top_up_user(self, user, top_up):
        if user in self.users:
            user.balance += top_up
            print(f"The new balance for user {user.uid} is {user.balance}")
        else:
            print("ERROR: User not found")
    

    def show_users(self):
        return [user.uid for user in self.users] 
    

    def show_cars(self):
       return [car for car in self.cars]

CAR_1 = Cars("Toyota","BLA979",500)
CAR_2 = Cars("Mazda","AGT007",350)
USER_1 = User(282930,5000)
USER_2 = User(100007,2000)
DEALER = Dealer()

DEALER.add_user(USER_1)
DEALER.add_user(USER_2)
DEALER.add_car(CAR_1)
DEALER.add_car(CAR_2)
print(DEALER.show_users())
print(DEALER.show_cars())

DEALER.top_up_user(USER_1,3000)

USER_1.rent_user(CAR_1)