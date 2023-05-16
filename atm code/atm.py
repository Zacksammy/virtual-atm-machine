import time
import random
import decimal
import datetime

current_time = datetime.datetime.now()

print("Current time is: ", current_time)
print("Please insert your CARD")
time.sleep(5)
password= 1234
pin=int(input("enter your pin: "))
balance= decimal.Decimal(int(random.uniform(1,1000000)))


if pin == password:
    while True:
    
        print("""
        1 == balance
        2 == withdraw
        3 == deposit
        4 == exit
        """)

        try:
            option =int(input("Please select your choice: "))
        except:
            print("Please enter a vailid option")

        if option==1:
            print("checking balance...")
            time.sleep(4)
            print(f"Your current balance is {balance}")
            time.sleep(4)
            

        if option==2:
            withdrawal_amount=int(input("enter withdrawal amount: "))
            balance=balance-withdrawal_amount
            print("checking...")
            time.sleep(4)
            if withdrawal_amount >= balance:
                print(f"invalid,Please enter an amount less than {balance}")
            if withdrawal_amount >= 50000:
                print("You cannot withdraw more than 50,000 in a single transaction")
            else:
                print(f"{withdrawal_amount} has been debited from your account")
                print(f"your new balance is {balance}")
            time.sleep(4)

        if option==3:
            deposit_amount=int(input("enter deposit amount: "))
            balance=balance+deposit_amount
            print("checking...")
            time.sleep(4)
            print("Successful!!!")
            time.sleep(2)
            print(f"{deposit_amount} has been credited into account")
            print(f"your new balance is {balance}")
            time.sleep(4)

        if option==4:
            print("...")
            time.sleep(4)
            print("Transaction ended,please take your card")

            
            break
            



else:
    print("Wrong pin,Please try again")



