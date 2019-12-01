import requests
import json
from json import JSONEncoder

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

artist1 = {"q":"eminem"}
artist2 = {"q":"ed sheeran"}
artist3 = {"q":"cardi b"}


headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "3d6b4f8a8fmsh5a8a772af4987ecp177529jsn342db06df10d"
    }

'''

response = requests.request("GET", url, headers=headers, params=artist1)
data = response.json()
#print(data.keys())
with open('eminem.json', 'w') as artist_file:
    artist_file.write(json.dumps(data))

response = requests.request("GET", url, headers=headers, params=artist2)
data = response.json()
with open('edsheeran.json', 'w') as artist_file:
    artist_file.write(json.dumps(data))

response = requests.request("GET", url, headers=headers, params=artist3)
data = response.json()
with open('cardib.json', 'w') as artist_file:
    artist_file.write(json.dumps(data))

'''

    
#a. How many tracks are listed?    
with open('eminem.json', 'r') as artist_file:
    data = json.load(artist_file)
    #print(data.keys())
    tracks = data['data']
total_count = 0
for track in tracks:
    if track['type'] == 'track':
        total_count += 1

print (f'Total number of songs by eminem is only {total_count}')

with open('edsheeran.json', 'r') as artist_file:
    data = json.load(artist_file)
    #print(data.keys())
    tracks = data['data']
total_count = 0
total_albums = 0
for track in tracks:
    if track['type'] == 'track':
        total_count += 1
for album in tracks:
    if album['type'] == 'album':
        total_albums += 1


print (f'Total number of songs by edsheeran is only {total_count}')
print (f'Total number of albums by edsheeran is only {total_albums}')
with open('cardib.json', 'r') as artist_file:
    data = json.load(artist_file)
    #print(data.keys())
    tracks = data['data']
total_count = 0
for track in tracks:
    if track['type'] == 'track':
        total_count += 1

print (f'Total number of songs by cardib is only {total_count}')


'''
1. Make separate API calls to retrieve data for the artists Eminem, Ed Sheeran, and Cardi B
2. Write the data for each artist to a separate json file (so you should have eminem.json, ed_sheeran.json, cardi_b.json files)
3. For each of the artists:
a. How many tracks are listed?
b. How many albums are listed?
c. Count the number of tracks with explicit lyrics d. Which year was the most recent album for each?
4. When was the release date for Eminem’s album titled “The Eminem Show”?
5. How many tracks are on Ed Sheeran’s album “Shape of You”?
6. Which artist(s) collaborated with Cardi B on the track titled “Cardi B”?
7. Build a playlist of 10 songs from these 3 artists. Take songs randomly from
each artist until you have 10. For each track store the artists name along with the following data: id readable title title_short title_version link duration rank explicit_lyrics explicit_content_lyrics
8. Save your playlist to a flie called random_playlist.json
'''