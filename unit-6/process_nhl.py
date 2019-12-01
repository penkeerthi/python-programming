import json

with open ('nhl.json','r') as nhl_file:
    data = json.load(nhl_file)

print(data.keys())

#how many teams are in the nhl
#json_filename = 'nhl.json'

total_of_team = len(data['teams'])
print(total_of_team)



#when was the bostonbruins started
for team_name in data['teams']:
    if team_name['name'] == 'Boston Bruins':
        print(team_name['firstYearOfPlay'])
'''
#what is the oldest teams in NHL
for oldest_team in data['teams']:
    min(data['firstYearOfPlay'])
print(oldest_team['name'])
 '''   


#what are the teams in the eastern conference


#what is the oldest teams in NHL
first_year_of_play = []
for oldest_team in data['teams']:
    #if oldest_team != '':
    first_year_of_play.append(oldest_team['firstYearOfPlay'])
        
print(first_year_of_play)

