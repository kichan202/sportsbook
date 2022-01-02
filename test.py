from printline import *

codes = load_codes()
games = load_games()

print("What Would you like to do?")
x = input("To print line Enter (P) to place bet Enter (B): ")
if x[0] == "p":
    print("Which Lines do you want to print?")
    available = leagues_in_action()
    print("Leagues Available today are %s" %available)
    x = input("Enter Choices seperated by a space ex: nfl nba mlb etc:")
    choices = x.split()
    chosen = []   
    for x in choices:
        if x in available:
            chosen.append(x)
    print_line(select_line(*chosen))
elif x[0] == "b":
    x = int(input("Enter code of team: "))
    for key in games:
        vs_key = games[key][7]
        if x == key or x == vs_key:
            print("cook the books")
            break
        
else:
    print("Enter P or B")



