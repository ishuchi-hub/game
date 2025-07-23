# game:rock paper scissor
```python
from random import randint
player = input('rock,scissor,paper:')
computer = randint(0, 2)
if computer == 0:
  computer = 'rock'
if computer == 1:
  computer = 'scissor'
if computer == 2:
  computer = 'paper'
print('player choose:', player)
print('computer choose:', computer)
if player == computer:
  print('draw')
else:
  if player == 'rock':
    if computer == 'scissor':
      print('player wins')
    else:
      print('player lose')
  if player == 'scissor':
    if computer == 'paper':
      print('player wins')
    else:
      print('player lose')
  if player == 'paper':
    if computer == 'rock':
      print('player wins')
    else:
      print('player lose')
  else:
    print('wrong invalid!')
      ```python
