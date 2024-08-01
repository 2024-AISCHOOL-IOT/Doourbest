import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def set_paging(row=5,col=5):
    """default value
    row=5
    col=None
    """ 
    pd.set_option('display.max_rows', row)
    pd.set_option('display.max_columns', col)

set_paging()

dataset = "C:/Users/USER/project/git/dataset"
games = pd.read_csv(dataset+"/games.csv")
games_details = pd.read_csv(dataset+"/games_details.csv")

warnings.filterwarnings('default')

games.dropna(subset=['PTS_home'],inplace=True)
games.drop_duplicates(subset=['GAME_ID'],inplace=True)

games_details = games_details[games_details['MIN']!='0']
games_details = games_details[(games_details['TEAM_ID']!=1610612756) | (games_details['GAME_ID']!=10500109)]


# 그룹별로 합계와 평균값 집계
grouped_summary = games_details.groupby(['GAME_ID', 'TEAM_ID']).agg({
    'FGM': 'sum',
    'FGA': 'sum',
    'FG3M': 'sum',
    'FG3A': 'sum',
    'FTM': 'sum',
    'FTA': 'sum',
    'FT_PCT': 'mean',
    'OREB': 'sum',
    'DREB': 'sum',
    'REB': 'sum',
    'AST': 'sum',
    'STL': 'sum',
    'BLK': 'sum',
    'TO': 'sum',
    'PF': 'sum',
    'PTS': 'sum',
    'FG_PCT': 'mean',
    'FG3_PCT': 'mean'
})

grouped_summary=grouped_summary.sort_values(by=['GAME_ID', 'PTS'], ascending=[True, False]).reset_index(drop=False)

tmp_games = games[['GAME_DATE_EST', 'GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'HOME_TEAM_WINS']]
tmp_games_detail = grouped_summary[['GAME_ID', 'TEAM_ID', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS']]

home = {}
away = {}

for i in tmp_games_detail.columns.tolist():
    home[i] = f'{i}_home'
    away[i] = f'{i}_away'
    
home_games_detail = tmp_games_detail.rename(columns=home)
away_games_detail = tmp_games_detail.rename(columns=away)

home_merge_df = games.merge(home_games_detail,how='inner', left_on=['GAME_ID','HOME_TEAM_ID'],right_on=['GAME_ID_home','TEAM_ID_home'],suffixes=('','_detail'))
away_merge_df = games.merge(away_games_detail,how='inner', left_on=['GAME_ID','VISITOR_TEAM_ID'],right_on=['GAME_ID_away','TEAM_ID_away'],suffixes=('','_detail'))

home_merge_df = home_merge_df.drop(columns=[col for col in home_merge_df.columns if 'id_' in col.lower() or '_detail' in col.lower()])
away_merge_df = away_merge_df.drop(columns=[col for col in away_merge_df.columns if 'id_' in col.lower() or '_detail' in col.lower()])

merged_df = pd.concat([home_merge_df,away_merge_df.iloc[:,19:]],axis=1)
merged_df.rename(columns={'HOME_TEAM_ID':'TEAM_ID_home','VISITOR_TEAM_ID':'TEAM_ID_away'},inplace=True)


# 익명 함수를 사용한 정렬
sorted_columns = sorted(
    merged_df.columns.tolist(),
    key=lambda column_name: (
        0, column_name) if column_name in ['GAME_DATE_EST', 'GAME_ID', 'GAME_STATUS_TEXT', 'SEASON'] else (
        1, 0) if column_name == 'TEAM_ID_home' else (
        1, 1, column_name) if 'home' in column_name else (
        2, 0) if column_name == 'TEAM_ID_away' else (
        2, 1, column_name) if 'away' in column_name else (
        3, column_name)
)

merged_df = merged_df.reindex(columns=sorted_columns)

def return_dict():

    return merged_df
