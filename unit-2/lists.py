#doing a loop within a loop - nested loop

cohort_4 = ['Daniela','Emma','Julian','Keerthi','Kyle','Christina','Connor','Meaghan','Sahil','Shilaj','Allaina']

print(len(cohort_4))

#access items in list using position (index)

print(cohort_4[0]) #print first item in list

print(cohort_4)

#add items to the list , you can use append 
#methods are given by adding .methodname()
#print,len,type - functions 

cohort_4.append('Princeston') 

print(cohort_4)

#remove from a list, Remove will remove first found value, python will not remove duplicates, python will complain if value is 
#not presented (you will get value error)

cohort_4.remove('Julian')
print(cohort_4)

"'Create a new number only with the floats'"
values = [2, 3, 45, 11, -5, 3.5, 7.5, 11.7, 40, 85.6, 77.1]
float_list = []

for value in values: 
    if type(value) is float: #first find the type of values and determine it is float
        float_list.append(value)

print (float_list)

print(type(cohort_4)) #type is a function of print

''' Class is a template for functions and methonds'''


'''Find the average of each list, store in a new list'''

weights = [[50,25,75],[95.7,38.3, 55.2],[88,45,16]]

'''for item in weights:
    print(item)''' #runs only in the first list
averages = []
#list_total = 0 adding list total here will assign 

for item in weights:
    list_total = 0
    for value in item:
        list_total += value
    averages.append(list_total/len(item))

print(averages)

'''
Print stars in the order
*
**
***
****
*****
******
*******
********
*********
'''

for row in range (1,11):
    #for col in range (1,11): - will  print 10*10
    for col in range(1, row + 1):
        print('*', end=' ')
    print('this allows for a new line')

for i in range(11):
    print('* ' * (i + 1))


#using indexes to access list items
# we need to use index to edit the elements/items on the lists
# use index if we need to edit items/elements in list 

readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0

print(readings)

'''
you cant use for in as you are not changing values
my = ['a','b','c']

for l in my:
    l = '-'
'''

#find the position of an item in a list
current_age = 25
ages = [15,17,27,35,12,25,55,40,31,20]

for idx in range(len(ages)):
#for idx in range(1,8):
    if ages[idx] == current_age:
      print ('25 is found at position', idx)