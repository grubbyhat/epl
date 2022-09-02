import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
from matplotlib import pyplot as plt
import time

tracker = 'https://www.skysports.com/premier-league-table/2021'
response = requests.get(tracker)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all("table")
dfs=pd.read_html(str(table))
df = dfs[0]

for i in range(len(df['Team'])):
    print(df.at[i,'W'], df.at[i,'GD'])
    if df.at[i,'GD'] == 0: 
        df.at[i, 'gpg'] = 0
        continue
        
    else:
        PGD = int(df.at[i,'F'])/(int(df.at[i,'L'])+int(df.at[i,'D'])+int(df.at[i,'W']))
        df.at[i,'gpg']=PGD

class Create_Team:
    def __init__(self, team_choice):
        self.team_url = f'https://www.skysports.com/{team_choice}-squad'
        self.response_team = requests.get(self.team_url)
        self.soup_team = BeautifulSoup(self.response_team.text, 'html.parser')
        self.squad_team = self.soup_team.find_all('table')
        
        self.dfs=pd.read_html(str(self.squad_team))
        self.goalkeepers, self.defenders, self.midfielders, self.striker = self.dfs
        
        
        self.formation = self.soup_team.find_all('dic', {'style'==' '})

for team in df['Team']:
    team_clean = team.replace(' ','-')
    print(team_clean)
    abrv = f'{team_clean[:4]}_{team_clean[-2:]}'
    print(abrv)
    locals()[abrv] = Create_Team(team_clean)

