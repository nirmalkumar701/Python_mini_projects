class ATM:
    def __init__(self,balance):
        self.balance = balance
    
    def check_balance (self):
        return f"Your balace is ${self.balance}"
    
    def deposit(self,amount):
        self.balance += amount
        return f"Deposited {amount} successfuly. New balance is {self.balance} "
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            print (f"Witdrew ${amount}... Your new balance is ${self.balance}")
        else:
            print("Insufficient Balance Please try again !")
atm=ATM(float(0))
while True:
    print("choice 1.Check Balance")
    print("choice 2.Deposit")
    print("choice 3.Withdraw")
    print("choice 4.Exit")

    Choice=int(input("Enter choice : "))

    if Choice==1:
        print(atm.check_balance())
    elif Choice==2:
        amount=int(input("Enter amount: "))
        print(atm.deposit(amount))
    elif Choice==3:
        amount=int(input("Enter amount: "))
        print(atm.withdraw(amount)) 
    elif Choice==4:
        print("Thanks for Visiting! Come again!!!")
        break
    else:
        print("Invalid operation Please try again")