import json

person = {'Name': 'Alice', 'Job': 'English', 'City': 'Toronto'}

print(type(person))


#properly formatted json 
#keys and all strings enclosed in double quotations
#enclosed with curly braces, square brackets can be used

with open('/Users/penkeerthi/python-programming/unit-4/cohort_4.json', 'r') as cohort_file:
    cohort = json.load(cohort_file) #converts json file to python dictionary 

print(type(cohort))
print(json.dumps(cohort, indent =2)) # indent only on print