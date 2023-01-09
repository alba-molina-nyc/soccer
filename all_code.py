# Make the imports
import pandas as pd
import json

# Open the players.json file, we will sample the data gathered from football API that was saved in the players.json file
with open("players.json", "r") as read_file:
    data = json.load(read_file)

# because the data is in json and therefore dictionaries and I will be needing the different data points below we clean up and set up the data so we can work with it
groups = data['response']

for group in groups:
    team = group.get('team')
    team_id = team.get('id')
    team_name = team.get('name')
    team_logo = team.get('logo')
    players = group.get('players')


for player in players:
    statistics = player.get('statistics')
    i_player = player.get('player')
    player_id = i_player.get('id')
    player_name = i_player.get('name')
    photo = i_player.get('photo')

for statistic in statistics:
    games = statistic.get('games')
    offsides = statistic.get('offsides')
    shots = statistic.get('shots')
    total_shots = shots.get('total')
    on_goals = shots.get('on')
    goals = statistic.get('goals')
    total_goals = goals.get('total')
    conceded = goals.get('conceded')
    assists = goals.get('assists')
    saves = goals.get('saves')
    passes = statistic.get('passes')
    total_passes = passes.get('total')
    key = passes.get('key')
    accuracy = passes.get('accuracy')
    tackles = statistic.get('tackles')
    total_tackles = tackles.get('total')
    blocks = tackles.get('blocks')
    interception = tackles.get('interceptions')
    duels = statistic.get('duels')
    total_duels = duels.get('total')
    won_duels = duels.get('won')
    dribbles = statistic.get('dribbles')
    attempts = dribbles.get('attempts')
    success = dribbles.get('success')
    past = dribbles.get('past')
    fouls = statistic.get('fouls')
    drawn = fouls.get('drawn')
    fouls_committed = fouls.get('committed')
    cards = statistic.get('cards')
    yellow = cards.get('yellow')
    red = cards.get('red')
    penalty = statistic.get('penalty')
    penalty_won = penalty.get('won')
    penalty_committed = penalty.get('committed')
    penalty_scored = penalty.get('scored')
    penalty_missed = penalty.get('missed')
    penalty_saved = penalty.get('saved')
    minutes = games.get('minutes')


# 

player_list = []

for player in players:
    player_list.append(player)

#

player_dict = {}
players_list = []

def create_player_bio_dict(players):
    for player in players:
        i_player = player.get('player')
        player_id = i_player.get('id')
        player_name = i_player.get('name')
        photo = i_player.get('photo')
        player_dict = {
            'id': player_id, 
            'name': player_name,
            'photo': photo,
            }
        players_list.append(player_dict)

    df = pd.DataFrame(players_list)
    df.to_csv('/Users/albamolina/files/soccer/players.csv')

    return player_dict, players_list, df

create_player_bio_dict(players)
