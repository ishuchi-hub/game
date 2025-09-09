questions=[
    'how much if 1+3?',
    'duyhkhanh is good,right?',
    'what can swin?',
    'what can fly?'
]
options=[
    ('A.4','B.2'),
    ('A.YES','B.No'),
    ('A.tiger','B.dolphin'),
    ( 'A.Lion','B.bird')
]
score=0
num=1
answer=('A','A','B','B')
q_num=0
for q in questions:
    print(f'---------question {num}---------')
    print(q)
    for o in options[q_num]:
        print(o,end=' ')
    print()
    guess=input('enter your guess: ')
    if guess.upper()==answer[q_num]:
        score += 1
        print('\033[92mCORRECT!\033[0m')
    else:
        print('\033[91mWRONG!\033[0m')
        print(f'answer is \033[93m{answer[q_num]}\033[0m')
    num += 1
    q_num += 1
print(f'in total u have {score}/{len(questions)}')