class MpesaAccount:
    def __init__(self,name,phone,balance):
        self.name=name
        self.phone=phone
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
        print("Deposited",amount)
        print(f"Your balance is {self.balance}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -=amount
            print(f"Withdrawn {amount}")
            print(f"New balance is {self.balance} ")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print(f"Balance is {self.balance}")

user1=MpesaAccount("Vanessa",254706910506,5000)
user1.check_balance()
user1.deposit(6500)
user1.check_balance()
user1.withdraw(20000)

user2=MpesaAccount("Jermain",254712654987,8000)
user2.check_balance()
user2.deposit(30000)
user2.check_balance()
user2.withdraw(5000)

user3=MpesaAccount("Angela",254745234987,10000)
user3.check_balance()
user3.deposit(7000)
user3.check_balance()
user3.withdraw(5000)

user4=MpesaAccount("Jimmy",254789654234,9000)
user4.check_balance()
user4.deposit(10000)
user4.check_balance()
user4.withdraw(4000)

user5=MpesaAccount("Julia",254765489076,50000)
user5.check_balance()
user5.deposit(20000)
user5.check_balance()
user5.withdraw(10000)