#sets do not allow duplicates 

rainbow_colors = {'Red','Orange','Yellow','Green','Blue','Indigo','Violet'}

print(type(rainbow_colors))

values = [1,5,7,2,5,5,9,7]

unique_values = set(values)

print(unique_values)

#add values to a set
unique_values.add(3)

#remove a value from a set
unique_values.remove(3)

print(unique_values)

# unique_values.remove(3) Traceback (most recent call last):
''' File " <module>unique_values.remove(3)
KeyError: 3 '''  #if you try to remove an item that is not in the set , python will complain


#single line is isogram 

def is_isogram(string):
    return len(set(string)) == len(string)

   # unique = set(string)
   #len(unique) == len(string):
        #return True
    #else:
        #return False '''


#tuples are immutable 
#tuples are ordered 

weekdays = ('Monday','Tuesday','Wed','Thursday','Fri','Sat','Sun')
weekends = ()
print(weekdays[0])
weekends = (0,1)
weekends = (0,2)
    

