#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd

def schedule(url_adress):

    url = url_adress
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Referer": "https://stats.nba.com",
        "Origin": "https://stats.nba.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # 모든 게임 데이터를 리스트에 추가
    all_games = []
    for game_date in data['leagueSchedule']['gameDates']:
        all_games.extend(game_date['games'])

    # 데이터프레임으로 변환
    schedule_df = pd.DataFrame(all_games)

    # 'homeTeam' 딕셔너리에서 'teamName' 값을 추출하여 'homeTeam' 열 업데이트
    schedule_df['homeTeam'] = schedule_df['homeTeam'].apply(lambda x: x['teamName'] if isinstance(x, dict) and 'teamName' in x else None)

    # 'awayTeam' 딕셔너리에서 'teamName' 값을 추출하여 'awayTeam' 열 업데이트
    schedule_df['awayTeam'] = schedule_df['awayTeam'].apply(lambda x: x['teamName'] if isinstance(x, dict) and 'teamName' in x else None)

    # 'pointsLeaders' 딕셔너리에서 'firstName' 값을 추출하여 'pointsLeaders' 열 업데이트
    schedule_df['pointsLeaders'] = schedule_df['pointsLeaders'].apply(lambda x: x['firstName'] if isinstance(x, dict) and 'firstName' in x else None)

    # 'broadcasters' 열 제거
    schedule_df['date'] = schedule_df['gameCode'].str[6:8]
    result = schedule_df[['gameLabel','monthNum','date','day','arenaCity','arenaName','homeTeam','awayTeam']]
    # 결과 출력
    return result

