from flask import Flask, render_template, request, jsonify
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import pytz
import random
import requests
import NBA_Player_RANK as npr
import NBA_Team_RANK as ntr
import NBA_Schedule_Data as nsd
from datetime import datetime
import prediction_model_from_paper as ppm
import needed_data as nd
from user_lib import predict

app = Flask(__name__)

# 학습모델호출
knn_paper_model = ppm.knn_control_model_training()
tree_paper_model = ppm.tree_control_model_training()
rf_paper_model = ppm.rf_control_model_training()

# 전체 팀 이름

teams = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]
        
team_scores = {'Magic' : nd.magic(), 'Cavaliers' : nd.cavaliers(), 'Timberwolves' : nd.timberwolves()
               , 'Pelicans' : nd.pelicans(), 'Grizzlies' : nd.grizzlies(), 'Kings' : nd.kings(), 'Lakers' : nd.lakers()
               , 'Rockets' : nd.rockets(), 'Pacers' : nd.pacers(), 'Nets' : nd.nets(), 'Wizards' : nd.wizards()
               , 'Hawks' : nd.hawks(), 'Clippers' : nd.clippers(), 'Nuggets' : nd.nuggets()}

korea_tz = pytz.timezone('Asia/Seoul')

scheduler = BackgroundScheduler(timezone=korea_tz)
# scheduler.add_job(update_team_ranking, 'cron', hour=18)
# scheduler.add_job(update_results, 'cron', hour=18)
scheduler.start()

@app.route('/teams', methods=['GET']) 
def get_teams():  
    return jsonify(teams)  

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction/real_time', methods=['GET'])
def real_time():
    return render_template('real_time.html')

@app.route('/api/prediction/real_time', methods=['GET'])
def get_real_time():
    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')
    home_q1,home_q2,home_q3,home_q4, PTS_home = team_scores[home_team]
    away_q1,away_q2,away_q3,away_q4, PTS_away = team_scores[away_team]
    now = datetime.now()
    seconds = now.second
    quater = (seconds % 4) + 1
    if quater == 1:
        df_home1 = home_q1.loc[home_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home1.reset_index(drop=True,inplace=True)
        df_away1 = away_q1.loc[away_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away1.reset_index(drop=True,inplace=True)
        result_home = df_home1
        result_away = df_away1
    elif quater == 2:
        df_home1 = home_q1.loc[home_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home1.reset_index(drop=True,inplace=True)
        df_away1 = away_q1.loc[away_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away1.reset_index(drop=True,inplace=True)

        df_home2 = home_q2.loc[home_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home2.reset_index(drop=True,inplace=True)
        df_away2 = away_q2.loc[away_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away2.reset_index(drop=True,inplace=True)

        result_home = df_home1 + df_home2
        result_away = df_away1 + df_away2
    elif quater == 3:
        df_home1 = home_q1.loc[home_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home1.reset_index(drop=True,inplace=True)
        df_away1 = away_q1.loc[away_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away1.reset_index(drop=True,inplace=True)

        df_home2 = home_q2.loc[home_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home2.reset_index(drop=True,inplace=True)
        df_away2 = away_q2.loc[away_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away2.reset_index(drop=True,inplace=True)

        df_home3 = home_q3.loc[home_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home3.reset_index(drop=True,inplace=True)
        df_away3 = away_q3.loc[away_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away3.reset_index(drop=True,inplace=True)

        result_home = df_home1 + df_home2 + df_home3
        result_away = df_away1 + df_away2 + df_away3
    elif quater == 4:
        df_home1 = home_q1.loc[home_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home1.reset_index(drop=True,inplace=True)
        df_away1 = away_q1.loc[away_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away1.reset_index(drop=True,inplace=True)

        df_home2 = home_q2.loc[home_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home2.reset_index(drop=True,inplace=True)
        df_away2 = away_q2.loc[away_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away2.reset_index(drop=True,inplace=True)

        df_home3 = home_q3.loc[home_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home3.reset_index(drop=True,inplace=True)
        df_away3 = away_q3.loc[away_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away3.reset_index(drop=True,inplace=True)

        df_home4 = home_q4.loc[home_q4['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_home4.reset_index(drop=True,inplace=True)
        df_away4 = away_q4.loc[away_q4['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
        df_away4.reset_index(drop=True,inplace=True)

        result_home = df_home1 + df_home2 + df_home3 + df_home4
        result_away = df_away1 + df_away2 + df_away3 + df_away4

    result_home[result_home['FGA']==0]['FGA']=1
    result_home[result_home['3PA']==0]['3PA']=1
    result_home[result_home['FTA']==0]['FTA']=1
    result_away[result_away['FGA']==0]['FGA']=1
    result_away[result_away['3PA']==0]['3PA']=1
    result_away[result_away['FTA']==0]['FTA']=1

    result_home['FG%'] = round(result_home['FGM'] / result_home['FGA'], 3)
    result_home['3P%'] = round(result_home['3PM'] / result_home['3PA'], 3)
    result_home['FT%'] = round(result_home['FTM'] / result_home['FTA'], 3)
    result_away['FG%'] = round(result_away['FGM'] / result_away['FGA'], 3)
    result_away['3P%'] = round(result_away['3PM'] / result_away['3PA'], 3)
    result_away['FT%'] = round(result_away['FTM'] / result_away['FTA'], 3)
    
    result_home = result_home[['FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    result_away = result_away[['FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    
    result_home_quater = result_home.copy()
    result_home_quater['FG%'] = result_home_quater['FG%'] * (1.00 + (4-quater)/100)

    result_diff = result_home_quater.subtract(result_away.values)[['BLK','DREB','3P%','FG%','FT%','STL','TO']]
    result_diff.columns = ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']

    model1 = predict.pre_knn(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    model2 = predict.pre_tree(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    model3 = predict.pre_rf(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    model4 = ppm.knn_control_model_prediction(knn_paper_model,result_home_quater['FG%'],result_away['FG%'],result_home_quater['FT%'],result_away['FT%'])
    model5 = ppm.tree_control_model_prediction(tree_paper_model,result_home_quater['FG%'],result_away['FG%'],result_home_quater['FT%'],result_away['FT%'])
    model6 = ppm.rf_control_model_prediction(rf_paper_model,result_home_quater['FG%'],result_away['FG%'],result_home_quater['FT%'],result_away['FT%'])
    # 결과 데이터
    data = {
        'columns': result_home.columns.tolist(),
        'result_home' : result_home.to_dict(orient='records'),
        'result_away': result_away.to_dict(orient='records'),
        'model1':str(model1),
        'model2':str(model2),
        'model3':str(model3),
        'model4':str(model4),
        'model5':str(model5),
        'model6':str(model6)
    }
    return jsonify(data)

@app.route('/prediction/future_games', methods = ['GET'])
def future_games():
    return render_template('future_games.html')

@app.route('/api/predict', methods=['GET'])
def future_game_predict():
    home_team = request.args.get('home_team').split(" ")[1]
    away_team = request.args.get('away_team').split(" ")[1]
    model = request.args.get('model')

    home_q1,home_q2,home_q3,home_q4, home_score = team_scores[home_team]
    away_q1,away_q2,away_q3,away_q4, away_score = team_scores[away_team]
    
    df_home1 = home_q1.loc[home_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home1.reset_index(drop=True,inplace=True)
    df_away1 = away_q1.loc[away_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away1.reset_index(drop=True,inplace=True)

    df_home2 = home_q2.loc[home_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home2.reset_index(drop=True,inplace=True)
    df_away2 = away_q2.loc[away_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away2.reset_index(drop=True,inplace=True)

    df_home3 = home_q3.loc[home_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home3.reset_index(drop=True,inplace=True)
    df_away3 = away_q3.loc[away_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away3.reset_index(drop=True,inplace=True)

    df_home4 = home_q4.loc[home_q4['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home4.reset_index(drop=True,inplace=True)
    df_away4 = away_q4.loc[away_q4['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away4.reset_index(drop=True,inplace=True)

    result_home = df_home1 + df_home2 + df_home3 + df_home4
    result_away = df_away1 + df_away2 + df_away3 + df_away4

    result_home[result_home['FGA']==0]['FGA']=1
    result_home[result_home['3PA']==0]['3PA']=1
    result_home[result_home['FTA']==0]['FTA']=1
    result_home['FG%'] = round(result_home['FGM'] / result_home['FGA'], 3)
    result_home['3P%'] = round(result_home['3PM'] / result_home['3PA'], 3)
    result_home['FT%'] = round(result_home['FTM'] / result_home['FTA'], 3)

    result_away[result_away['FGA']==0]['FGA']=1
    result_away[result_away['3PA']==0]['3PA']=1
    result_away[result_away['FTA']==0]['FTA']=1
    result_away['FG%'] = round(result_away['FGM'] / result_away['FGA'], 3)
    result_away['3P%'] = round(result_away['3PM'] / result_away['3PA'], 3)
    result_away['FT%'] = round(result_away['FTM'] / result_away['FTA'], 3)

    result_diff = result_home.subtract(result_away.values)[['BLK','DREB','3P%','FG%','FT%','STL','TO']]
    result_diff.columns = ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']

    if model == "model1":
        pre = predict.pre_knn(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    elif model == "model2":
        pre = predict.pre_tree(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    elif model == "model3":
        pre = predict.pre_rf(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    elif model == "model4":
        pre = ppm.knn_control_model_prediction(knn_paper_model,result_home['FG%'],result_away['FG%'],result_home['FT%'],result_away['FT%'])
    elif model == "model5":
        pre = ppm.tree_control_model_prediction(tree_paper_model,result_home['FG%'],result_away['FG%'],result_home['FT%'],result_away['FT%'])
    elif model == "model6":
        pre = ppm.rf_control_model_prediction(rf_paper_model,result_home['FG%'],result_away['FG%'],result_home['FT%'],result_away['FT%'])
    result = {'result': home_team if pre else away_team}
    return jsonify(result)

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/information/game_schedule')
def game_schedule():
    return render_template('game_schedule.html')

@app.route('/information/team_ranking')
def team_ranking():
    return render_template('team_ranking.html')

@app.route('/api/team_ranking', methods=['GET'])
def get_team_ranking():
    team_ranking = ntr.team_rank().drop(columns=['TEAM_ID'])
    team_ranking = team_ranking.sort_values(by='W_PCT', ascending=False)
    team_ranking['RANK'] = [i for i in range(1,len(team_ranking)+1)]
    team_ranking = team_ranking[['RANK','TEAM_NAME','GP','W','L','W_PCT','MIN',
                      'FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM',
                      'FTA','FT_PCT','OREB','DREB','REB','AST','TOV','STL',
                      'BLK','BLKA','PF','PFD','PTS','PLUS_MINUS']]
    data = {
        'columns': team_ranking.columns.tolist(),
        'data': team_ranking.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/api/team_ranking/sort', methods=['GET'])
def sort_team_ranking():
    sort_column = request.args.get('column')
    
    # 유효한 컬럼명인지 확인
    valid_columns = ['GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 
                     'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 
                     'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
    if sort_column not in valid_columns:
        return jsonify({'error': 'Invalid column name'}), 400
    
    team_ranking = ntr.team_rank().drop(columns=['TEAM_ID'])
    team_ranking = team_ranking.sort_values(by='W_PCT', ascending=False)
    
    # 데이터프레임을 정렬
    sorted_df = team_ranking.sort_values(by=sort_column, ascending=False)
    
    # RANK 열 추가
    sorted_df['RANK'] = range(1, len(sorted_df) + 1)
    sorted_df = sorted_df[['RANK', 'TEAM_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 
                           'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 
                           'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 
                           'PFD', 'PTS', 'PLUS_MINUS']]
    
    data = {
        'columns': sorted_df.columns.tolist(),
        'data': sorted_df.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/information/player_ranking')
def player_ranking():
    return render_template('player_ranking.html')

@app.route('/api/player_ranking', methods=['GET'])
def get_player_ranking():
    player_ranking = npr.player_rank()
    new_player_ranking = player_ranking.drop(columns=['PLAYER_ID', 'TEAM_ID'])
    data = {
        'columns': new_player_ranking.columns.tolist(),
        'data': new_player_ranking.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/api/player_ranking/sort', methods=['GET'])
def sort_player_ranking():
    sort_column = request.args.get('column')
    
    # 유효한 컬럼명인지 확인
    if sort_column not in ['GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 
                           'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 
                           'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF']:
        return jsonify({'error': 'Invalid column name'}), 400
    
    player_ranking = npr.player_rank()
    # RANK를 제외한 데이터프레임을 사용하여 정렬
    df_to_sort = player_ranking.drop(columns=['RANK','PLAYER_ID','TEAM_ID'])
    sorted_df = df_to_sort.sort_values(by=sort_column, ascending=False)
    
    # 정렬된 데이터에 원래의 RANK를 추가
    sorted_df = pd.concat([player_ranking[['RANK']], sorted_df.reset_index(drop=True)], axis=1)
    
    data = {
        'columns': sorted_df.columns.tolist(),
        'data': sorted_df.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/information/prediction_results')
def prediction_results():
    return render_template('prediction_results.html')

@app.route('/api/get_match_result', methods=['GET'])
def get_match_result():
    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')

    home_q1,home_q2,home_q3,home_q4, home_score = team_scores[home_team]
    away_q1,away_q2,away_q3,away_q4, away_score = team_scores[away_team]
    
    df_home1 = home_q1.loc[home_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home1.reset_index(drop=True,inplace=True)
    df_away1 = away_q1.loc[away_q1['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away1.reset_index(drop=True,inplace=True)

    df_home2 = home_q2.loc[home_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home2.reset_index(drop=True,inplace=True)
    df_away2 = away_q2.loc[away_q2['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away2.reset_index(drop=True,inplace=True)

    df_home3 = home_q3.loc[home_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home3.reset_index(drop=True,inplace=True)
    df_away3 = away_q3.loc[away_q3['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away3.reset_index(drop=True,inplace=True)

    df_home4 = home_q4.loc[home_q4['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_home4.reset_index(drop=True,inplace=True)
    df_away4 = away_q4.loc[away_q4['PLAYER'] == 'TOTALS',['FGM','FGA','3PM','3PA','FTM','FTA','OREB','DREB','REB','AST','STL','BLK','TO','PF','PTS','+/-']]
    df_away4.reset_index(drop=True,inplace=True)

    result_home = df_home1 + df_home2 + df_home3 + df_home4
    result_away = df_away1 + df_away2 + df_away3 + df_away4

    result_home[result_home['FGA']==0]['FGA']=1
    result_home[result_home['3PA']==0]['3PA']=1
    result_home[result_home['FTA']==0]['FTA']=1
    result_home['FG%'] = round(result_home['FGM'] / result_home['FGA'], 3)
    result_home['3P%'] = round(result_home['3PM'] / result_home['3PA'], 3)
    result_home['FT%'] = round(result_home['FTM'] / result_home['FTA'], 3)

    result_away[result_away['FGA']==0]['FGA']=1
    result_away[result_away['3PA']==0]['3PA']=1
    result_away[result_away['FTA']==0]['FTA']=1
    result_away['FG%'] = round(result_away['FGM'] / result_away['FGA'], 3)
    result_away['3P%'] = round(result_away['3PM'] / result_away['3PA'], 3)
    result_away['FT%'] = round(result_away['FTM'] / result_away['FTA'], 3)

    result_diff = result_home.subtract(result_away.values)[['BLK','DREB','3P%','FG%','FT%','STL','TO']]
    result_diff.columns = ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']

    model1 = predict.pre_knn(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    model2 = predict.pre_tree(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    model3 = predict.pre_rf(result_diff[['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']])
    model4 = ppm.knn_control_model_prediction(knn_paper_model,result_home['FG%'],result_away['FG%'],result_home['FT%'],result_away['FT%'])
    model5 = ppm.tree_control_model_prediction(tree_paper_model,result_home['FG%'],result_away['FG%'],result_home['FT%'],result_away['FT%'])
    model6 = ppm.rf_control_model_prediction(rf_paper_model,result_home['FG%'],result_away['FG%'],result_home['FT%'],result_away['FT%'])
    # 결과 데이터
    result = {'model1':str(model1),
              'model2':str(model2),
              'model3':str(model3),
              'model4':str(model4),
              'model5':str(model5),
              'model6':str(model6),
        'matchup': f'{home_team} vs {away_team}',
        'score': f'{home_score} : {away_score}'
    }
    


    return jsonify(result)


@app.route('/api/game_schedule', methods=['GET'])
def get_game_schedule():
    df_schedule = nsd.schedule("https://stats.nba.com/stats/scheduleleaguev2int?GameSubType=&LeagueID=15&Season=2024-25&SeasonType=Regular%20Season")
    # year, month, date = datetime.now().date()
    year, month, date = '2024', 7, '12'
    df_now_month = df_schedule[df_schedule['monthNum'] == month]
    df_today = df_now_month[df_now_month['date'] == date]
    data = {
        'columns': df_today.columns.tolist(),
        'data': df_today.to_dict(orient='records')
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
