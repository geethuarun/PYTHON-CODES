class bank:
    accno:int
    balance:int
    ac_type:str
    p_name:str
    def create_account(self,acc,bal,ac,p):
        self.accno=acc
        self.balance=bal
        self.ac_type=ac
        self.p_name=p

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your {self.accno} as been credited with amount {amount} your current balance is {self.balance}")


    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"Your {self.accno} as been credited with amount {amount} your current balance is {self.balance}")


holder=bank()
holder.create_account(12345,45689,"fixed","geethu")
# holder.deposit(1000)
holder.withdraw(1000)

#using constructor

class bank:
    accno:int
    balance:int
    ac_type:str
    p_name:str
    def __init__(self,acc,bal,ac,p):
        self.accno=acc
        self.balance=bal
        self.ac_type=ac
        self.p_name=p

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your {self.accno} as been credited with amount {amount} your current balance is {self.balance}")


    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"Your {self.accno} as been credited with amount {amount} your current balance is {self.balance}")


holder=bank(12345,45689,"fixed","geethu")
# holder.deposit(1000)
holder.withdraw(1000)


