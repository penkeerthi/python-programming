#While loops is executed  only when a condition is met
#be lookout for infinite loop

import random

val = 1
while val < 10:
    print (val)
    val += 1 #increment val

#guessing game

#all user input is string, All keyboard input is a string

#correct_answer = 7
correct_answer = random.randint(1,10)
guess = int(input('guess my number (1 - 10) '))

while guess != correct_answer:
    guess = int(input('wrong. try again'))

print('You are correct!!')


# how do you break a loop?

names = ['jack','jill','mary','jane','kate']

idx = 0
while idx < len(names):
    if 'mary' == names[idx]:
        print('found mary')
        break
    idx += 1

#How do we loop forever

while True:
    answer = input('Continue y/n')
    if answer == 'n':
        break
