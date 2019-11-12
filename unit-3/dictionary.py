#a dictionary is a collection of a key/value pair

student = {'name': 'keerthi', 'age': 30,'address': 'Scarborough'}

#how to access elements in a dictionary 
print(student['name'])
print(student['age'])
print(student['address'])


#dictionary name [value] = always gives value 
#dictionarycannot have duplicate keys

#add items to a dictionary

car = {} #creates an empty dictionary 

car['make'] = 'Toyota'
car['model'] = 'Prius'
car['year'] = 2020
car['color'] = 'silver'

print(car)

car['year'] = 2021

print(car)

#how do we iterate over a dictionary
for item in car:
    print(car[item]) #prints the values

#make a list of dictionaries - cars

cars = [{'make': 'Toyota', 'model': 'Prius', 'year': 2019, 'color': 'silver'},
{'make': 'Toyota', 'model': 'Corolla', 'year': 2018, 'color': 'blue'},
{'make': 'Honda', 'model': 'Accord', 'year': 2003, 'color': 'black'},
{'make': 'Ford', 'model': 'F-150', 'year': 2016, 'color': 'red'},
{'make': 'Peugeot', 'model': '306', 'year': 2005, 'color': 'beige'}]

#how do we process a list of dictionaries 

count = 0
for car in cars:
    #count how many toyotas are there
    
    if car['make'] == 'Toyota':
        count += 1
    print(count)


#return the frequency of each letter in the string
frequency_counter(string)

frequency_counter('a tasty line of text')'
'a' : 1
' ' : 4
't' : 3
'e' : 2
's' : 1


#use a dictionary 
'''

car['make'] = 'Toyota'
car['model'] = 'Prius'
car['year'] = 2020
car['color'] = 'silver'
car['make'] = 'Honda'
car['model'] = 'Prius'
car['year'] = 2020
car['color'] = 'silver'
car['make'] = 'Tesla'
car['model'] = 'Prius'
car['year'] = 2020
car['color'] = 'silver'
car['make'] = 'Benz'
car['model'] = 'Prius'
car['year'] = 2020
car['color'] = 'silver'
car['make'] = 'Subaru'
car['model'] = 'Prius'
car['year'] = 2020
car['color'] = 'silver'

for model in car:
    print(car[model])
'''