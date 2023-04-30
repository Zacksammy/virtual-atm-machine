import time

print("Please insert your CARD")
time.sleep(5)

password=1234
pin=int(input("enter your pin: "))
balance=500000

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
            print(f"Your current balance is {balance}")

        if option==2:
            withdrawal_amount=int(input("enter withdrawal amount: "))
            balance=balance-withdrawal_amount
            if withdrawal_amount >= balance:
                print(f"invalid,Please enter an amount less than {balance}")
            else:
                print(f"{withdrawal_amount} has been debited from your account")
                print(f"your new balance is {balance}")

        if option==3:
            deposit_amount=int(input("enter deposit amount: "))
            balance=balance+deposit_amount
            print(f"{deposit_amount} has been credited into account")
            print(f"your new balance is {balance}")

        if option==4:
            print("Tranaction ended,please take your card")
            break



else:
    print("Wrong pin,Please try again")
