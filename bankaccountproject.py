
class Cente_Mobile_Operation:

    def _init_(self):
        self.actName=""
        self.actNumber=0
        self.balance=0
        self.mmbalance=0

    def welcome(self):
        print("hello welcome to cente mobile, centenary bank online banking")    

class Displaying(Cente_Mobile_Operation):
    def display(self):
         self.balance+=self.balance
z=Displaying()
z.balance=40000
z.actName="Andinda Ruth"
z.actNumber=3201916420
print("\n Your details:\n Account Name AccountNumber Account Balance \n",z.actName, z.actNumber, z.balance)    

class Withdrawing(Cente_Mobile_Operation):
    def withdraw(self):
        amount=int(input("\nEnter amount to withdraw"))
        if amount<=self.balance:
            print("You have withdrawn:",amount)
        else:
            print("\nyou have inssufficient funds on your centenary acount")
        self.balance-=amount
        print("your new balance is:",self.balance)
x=Withdrawing()
x.actName="Andinda Ruth"
x.actNumber=3201916420
x.balance=40000
x.withdraw()

class Depositing(Cente_Mobile_Operation):
    def deposit(self):
        amount=int(input("\nEnter amount to deposit"))
        if amount<=self.mmbalance:
            print("You have deposited:",amount)
        else:
            print("\nyou have inssufficient funds on your mobile money")
        self.balance+=amount
        print("Your new balance is",self.balance)
y=Depositing()
y.actName="Andinda Ruth"
y.actNumber=3201916420
y.mmbalance=50000
y.balance=40000
y.deposit()