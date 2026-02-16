''' object oriented programming '''

# Example 1

class Person: 
    # This is my class (the template contaning persons - name and age)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

person_1 = Person("Daniel",28)
person_2 = Person("Carlos",41)

person_1.greet()
person_2.greet()

# define the classes

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self.is_active = True
    
    
    def deposit(self, amount):
        if self.is_active:
            self.balance = self.balance + amount
            print(f"Deposit of {amount} complete \n Your new balance is {self.balance}")
        else:
            print("Your account is innactive")
    
    
    def withdraw(self, withdraw):
        if self.is_active:
            self.balance = self.balance - withdraw
            if self.balance < 0:
                print("Not enough funds!")
            else:
                print(f"Withdraw of {withdraw} complete, your balance is {self.balance}")
        else:
            print("Your account is innactive")

    
    def deactivate_account(self):
        self.is_active = False
        print("Your account has been deactivated")
    
    def activate_account(self):
        self.is_active = True
        print("Your account has been activated")

# create the instances
account_1 = BankAccount("Daniel", 88)

# Call the methods
account_1.activate_account()
account_1.deposit(5000)
account_1.withdraw(500)
account_1.deactivate_account()
account_1.deposit(5000)
account_1.withdraw(5000)