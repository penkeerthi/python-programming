import json

with open('nhl.json', 'r') as nhl_file:
    data = json.load(nhl_file)


team_list = data['teams']

#how may teams are in the nhl
no_of_teams = len(team_list)
print('Number of teams in NHL {}'.format(no_of_teams))

eastern_conf_teams = []
oldest_year = '2019'
oldest_name = ''
for team in team_list:
    #when was the boston bruins started
    if team['name'] == 'Boston Bruins':
        print('Boston Bruins started in {}'.format(team['firstYearOfPlay']))

    #what are the teams in the eastern conference
    if team['conference']['name'] == 'Eastern':
        eastern_conf_teams.append(team['name'])


    #what is the oldest team in the nhl
    #(there are several ways to do this)
    #we could grab the firstYearOfPlay along with the name of 
    # each team and put in a list, sort this list, grab
    #the first item in the sorted list
    if team['firstYearOfPlay'] < oldest_year:
        oldest_year = team['firstYearOfPlay']
        oldest_name = team['name']

print('Eastern conference teams: ', end= ' ')
print(eastern_conf_teams)

print('Oldest team is {}, started in {}'.format(oldest_name, oldest_year))
