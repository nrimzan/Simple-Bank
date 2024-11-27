#Write a program in order to write a bank acc., so you can perform:
#deposit operation into the bank acc., 
#also withdrawing money from the bank acc.
#enquiry to check balance

#MY METHOD
import time 
class Account:
    def __init__(self):
        
        self.balance = 0
    def deposit(self):
        money=int(input("Enter amount: $ "))
        self.balance += money
        time.sleep(2) #apparently this is how you delay texts in py
        print("$", money, "deposited into account")
        time.sleep(1)
        print("New balance after deposit is $",self.balance)
    def withdraw(self):
        money=int(input("Enter amount: "))
        if (money>self.balance):
            print("Insufficient balance")
        else:
            self.balance -= money
            print("Counting cash")
            time.sleep(1) 
            print("Please take the cash")
            time.sleep(2)
            print("New balance after withdraw is $",self.balance)
    def enquire(self):
        time.sleep(1)
        print("Your balance is: $",Acc.balance)

#Intro
formattedText = f"New bank account created. Pick an action:\n1.Enquire\n2.Deposit\n3.Withdraw"    
formattedText2 = f"Thank you for trusting our service. Bye."
print(formattedText)
Acc=Account()
action = input("Action: ")
if action in ('1', '1.','Enquire','enquire'):
    Acc.enquire()
elif action in ('2','2.','Deposit','deposit','depo'):
    Acc.deposit()
elif action in ('3','3.','Withdraw','withdraw'):
    Acc.withdraw()
else:
    print("no such action")

#repeat cycle
time.sleep(1)
ans=str(input("Do you wish to repeat?: "))
if ans in ('Yes', 'yes'):
    Acc=Account()
    action = input("Action: ")
    if action in ('1', '1.','Enquire','enquire'):
        Acc.enquire()
    elif action in ('2','2.','Deposit','deposit','depo'):
        Acc.deposit()
    elif action in ('3','3.','Withdraw','withdraw'):
        Acc.withdraw()
    else:
        print("no such action")
else:
    print(formattedText2)
    exit()

time.sleep(1)
print(formattedText2)