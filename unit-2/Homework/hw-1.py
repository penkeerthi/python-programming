numvar = 0
for evennumber in range (1000,10001):
    if evennumber % 2 == 0:
        numvar += evennumber
        print(numvar)

    print (f'The sum of even numbers between 1000 and 10,000 is:{numvar}')

    #make sure print is outside the for loop so you dont get repeated prints


    #or you can also print 
print('The sum of even numbers is', numvar)