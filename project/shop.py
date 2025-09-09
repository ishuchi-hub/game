#dictionaries={key,value}
menu = {
    'pizza':13,
    'bread':1,
    'coffee':1.5,
    'hamburger':3,
    'french fried':1,
    'sandwich':1,
    'milktea':1.5
}
cart = []
total = 0
print('\033[92m===============MENU================\033[0m')
for food,price in menu.items():
    print(f'{food}: ${price:.2f}')
while True:
    guest = input('select ur food(or q to quit): ')
    if guest == 'q':
        break
    elif guest in menu:
        cart.append(guest)
print('\033[92m================YOUR ORDER=================\033[0m')
for food in cart:
    total=total+menu.get(food)
    print(food,end=' ')
def net_price(price,tax=0.05):
    return price*(1+tax/100)
totalwit_tax=net_price(total)
print()
print(f'\033[92mafter tax, ur total is: ${totalwit_tax:.2f}')
