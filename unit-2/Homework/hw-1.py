numvar = 0
for evennumber in range (1000,10001):
    if evennumber % 2 == 0:
        numvar += evennumber
        print(numvar)

    print (f'The sum of even numbers between 1000 and 10,000 is:{numvar}')