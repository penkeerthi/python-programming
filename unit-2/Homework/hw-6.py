marvel_movies = ['Ironman','The incredible hulk','Iron Man 2','Thor','Captain America: The first Avenger','The Avengers','Iron Man 3','Thor: The Dark World','Captain America : The Winter soldier','Guardians of The galaxy']
special_marvel_movies = []

for special in marvel_movies:
    if 'The' in special: #use in instead of == as you are looking for values in the movies list
        special_marvel_movies.append(special)
    print (special_marvel_movies)


#attempt 1
'''
idx = 0

while idx < len(marvel_movies):
    if 'the' == marvel_movies[idx]:
        special_marvel_movies += marvel_movies
        break
    idx += 1

print (special_marvel_movies)
'''