#the for loop
#for loop works with an iterable Count,Num
name='keerthi'

for num in range(1,11):

    print(name)

#or 

name = 'keerthi'

for count in range(0,10):
    print(name)

#print the odd numbers between 1 and 10

for oddnumber in range (1,11):
    if oddnumber % 2 ==1:
        print(oddnumber)
      
#print the sum of even numbers 

total=0
#declare the value outside the loop , for example if you declare the value inside the loop you always end with value = 0 
for sumofeven in range (1,100):
    if sumofeven % 2 == 0:
        total = sumofeven + total
        # you can also right it as  total += num 
print(total)

########################################
for sumofeven in range (1,11):
    if sumofeven % 2 == 0:
        total += sumofeven
        # you can also right it as  total += num 
print(total)
##########################################
#store your full name in a variable,loop over your name 
#print the vowels in your name
#if you find a vowel,print it

name='keerthi penumutchu'

for vowel in name: 
#for each letter in my name
    if vowel == 'a' or vowel =='e' or vowel == 'i' or vowel == 'o' or vowel=='u':
        print(vowel)

