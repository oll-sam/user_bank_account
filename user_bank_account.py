class Bank_Account:
    bank_name = "Bank of Dojo"
    account = []
    def __init__(self,name,int_rate,account_balance):
        self.name = name
        self.int_rate = int_rate
        self.account_balance = account_balance
        Bank_Account.account.append(self)
    def deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} made a deposit. His new balance is {self.account_balance}.")
        return self
    def withdrawal(self, amount):
        self.account_balance -= amount
        if(self.account_balance > amount):
            print(f"{self.name} made a withdrawal. His new balance is {self.account_balance}.")
        else:
            self.account_balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount 
        other_user.account_balance += amount
        print(f"{self.name}'s Current Balance: {self.account_balance} | {other_user.name}'s Current Balance: {other_user.account_balance}")
        return self
    def yield_interest(self):
        account_rate = self.account_balance * self.int_rate
        if(self.account_balance > 0 ):
            self.account_balance -= account_rate
            print(f"Your interest rate of {self.int_rate} has been implemented.")
            return self
    def display_account_info(self):
        print(f"Balance: {self.account_balance}.")
        return self

    @classmethod
    def bank_account_info(cls):
        print("Account Info:")
        for info in cls.account:
            print(info.name, info.int_rate, info.account_balance)

    @staticmethod
    def yeild_interest(account_balance, ammount):
        if(account_balance - ammount) < 0:
            return False
        else:
            return True


sam =   Bank_Account("Sam", .125, 1000)
rob = Bank_Account("Rob", .065, 2500)

# sam.make_deposit(100).make_deposit(100).make_withdrawal(2000).transfer_money(rob, 20).yield_interest()
# sam.display_account_info()
# rob.make_withdrawal(100).transfer_money(sam, 1500).yield_interest()
# rob.display_account_info()

Bank_Account.bank_account_info()

class User:
    bank_name = "Bank of Dojo"
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = Bank_Account(name= self.name, int_rate=0.02, account_balance=10)
    def make_deposit(self):
        self.account.deposit(100)
        print(self.account.account_balance)
        return self
    def make_withdrawal(self):
        self.account.withdrawal(250)
        print(self.account.account_balance)
        return self
    def display_user_balance(self):
        print(self.account.account_balance)
        return self

guido = User("Guido", "guido@codingdojo.com")
marvin= User("Marvin", "marvin@codingdojo.com")

guido.make_deposit().make_deposit().make_withdrawal().display_user_balance()
marvin.make_deposit().make_withdrawal().display_user_balance()