#create a class
class Person:
    #every class must have an init method
    def __init__(self, name, age):
        #print('person object initialized')
        self.name = name
        self.age = age
    
    def say_hello(self):
        print('Hello my name is {} and I am {} years old'.format(self.name, self.age))
​
​
​
​
​
#how to instantiate a class (create an object)
p = Person("John", 35)
​
q = Person("Jane", 28) 
​
print(p.name)
​
print(q.name)
​
#use a class method
p.say_hello()
​
​
print(type(p))
​
​
#create a rectangle class
#it should have a length and a width
#it should have two methods, perimeter and area
​
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def perimeter(self):
        return (self.length + self.width) * 2
​
    def area(self):
        return self.length * self.width
​
r = Rectangle(10, 5)
​
#print('Area is {}, perimeter is {}'.format(r.area(), r.perimeter()))
​
​
#create a playlist class
#the playlist has a name and a list of tracks
#each track is a dictionary, with title, artiste, length of track
​
#write methods to add a track, to remove a track, to shuffle the playlist
​
class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []
    
    def add_track(self, title, artist, length):
        track = {}
        track['title'] = title
        track['artist'] = artist
        track['length'] = length
        self.tracks.append(track)
    
    def remove_track(self, title):
        for idx in range(len(self.tracks)):
            if title == self.tracks[idx]['title']:
                break
        self.tracks.pop(idx)
    
​
​
pl = Playlist('tunes')
​
pl.add_track('Shape of You', 'Ed Sheeran', 3.45)
pl.add_track('Mamacita', 'Tyga, Santanta, YG', 4.15)
​
print(pl.tracks)
​
​
pl.remove_track('Shape of You')
​
print(pl.tracks)