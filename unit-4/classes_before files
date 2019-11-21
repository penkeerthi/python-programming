#a class us a Template or Blueprint for Object oriented programming
class Person:
    #every class must have an init method
    def __init__(self, name, age):
        #print('person object initialization')
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f'my name is is {self.name} and i am {self.age}')


#how to initantiate a class (create an object)
p = Person('keerthi', 29)

q = Person('Princeston', 35)

print (p.name,p.age)
print (p.age)

#use a class method
p.say_hello()

print(type(p))

#create a rectangle class
#it should have a len and width 
#it should have two methonds, paramenter and area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    
    def parameter(self):
        return (self.length * self.width) * 2
    
    def area(self):
        return self.length * self.width
        

a = Rectangle(2, 5)

print (f'Area is {a.area} parameter is {a.parameter}')
'''
a = Rectangle(10,10)
a.total_area(a.length + 2*a.width)
print(a.total_area)
'''

#create a playlist class
#the playlist has a  name and list of tracks
#eac track is a dictionary with title artists length of track

#write methiod to add a track, to remove a track , to shuffle the playlist

'''
class Playlist:
    def __init__(self, name, tracklists):
        self.name = name
        self.tracklists = tracklists
        my_list = [(self.name),(self.tracklists)]
'''

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
            if self.tracks[idx]['title']:
                break
        self.tracks.pop(idx)
        

        #pass


pl = Playlist('tunes')

pl.add_track('Shape of you ','ed', 1.30)
pl.add_track('Old time road ','Lil Nas', 4.30)

print(pl.tracks)

pl.remove_track('Shape of you')

print(pl.tracks)

