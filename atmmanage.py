class ATM:
    bankname="SBI"
    def init(self,accountno,accountholder):
        self.accountno=accountno
        self.accountholder=accountholder
        self.balance=1000

    def display(self):
        print(f"Account no : {self.accountno}")
        print(f"Account Holder : {self.accountholder}")
        print(f"Current Balance : {self.balance}")

    def balanceenquiry(self):
        print(f"Current balance : {self.balance}")

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposit amount : {amount}")
        print(f"Current balance : {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawal amount : {amount}")
            print(f"Current balance : {self.balance}")
        else:
            print("Insufficient balance")
        
obj1=ATM("1234xxxxxxx","Anu")
while True:
    choice=int(input("1.Display\n2.Balance enquiry\n3.Deposit\n4.withdraw\n5.Exit\nEnter the choice:"))
    if choice==1:
        obj1.display()
        print("========================")
    elif choice==2:
        obj1.balance_enquiry()
        print("========================")
    elif choice==3:
        amount=float(input("Enter the amount to deposit:"))
        obj1.deposit(amount)
        print("========================")
    elif choice==4:
        amount=float(input("Enter the amount to withdraw:"))
        obj1.withdraw(amount)
        print("========================")
    elif choice==5:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
        print("========================")
