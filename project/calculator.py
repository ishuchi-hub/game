#calculator
from faulthandler import cancel_dump_traceback_later


def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lower()=='cancel':
            return 'cancel'
        try:
            value = float(value)
            return value
        except ValueError:
            print('ur wrong,pls enter a number')
while True:
    print('\033[93menter "cancel" to stop\033[0m')
    a = get_number('enter number 1:')
    if a=='cancel':
        break
    b = get_number('enter number 2:')
    if b=='cancel':
        break
    player=input('+ - / *:')
    if player=='cancel':
        break
    elif player=='+':
        print('addition=',a+b)
    elif player=='-':
        print('subtraction=',a-b)
    elif player=='*':
        print('mutiplication=',a*b)
    elif player=='/':
        print('division=',a/b)
    else:
        print('pls enter operation')

