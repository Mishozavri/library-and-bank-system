class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} {self.balance}")
        else:
            print("თანხა უნდა იყოს დადებითი.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount}გატანილია. მიმდინარე ბალანსი: {self.balance}₾")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"{self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"დაემატა {interest}სარგებელი ({self.interest_rate*100}%). ახალი ბალანსი: {self.balance}")


# ---- ტესტირება ----
acc = BankAccount("გიორგი", 100)
acc.deposit(50)
acc.withdraw(200)
acc.get_balance()

print("\n=== დანაზოგის ანგარიში ===")
sav = SavingsAccount("ნინო", 1000, 0.1)
sav.apply_interest()
sav.get_balance()