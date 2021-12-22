from datetime import date, datetime
import pandas as pd
from pandas.core.arrays import string_

codes_file = "/home/gaza/Documents/sportsbook/sportsbook/nflcodes.csv"
games_file = "/home/gaza/Documents/sportsbook/sportsbook/dailybets.csv"

def load_codes():
    data = pd.read_csv(codes_file)
    df = pd.DataFrame(data, columns=['code','league','name'])
    codes = df.set_index('code').T.to_dict('list')
    return codes


def load_games():
    data = pd.read_csv(games_file)
    df = pd.DataFrame(data)
    games = df.set_index('code').T.to_dict('list')
    return games


def print_line():
    text = ""
    codes = load_codes()
    games = load_games()
    
    for key in games:
        #must use variables
        main_list = games[key]
        vs_list = codes[main_list[7]]
        game_time = main_list[6]

        #string to time object
        time_object = datetime.strptime(game_time, '%I:%M %p').time()
        #only games that the time hasn't passed will be available for now
        if time_object > datetime.now().time():
            print("%s" %game_time)
            spread_number = ""
            game_string = "%s %s\t%s(%s)\t%s\t%s" %(key,codes[key][1], main_list[0], main_list[1], main_list[2], main_list[4])
            vs_string = "%s %s\t%s\t\t%s\t%s" %(main_list[7], vs_list[1],main_list[8],main_list[9],main_list[5])
            print("%s\n%s" %(game_string,vs_string))
        

print_line()