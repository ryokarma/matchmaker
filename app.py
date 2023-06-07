from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import matchmaker

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'un secret par défaut')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/overwatch')
def overwatch():
    return render_template('overwatch.html')

@app.route('/lol')
def lol():
    return render_template('lol.html')

@app.route('/match_ow', methods=['POST'])
def match_ow():
    data = [request.form.get(f'player{i}') for i in range(1, 11)]
    blue_team, red_team, roaster_red, roaster_blue = matchmaker.teams_overwatch(data)
    return render_template('results_ow.html', blue_team=blue_team, red_team=red_team, roaster_red=roaster_red, roaster_blue=roaster_blue)

@app.route('/match_lol', methods=['POST'])
def match_lol():
    data = [request.form.get(f'player{i}') for i in range(1, 11)]
    blue_team, red_team, roaster_red, roaster_blue = matchmaker.teams_lol(data)
    return render_template('results_lol.html', blue_team=blue_team, red_team=red_team, roaster_red=roaster_red, roaster_blue=roaster_blue)

if __name__ == '__main__':
    app.run(debug=True)
