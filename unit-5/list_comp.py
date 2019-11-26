#list comprehension can be used to crate a new list from an existing one

nums = [1,3,6,8,9,11,15,18]

#create a new list from an only the even numbers
even_nums= []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print (even_nums)
#using list comprehension
new_even_nums = [num for num in nums if num % 2 == 0] #this construct is called list comprehension
print (new_even_nums)

#a list with the square of the even numbers
even_square = [val * val for val in nums if val % 2 == 0 ]
print (even_square)

#crete a list of the titles with 't' in their names
titles = ['Lord of The rings','The time Machine','The great gatsby','Moby Dick','Chronicles of Narnia']

new_titles = [newvals for newvals in titles if 'T' or 't' in newvals ]
print(new_titles)

#convert a string to upperscase
string = ' this is the sample string'
#create a list of the characters - upper case
capital = [char.upper() for char in string]
print(capital)

#convert list to string 
capital = ''.join([char.upper() for char in string])
print(capital)

#if/else goes before the for 
#if number is < 10, add ten, else subtract ten

vals = [15,12,3,8,-1,7,11,25,0,10]

ten_list = [val + 10  if val < 10 else val -10 for val in vals ]
print(ten_list)

#dictionaries comprehension
person = {'Name': 'alice','Job':'Engineer','City':'Toronto'}

#create a new dictionary that has the first initial if both key and value

new_person = { key[0]:value[0] for key,value in person.items() }
print(new_person)


#abstractions and modules
