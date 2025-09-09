#word counting
# word counting
from platform import android_ver


def get_word(char):
    while True:
        value = input(char)

        if value.isdigit():
            print('pls enter a character/sentence')
        else:
            return value
while True:
    print('\034[93menter "cancel" to stop')
    i_o=get_word('enter the word that u wanna count:')
    if i_o=='cancel':
        break
    player=get_word('enter your word:')
    if player=='cancel':
        break
    count=0
    for i in player:
        if i==i_o:
            count+=1
    print(f'total of {i_o} is:',count)


