import json

with open ('nhl.json','r') as nhl_file:
    data = json.load(nhl_file)

print(data.keys())

#how many teams are in the nhl
#json_filename = 'nhl.json'

total_of_team = len(data['teams'])
print(total_of_team)



#when was the bostonbruins started
for team_name in data.keys:


#what is the oldest teams in NHL

#what are the teams in the eastern conference