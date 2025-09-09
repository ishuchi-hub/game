import random


def spin_row():
    symbols=['🍕', '🍟','🍔','🧀','🥫']
    return [random.choice(symbols) for symbol in range(3)]
def print_row(row):
    print('***************')
    print('==','-'.join(row),'==')
    print('***************')
def payout(row, bet):
    for symboled in set(row):
        count=row.count(symboled)
        if count==2:
            multiplier={'🍕':1.5, '🍟':2,'🍔':3,'🧀':4,'🥫':5}
            return multiplier[symboled]*bet
        elif count==3:
            multiplier ={'🍕':3,   '🍟':4, '🍔':5, '🧀':6, '🥫':7}
            return bet*multiplier[symboled]
    return 0
balance=100
print('===Welcom to Python slot===')
print('Symbol:🍕 🍟 🍔 🧀 🥫')
print('===========================')
print(f'\033[92mcurrent balance: ${balance}\033[0m')
while balance > 0:
    bet=input('enter your bet: ')
    if not bet.isdigit():
        print('pls enter a numeric value!!!')
        continue
    bet=int(bet)
    if bet>balance:
        print('insufficent funds!!')
        continue
    if bet<=0:
        print('greater than zero amount!!')
        continue
    balance-=bet
    row=spin_row()
    print_row(row)
    get_payout=payout(row,bet)
    balance += get_payout
    if get_payout>0:
        print(f'\033[92mCongratulations!! u win ${get_payout}!\033[0m')
        print(f'\033[92mNew balance: {balance}\033[0m')
    else:
        print(f'\033[93mSorry, u lose ${bet}!\033[0m')
        print(f'\033[92mNew balance: {balance}\033[0m')
    while True:
        a=input('\033[95mY for continue N for quit: \033[0m')
        if a.lower()=='y':
            break
        elif a.lower()=='n':
            break
        else:
            print('\033[91mSorry, try again!\033[0m')
    if a.lower()=='n':
        print('=========================')
        print(f'\033[97mur balance in total is {balance}\033[0m')
        print('=========================')
        break
