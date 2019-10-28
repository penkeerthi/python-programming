total = 10 #assignment, assigment value of 15

#condition + action

if total == 15: #block statement ends with : 
    print('good')
else:
    print('bad')

# to return even or odd

if  total % 2 == 0:
    print('even')
else:
    print('odd')

#modulus operator with odd number

if total % 3 ==0:
    print('odd')
else:
    print("even")


#lenght operator 
first_name='keerthi'

if  len (first_name) > 7:
    print('this is a nice size')
else:
    print("this is not a nice size")

#comparision operators 
# ==
# > 
# <
# >=
# <= 
# !=


#print correspending letter for a grade 
# if score is 80 - 100 , print a 
# if score is 60 - 79 , print b\
# if score is 50 - 69 , print c
# other wise, print f

score = 19 

if score >= 80 <= 100:
    print('Grade A')
elif score >= 60 <= 79:
    print('Grade B')
elif score >= 50 <= 60:
    print ('Grade C')
else:
    print("F")


score = 50 

if score >= 80 :
    print('Grade A')
elif score >= 60 :
    print('Grade B')
elif score >= 50 :
    print ('Grade C')
else:
    print("F")

#Truthy #use truthy to check user input
if "hello world":
    print('yes, its true')

#Falsy 
if "":
    print('no, it is false')
else:
    print('no its false')

#any number that is not zero is truthy
if 13:
    print('it is true')

#0 is falsey
if 0:
    print('it is true')
else:
    print('it is false')


a=-10
b=-11

#or 
if a>0 or b <0:
    print('good!')

#and
if a>0 and b<0:
    print('excellent')