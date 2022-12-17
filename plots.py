from dataprep import *
from players import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date

dataset = []
for player in players: 
    for item in player.items():
        dataset.append({})
        
df = pd.DataFrame(dataset)

df.plot(kind='bar', x='player name', y='total-players')

plt.show()


