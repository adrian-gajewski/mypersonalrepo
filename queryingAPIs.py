# to install the module run:
# pip install nba_api
import os
from nba_api.stats.static import teams
import pandas as pd
os.system("cls")
# Get all NBA teams
all = teams.teams
all_teams = pd.DataFrame(all)
#Print sample of data
print(all_teams.head(3))

#Print only sorted list of names
names = sorted(all_teams[2])

print(names)
 