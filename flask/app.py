from flask import Flask, render_template, request, jsonify
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import pytz
import random
import requests
import NBA_Player_RANK as npr

app = Flask(__name__)

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

# 팀 순위 데이터 
df_team_ranking = pd.DataFrame({
    '순위' : [i for i in range(1,len(teams)+1)],
    '팀명': teams,
    '승': [50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 3, 5, 7, 9],
    '패': [32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 81, 79, 77, 75, 73]
})

df_team_ranking['승률'] = df_team_ranking['승'] / (df_team_ranking['승'] + df_team_ranking['패'])
df_team_ranking['승률'] = df_team_ranking['승률'].apply(lambda x: round(x, 3))

def update_team_ranking():
    global df_team_ranking

# 경기일정 데이터    
# 10개의 팀 선택
selected_teams = random.sample(teams, 10)

cached_player_ranking = None
last_update_time = datetime.now(pytz.timezone('Asia/Seoul')) - timedelta(days=1)  # 초기값을 하루 전으로 설정

def update_player_ranking_cache():
    global cached_player_ranking, last_update_time
    current_time = datetime.now(pytz.timezone('Asia/Seoul'))
    if current_time - last_update_time >= timedelta(days=1):  # 하루가 경과한 경우에만 업데이트
        cached_player_ranking = npr.player_rank()
        last_update_time = current_time

# 5경기 생성
games = []
start_date = datetime.now()
for i in range(5):
    game_date = start_date + timedelta(days=i)
    home_team, away_team = random.sample(selected_teams, 2)
    games.append({
        '날짜': game_date.strftime('%Y-%m-%d'),
        '홈팀': home_team,
        '어웨이팀': away_team
    })

df_games = pd.DataFrame(games)    

# 실제 결과와 예측 결과
predictions = pd.DataFrame(columns=['경기', '예측결과'])
actual_results = pd.DataFrame(columns=['경기', '실제결과'])

def fetch_actual_results():
    # 실제 경기 결과를 가져오는 함수
    # 여기에 실제 API 호출을 넣어야 합니다.
    # 예시로 랜덤 데이터 생성
    results = []
    for i in range(5):
        home_team, away_team = random.sample(teams, 2)
        result = f"{home_team} vs {away_team}: {random.choice([home_team, away_team])} 승"
        results.append(result)
    return results

def predict_game_results():
    # 예측 결과를 생성하는 함수
    results = []
    for i in range(5):
        home_team, away_team = random.sample(teams, 2)
        prediction = f"{home_team} vs {away_team}: {random.choice([home_team, away_team])} 승"
        results.append(prediction)
    return results

def update_results():
    global predictions, actual_results
    predicted = predict_game_results()
    actual = fetch_actual_results()
    
    # 현재 날짜와 함께 결과 저장
    date = datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d')
    predictions = pd.DataFrame({'경기': [f'경기 {i+1}' for i in range(5)], '예측결과': predicted})
    actual_results = pd.DataFrame({'경기': [f'경기 {i+1}' for i in range(5)], '실제결과': actual})    
    
        
korea_tz = pytz.timezone('Asia/Seoul')

scheduler = BackgroundScheduler(timezone=korea_tz)
scheduler.add_job(update_team_ranking, 'cron', hour=18)
scheduler.add_job(update_results, 'cron', hour=18)
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
    data = pd.read_csv('merged_df.csv').head(10).to_dict(orient='records')
    return render_template('real_time.html', data= data)

@app.route('/prediction/future_games', methods = ['GET','POST'])
def future_games():
    if request.method == 'POST':
        data = request.get_json()
        home = data.get('home_team')
        away = data.get('away_team')
        if home > away:
            result = home
        else :
            result = away 
        return jsonify({'result': result})
    return render_template('prediction_index.html')

@app.route('/information')
def information():
    return render_template('information_.html')

@app.route('/information/game_schedule')
def game_schedule():
    return render_template('game_schedule.html')

@app.route('/information/team_ranking')
def team_ranking():
    return render_template('team_ranking.html')

@app.route('/api/team_ranking', methods=['GET'])
def get_team_ranking():
    data = {
        'columns': df_team_ranking.columns.tolist(),
        'data': df_team_ranking.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/information/player_ranking')
def player_ranking():
    return render_template('player_ranking.html')

@app.route('/api/player_ranking', methods=['GET'])
def get_player_ranking():
    update_player_ranking_cache()
    data = {
        'columns': cached_player_ranking.columns.tolist(),
        'data': cached_player_ranking.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/information/prediction_results')
def prediction_results():
    return render_template('prediction_results.html')

@app.route('/api/prediction_results', methods=['GET'])
def get_prediction_results():
    data = {
        'predictions': predictions.to_dict(orient='records'),
        'actual_results': actual_results.to_dict(orient='records')
    }
    return jsonify(data)

@app.route('/api/game_schedule', methods=['GET'])
def get_game_schedule():
    data = {
        'columns': df_games.columns.tolist(),
        'data': df_games.to_dict(orient='records')
    }
    return jsonify(data)

if __name__ == '__main__':
    update_team_ranking()
    app.run('0.0.0.0', port=5000, debug=True)
