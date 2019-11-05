import random

name = input ('please enter your name (or e to end game):')
positive_messages = ['you\'re best','you can do python','make the best of this class',
'you will be a pro']

while name != 'e':
    pos = random.randint(0, len(positive_messages) - 1)
    print(positive_messages[pos])
    name = input ('please enter your name (or e to end game):')
