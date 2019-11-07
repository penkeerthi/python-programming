#define functions is by def

#parameter vs arguments 

#function is a block, Function followed by parameters but are not needed.

#functions are written to do a specific job and return something, think of functions as helpers.

#when writing a function that returns value use "Return"

#Things go inside function are arguments for example print (arguments)

#when calling function you provide name and arguments

#define function before invoking it

#python is assigns a variable type when running, since python is a loosely typed value
#Value is bound to functions after its called. For example add(num1,num 2) - they are just placeholders

#function to add two integers
def add(num1, num2):
    return num1 + num2

#function to display hello there
def say_hello():
    print('Hello There!')

#function that returns the lenght of a string 
def lenght_of_string(string):
    return len(string)

#function to return the sum of integers in a list
def sum_of_integers(a_list):
    result = 0
    for num in a_list:
        if type(num) is int:
            result += num
    return result

#function to reverse a string


def rev_string(string):
    idx = len(string) -1
    result = ''
    while idx >= 0:
        result += string [idx]
        idx -= 1
    print (result)
    return result

rev_string('keerthi')

#print (rev_string('some random string'))

#reverse string in one line (python)
def one_line_reverse(string):
    return string[::-1]

#daniela solutions using a for loop

def  daniela_reverse (string):
    result = ''
    for character in string:
        result = character + result

    return result


   


''' attempt 1
def my_reverse(words):
    a = 0
    while 0 < len(words):
        a += -1
        print (words[a])
        

my_reverse('keerthi')


add(5,10)

print ((add(5,10)) #pass to print function


result = add(50,20) #assign to a variable

#function takes no arguments 
# 
# '''