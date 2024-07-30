#!/usr/bin/env python
# coding: utf-8

# In[101]:


import numpy as np
import pandas as pd
import requests
pd.set_option('display.max_columns', None)


# In[103]:


import requests

# 플레이 오프 시즌, 선수들 랭킹
def player_rank():
    url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Playoffs&StatCategory=PTS"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Referer": "https://stats.nba.com",
        "Origin": "https://stats.nba.com"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    data_df = pd.DataFrame(data['resultSet']['rowSet'], columns = data['resultSet']['headers'])
    
    return data_df


# In[105]:


player_rank()


# In[107]:

def sort(column):
    data_df.sort_values(by='column', ascending=False)
    return data_df

