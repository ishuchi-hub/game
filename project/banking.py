#ef show_balance():
  #  pass
def deposit():
    while True:
        try:
            amount = float(input("\033[92mEnter the amount you want to deposit:\033[0m "))
            if amount <= 0:
                print("\033[91mPlease enter a greater than zero amount\033[0m")
            else:
                return amount
        except ValueError:
            print("\033[91mPlease enter a numeric value\033[0m")
def withdraw():
    while True:
        a= input("\033[92mEnter the amount you want to withdraw(or q to quit): \033[0m")
        if a.lower()=='q':
            break
        else:
            try:
                a=float(a)
                if a <= 0:
                    print("\033[91mPlease enter a greater than zero amount\033[0m")
                elif a >balance:
                    print("\033[91mYou don't have enough money\033[0m")
                else:
                    return a
            except ValueError:
                print("\033[91mPlease enter a numeric value\033[0m")
balance=0
while True:
    print("\033[93m===Welcome to Banking===\033[0m")
    print('1.show balance')
    print('2.deposit')
    print('3.withdraw')
    print('4.exit')
    use=input("Enter your choice:")
    if use=='1':
        print(f'Your balance is \033[92m{balance:.2f}\033[0m')
    elif use=='2':
        balance+=deposit()
    elif use=='3':
        withdraw()
    elif use=='4':
        print('Thank you for using Banking')
        break
    else:
        print('\033[91mInvalid choice\033[0m')