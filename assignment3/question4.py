# Question4

class Bank_account:
    ac_no:int
    ac_name:str
    balance:int

    def __init__(self,ac_no,ac_name,balance):
        self.ac_no=ac_no
        self.ac_name=ac_name
        self.balance=balance

    
    def create_account(self):
        print(f"New account holder : {self.ac_name} with account number {self.ac_no} has balance {self.balance}")

obj=Bank_account(123283198,"Arun",25000)
obj.create_account()

