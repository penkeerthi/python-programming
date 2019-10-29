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

for float_value in values: 
    if type(float_value) is float: #first find the type of values and determine it is float
        float_list.append(float_value)

print (float_list)

print(type(cohort_4)) #type is a function of print

''' Class is a template for functions and methonds'''