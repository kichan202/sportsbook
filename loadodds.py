import pandas as pd

code_names_file = "/home/gaza/Documents/sportsbook/sportsbook/codenames.csv"
available_bets = "/home/gaza/Documents/sportsbook/sportsbook/dailybets.csv"

#read the file into memory

def load_code_names():
    data = pd.read_csv(code_names_file) #read in the csv file
    df = pd.DataFrame(data, columns=['code','name', 'league']) #make a dataframe using panda
    #set "code" to the index, transpose and make a list, and to dictionary
    dictionary = df.set_index('code').T.to_dict('list')
    #return the dictionary
    return dictionary

data = pd.read_csv(available_bets)
df = pd.DataFrame(data, columns=['code','spread','spreadodds','moneyline', 'over/under', 'o/u odds', 'time', 'vs'])
print(df)