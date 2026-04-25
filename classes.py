class Person:
    def __init__(self,name,age,address,email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def talks(self):
        print(f"{self.name} talks")

    def walks(self):
        print(f"{self.name} is walking")

        
#person1 object      
person1 = Person("Mike",24,'Karen','mike@mail.com')
print(type(person1))
print(person1.address)
person1.talks()
person1.walks()


#person2 object
person2 = Person("Kate",21,'Eastleigh','kate@mail.com')
print(type(person2))
print(person2.name)
person2.talks()
person2.walks()

class BankAccount:
    def __init__(self, account_number, balance, name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.date_opened = date_opened

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.name} deposited {amount}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"{self.name} withdrew {amount}")


# bankaccount1 
bankAccount1 = BankAccount("88210", 1000, "Mike", "15-04-2024")

# bankaccount2 
bankAccount2 = BankAccount("88211", 500, "Kate", "16-04-2024")

bankAccount1.deposit(1000)
bankAccount1.withdraw(500)
bankAccount1.display_info()

bankAccount2.deposit()
bankAccount2.withdraw()
bankAccount2.display_info()


class Car:
    def __init__(self, brand, model, year, fuel_capacity, fuel_level, is_running):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running

    def start(self):
        print(f"{self.brand} starts")

    def stop(self):
        print(f"{self.brand} stops")

    def refuel(self):
        print(f"{self.brand} refuels")

    def drive(self):
        print(f"{self.brand} drives")

    def display_car_info(self):
        print(f"Car details: {self.brand}, {self.model}, {self.year}, {self.fuel_capacity}, {self.fuel_level}, {self.is_running}")


car1 = Car("Chevrolet", "Toyata", 2025, "25L", "5L", True)
car1.start()
car1.stop()
car1.refuel()
car1.drive()
car1.display_car_info()



