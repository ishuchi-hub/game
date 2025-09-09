import random
dice_art={
      1:(
        '┌────────────┐',
        '│            │',
        '│     ●      │',
        '│            │',
        '└────────────┘'
         ),
      2:(
        '┌────────────┐',
        '│   ●        │',
        '│            │',
        '│        ●   │',
        '└────────────┘'
         ),
      3:(
        '┌────────────┐',
        '│     ●      │',
        '│     ●      │',
        '│     ●      │',
        '└────────────┘'
         ),
      4:(
        '┌────────────┐',
        '│   ●    ●   │',
        '│            │',
        '│   ●    ●   │',
        '└────────────┘'
      ),
      5:(
        '┌────────────┐',
        '│  ●      ●  │',
        '│     ●      │',
        '│  ●      ●  │',
        '└────────────┘'
      ),
      6:(
        '┌────────────┐',
        '│    ●   ●   │',
        '│    ●   ●   │',
        '│    ●   ●   │',
        '└────────────┘'
      )
}
dice=[]
total=0
dice_times=int(input('enter number of dices: '))
for i in range(dice_times):
    dice.append(random.randint(1,6))
for i in range(5):
    for line in dice:
        print(dice_art[line][i],end='')
    print()
a=sum(dice)
print(a)