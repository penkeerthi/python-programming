#string is iterable
#strings are immutable

movie_title = 'Thor, the Dark World'

print (movie_title[0])  

# position 0 is T

# movie_title[5] = '-' # not allowed, you cannot changing the values

movie_title = 'The Avengers' # here we are re-assining the variable to something else, different from changing 

start = movie_title[0:3] #using this expression you can declare parts of the string in the variable

print (start) 

print (movie_title [-1]) #gives us the last character 

print (movie_title[:4])

print(movie_title[2:])

