#rock,paper and scissors
while True:
    from random import choice
    player=input('rock,paper and scissors(or "cancel" to stop):')
    if player =='cancel':
        print('game cancelled')
        break
    if player not in ['rock','paper','scissors']:
        print('invalid value, pls give another choice')
    else:
        computer=choice(['rock','paper','scissors'])
        print('player choice:',player)
        print('computer choice:',computer)
        if player==computer:
                print('tie')
        elif player=='rock':
                if computer=='paper':
                        print('you lose')
                else:
                        print('you win')
        elif player=='paper':
                if computer=='rock':
                        print('you win')
                else:
                        print('you lose')
        elif player=='scissors':
                if computer=='rock':
                        print('you lose')
                else:
                        print('you win')