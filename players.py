from dataprep import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date

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
