#for all numbers from 1 to 50 
#if its a multiple of 3, print "fizz"
#if its a multiple of 5, print "buzz"

#if its a multiple of 15, print 'fizzbuzz'
#otherwise print the number
''' 1 // 1 # if result is 1 , result is going to be 1 
2 // 2 # if result is 2 , result is going to be 2 
3 // 'fizz' # if result is a multiple of 3, return 3
4 // 4 
5 // 'buzz' 
6 // 'fizz' 
'''

for num in range (1,51): #range is going to end one number before the number
    if num % 15 == 0:
        print(f'{num} is Fizzbuzz')
        #print('Fizzbuzz').Checking is number divided by 15, returns true. so for example 15/15 = 0, returns Fizzbuzz
    elif num % 5 == 0:
        print(f'{num} is Buzz')
        #print('Buzz')
    elif num % 3 == 0:
        print(f'{num} is Fizz')
        #print('Fizz')
    else:
        print(num)


