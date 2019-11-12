def add(*args): #page10 of func args // adding any number of values
    #print(len(args))
    total = 0
    for item in args:
        total += item
        
    return total

#add(1,2,3,4,5)

print(add(1,2,3,4,5,6,7,8,9))