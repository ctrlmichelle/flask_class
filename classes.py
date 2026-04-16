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

bankAccount1.deposit()
bankAccount1.withdraw()
bankAccount1.display_info()

bankAccount2.deposit()
bankAccount2.withdraw()
bankAccount2.display_info()


