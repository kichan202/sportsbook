from datetime import datetime
import pandas as pd
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

def select_line(*argv):
    #load the games and codes
    codes = load_codes()
    games = load_games()
    has_a_game = 0
    line ="" #major array had it as line=[] which was saving each character instead of a string
    """loop through the games
    if they match the league add it to the string
    should use a dictionary?"""
    code_team = "CODE  TEAM\tSPREAD\t\tM.L\tO\\U"
    equals_sign="============================================"
    dash_sign = "--------------------------------------------"
    for arg in argv:
        title = "%s: \t\tFULL TIME GAME"%str.upper(arg)
        data="%s\n%s\n%s\n%s\n%s\n"%(equals_sign,title,equals_sign,code_team,dash_sign)
        for key in games:
            main_list = games[key]
            vs_list = codes[main_list[7]]
            game_time = main_list[6]
            if(vs_list[0] == arg):
                has_a_game+=1
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

                #PickEm
                if away_team_spread == 0 :
                    away_team_spread = "PK"
                
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
                         
        line+=data
    return line

def leagues_in_action():
    data = []
    codes = load_codes()
    games = load_games()
    
    for key in games:
        data.append(codes[key][0])

    return set(data)

def print_line(arg):
    time_object= datetime.now()
    time = time_object.strftime("%d/%b/%Y %I:%M %p")
    header ="%s\n\tFull Games\n\tTeams MoneyLine O/U"%time
    line = "\t%s\n"%(header)
    line+=arg
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    lpr.stdin.write(line.encode())