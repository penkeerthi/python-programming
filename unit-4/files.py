#how to read a file http://ga-python-course.herokuapp.com/content/unit-5-intermediate/instructor-resources/21-scripting/21-scripting-slides.md.html#/section
my_file = open('lines.txt','r') #mode r is for reading 

data = my_file.read()

my_file.close() #you should close a file after using it 

print(data)

#how do we write to a file

my_file = open('lines.txt', 'w') #w overwrites the contents, if it exists
my_file.write('Adding one line')
my_file.close()

my_file = open('new_file.text','w')
my_file.write('lines for my new file')
my_file.close()

my_file = open('new_file.mov','w')
my_file.write('lines for my new file')
my_file.close()


#to add to the end of file, we append (a)

my_file = open('new_file.text','a')
my_file.write('writing a new line')
my_file.write('\n this is a new line')
my_file.close()

#we can use "with" if we dont want to have to close everytime
with open('lines.txt', 'r') as text_file:
    data = text_file.read()

print(data)