from printline import load_codes, load_games
from datetime import datetime

def select_line(*argv):
    codes = load_codes()
    games = load_games()
    for arg in argv:
        for key in games:
            league =codes[key][0]
            while(league == arg):
                print("arg")





choices = ["nfl","nba", "mlb"]

select_line(*choices)