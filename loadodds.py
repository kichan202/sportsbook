import pandas as pd

file_path = "/home/gaza/Documents/sportsbook/sportsbook/codenames.csv"

#read the file into memory

def load_code_names():
    data = pd.read_csv(file_path) #read in the csv file
    df = pd.DataFrame(data, columns=['code','name', 'league']) #make a dataframe using panda
    #set "code" to the index, transpose and make a list, and to dictionary
    dictionary = df.set_index('code').T.to_dict('list')
    #return the dictionary
    if 2020 in dictionary:
        print(dictionary[2020])
    else:
        print("what the fuck")
    return dictionary

load_code_names()