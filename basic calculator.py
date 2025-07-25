#calculator
while True:
    a=float(input('enter number1:'))
    b=float(input('enter number2:'))
    choice=input('enter choice +, -, *, /, cancel:')
    if choice=='cancel':
        print('cancel')
        break
    elif choice=='+':
        print('addition:', a+b)
    elif choice=='-':
        print('subtraction:',a-b)
    elif choice=='*':
        print('multiplication:',a*b)
    elif choice=='/':
        print('division:',a/b)
    else:
        print('invalid choice')