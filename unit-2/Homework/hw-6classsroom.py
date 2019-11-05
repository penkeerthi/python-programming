marvel_movies = ['Ironman','the incredible hulk','Iron Man 2','Thor','Captain America: The first Avenger','The Avengers','Iron Man 3','Thor: The Dark World','Captain America : The Winter soldier',
'Guardians of The galaxy','black panther']
special_marvel_movies = []

for movie in marvel_movies:
    if 'the ' in movie.lower():
        special_marvel_movies.append(movie)

print(special_marvel_movies)

