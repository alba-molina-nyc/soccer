from dataprep import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date


player_dict, player_stat_dict = {}, {}
players_list, players_stat_list = [], []

def create_player_bio_dict(players):
    for player in players:
        statistics = player.get('statistics')
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
            player_stat_dict = {
            'id': player_id, 
            'name': player_name,
            'total shots': total_shots,
            'shots on goals': on_goals,
            'total goals': total_goals,
            'conceded goals': conceded,
            'assists goals': assists,
            'saved goals': saves,
            'total passes': total_passes,
            'key passes': key,
            'accuracy passes': accuracy,
            'total tackles': total_tackles,
            'blocks': blocks,
            'interceptions': interception,
            'total duels': total_duels,
            'won duels': won_duels,
            'dribble attempts': attempts,
            'dribble success': success,
            'dribble past': past,
            'drawn fouls': drawn,
            'committed fouls': fouls_committed,
            'yellow cards': yellow,
            'red cards': red,
            'won penalties': penalty_won,
            'committed pentalties': penalty_committed,
            'scored penalty': penalty_scored,
            'missed penalty': penalty_missed,
            'penalty saved': penalty_saved,
            'minutes': minutes,
            }
       
        players_stat_list.append(player_stat_dict)

    df, fd = pd.DataFrame(players_list),  pd.DataFrame(players_stat_list)
    df.to_csv('/Users/albamolina/files/soccer/players.csv')
    fd.to_csv('/Users/albamolina/files/soccer/player_stats.csv')

    return player_dict, players_list, df, statistics

create_player_bio_dict(players)

# on_goals, total_goals, conceded, assists, saves