from datetime import datetime
import pandas as pd
from pandas.core.arrays import string_
import subprocess

codes_file = "/home/gaza/Documents/sportsbook/sportsbook/codenames.csv"
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

def print_line(*argv):
    time_object= datetime.now()
    time = time_object.strftime("%d/%b/%Y %I:%M %p")
    header ="%s\n\tFull Games\n\tTeams MoneyLine O/U"%time
    line = "\t%s\n"%(header)
    for arg in argv:
        line+=arg
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    lpr.stdin.write(line.encode())


def nfl_line():
    codes = load_codes()
    games = load_games()
    title = "NFL: \t\tFULL TIME GAME"
    code_team = "CODE  TEAM\tSPREAD\t\tM.L\tO\\U"
    equals_sign="============================================"
    dash_sign = "--------------------------------------------"
    data="%s\n%s\n%s\n%s\n%s\n"%(equals_sign,title,equals_sign,code_team,dash_sign)
    if bool(games):
        for key in games:
            #must use variables
            main_list = games[key]
            vs_list = codes[main_list[7]]
            game_time = main_list[6]
            league =codes[key][0]
            if league == 'nfl':
                away_team_name =codes[key][1]
                home_team_name = vs_list[1]
                away_team_code = key
                home_team_code=main_list[7]
                away_team_spread=main_list[0]
                away_team_spread_odds = main_list[1]
                home_team_spread_odds= main_list[8]
                over_under=main_list[4]
                over_under_odds= main_list[5]
                away_team_money_line = main_list[2]
                home_team_money_line = main_list[9]

                if away_team_spread > 0 :
                    away_team_spread = "+%s"%away_team_spread
                
                if home_team_money_line > 0 :
                    home_team_money_line = "+%s"%home_team_money_line

                #string to time object
                time_object = datetime.strptime(game_time, '%I:%M %p').time()
                #only games that the time hasn't passed will be available for now
                if time_object > datetime.now().time():
                    #print("%s" %game_time)
                    game_string = "%s %s\t%s(%s)\t%s\t%s" %(away_team_code,away_team_name, away_team_spread,away_team_spread_odds, away_team_money_line, over_under)
                    vs_string = "%s %s\t%s\t\t%s\t%s" %(home_team_code, home_team_name,home_team_spread_odds,home_team_money_line,over_under_odds)

                    data+="%s\n%s\n%s\n%s\n"%(game_time,game_string,vs_string,dash_sign)
    return data


def nba_line():
    codes = load_codes()
    games = load_games()
    title = "NBA: \t\tFULL TIME GAME"
    code_team = "CODE  TEAM\tSPREAD\t\tM.L\tO\\U"
    equals_sign="============================================"
    dash_sign = "--------------------------------------------"
    data="%s\n%s\n%s\n%s\n%s\n"%(equals_sign,title,equals_sign,code_team,dash_sign)
    if bool(games):
        for key in games:
            #must use variables
            main_list = games[key]
            vs_list = codes[main_list[7]]
            game_time = main_list[6]
            league =codes[key][0]
            if league == 'nba':
                away_team_name =codes[key][1]
                home_team_name = vs_list[1]
                away_team_code = key
                home_team_code=main_list[7]
                away_team_spread=main_list[0]
                away_team_spread_odds = main_list[1]
                home_team_spread_odds= main_list[8]
                over_under=main_list[4]
                over_under_odds= main_list[5]
                away_team_money_line = main_list[2]
                home_team_money_line = main_list[9]

                if away_team_spread > 0 :
                    away_team_spread = "+%s"%away_team_spread
                
                if home_team_money_line > 0 :
                    home_team_money_line = "+%s"%home_team_money_line

                #string to time object
                time_object = datetime.strptime(game_time, '%I:%M %p').time()
                #only games that the time hasn't passed will be available for now
                if time_object > datetime.now().time():
                    #print("%s" %game_time)
                    game_string = "%s %s\t%s(%s)\t%s\t%s" %(away_team_code,away_team_name, away_team_spread,away_team_spread_odds, away_team_money_line, over_under)
                    vs_string = "%s %s\t%s\t\t%s\t%s" %(home_team_code, home_team_name,home_team_spread_odds,home_team_money_line,over_under_odds)

                    data+="%s\n%s\n%s\n%s\n"%(game_time,game_string,vs_string,dash_sign)
    return data


def mlb_line():
    codes = load_codes()
    games = load_games()
    title = "MLB: \t\tFULL TIME GAME"
    code_team = "CODE  TEAM\tSPREAD\t\tM.L\tO\\U"
    equals_sign="============================================"
    dash_sign = "--------------------------------------------"
    data="%s\n%s\n%s\n%s\n%s\n"%(equals_sign,title,equals_sign,code_team,dash_sign)
    if bool(games):
        for key in games:
            #must use variables
            main_list = games[key]
            vs_list = codes[main_list[7]]
            game_time = main_list[6]
            league =codes[key][0]
            if league == 'mlb':
                away_team_name =codes[key][1]
                home_team_name = vs_list[1]
                away_team_code = key
                home_team_code=main_list[7]
                away_team_spread=main_list[0]
                away_team_spread_odds = main_list[1]
                home_team_spread_odds= main_list[8]
                over_under=main_list[4]
                over_under_odds= main_list[5]
                away_team_money_line = main_list[2]
                home_team_money_line = main_list[9]

                if away_team_spread > 0 :
                    away_team_spread = "+%s"%away_team_spread
                
                if home_team_money_line > 0 :
                    home_team_money_line = "+%s"%home_team_money_line

                #string to time object
                time_object = datetime.strptime(game_time, '%I:%M %p').time()
                #only games that the time hasn't passed will be available for now
                if time_object > datetime.now().time():
                    #print("%s" %game_time)
                    game_string = "%s %s\t%s(%s)\t%s\t%s" %(away_team_code,away_team_name, away_team_spread,away_team_spread_odds, away_team_money_line, over_under)
                    vs_string = "%s %s\t%s\t\t%s\t%s" %(home_team_code, home_team_name,home_team_spread_odds,home_team_money_line,over_under_odds)

                    data+="%s\n%s\n%s\n%s\n"%(game_time,game_string,vs_string,dash_sign)
    return data


def nhl_line():
    codes = load_codes()
    games = load_games()
    title = "NHL: \t\tFULL TIME GAME"
    code_team = "CODE  TEAM\tSPREAD\t\tM.L\tO\\U"
    equals_sign="============================================"
    dash_sign = "--------------------------------------------"
    data="%s\n%s\n%s\n%s\n%s\n"%(equals_sign,title,equals_sign,code_team,dash_sign)
    if bool(games):
        for key in games:
            #must use variables
            main_list = games[key]
            vs_list = codes[main_list[7]]
            game_time = main_list[6]
            league =codes[key][0]
            if league == 'NHL':
                away_team_name =codes[key][1]
                home_team_name = vs_list[1]
                away_team_code = key
                home_team_code=main_list[7]
                away_team_spread=main_list[0]
                away_team_spread_odds = main_list[1]
                home_team_spread_odds= main_list[8]
                over_under=main_list[4]
                over_under_odds= main_list[5]
                away_team_money_line = main_list[2]
                home_team_money_line = main_list[9]

                if away_team_spread > 0 :
                    away_team_spread = "+%s"%away_team_spread
                
                if home_team_money_line > 0 :
                    home_team_money_line = "+%s"%home_team_money_line

                #string to time object
                time_object = datetime.strptime(game_time, '%I:%M %p').time()
                #only games that the time hasn't passed will be available for now
                if time_object > datetime.now().time():
                    #print("%s" %game_time)
                    game_string = "%s %s\t%s(%s)\t%s\t%s" %(away_team_code,away_team_name, away_team_spread,away_team_spread_odds, away_team_money_line, over_under)
                    vs_string = "%s %s\t%s\t\t%s\t%s" %(home_team_code, home_team_name,home_team_spread_odds,home_team_money_line,over_under_odds)

                    data+="%s\n%s\n%s\n%s\n"%(game_time,game_string,vs_string,dash_sign)
    return data


print_line(nfl_line())