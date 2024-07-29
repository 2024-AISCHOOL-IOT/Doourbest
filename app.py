from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction/real_time')
def real_time():
    return render_template('real_time.html')

@app.route('/prediction/future_games')
def future_games():
    return render_template('future_games.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/information/game_schedule')
def game_schedule():
    return render_template('game_schedule.html')

@app.route('/information/team_ranking')
def team_ranking():
    return render_template('team_ranking.html')

@app.route('/information/player_ranking')
def player_ranking():
    return render_template('player_ranking.html')

@app.route('/information/prediction_results')
def prediction_results():
    return render_template('prediction_results.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
