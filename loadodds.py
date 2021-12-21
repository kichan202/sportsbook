# import pandas as pd
# from datetime import datetime
# """import subprocess
# lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# lpr.stdin.write("hello".encode())"""


# code_names_file = "/home/gaza/Documents/sportsbook/sportsbook/codenames.csv"
# available_bets_file = "/home/gaza/Documents/sportsbook/sportsbook/dailybets.csv"

# #read the file into memory

# def load_code_names():
#     data = pd.read_csv(code_names_file) #read in the csv file
#     df = pd.DataFrame(data, columns=['code','name', 'league']) #make a dataframe using panda
#     #set "code" to the index, transpose and make a list, and to dictionary
#     code_names = df.set_index('code').T.to_dict('list')
#     #return the dictionary
#     return code_names

# def load_available_bets():
#     data = pd.read_csv(available_bets_file)
#     df = pd.DataFrame(data, columns=['code','spread','spreadodds','moneyline', 'over/under', 'o/u odds', 'time', 'vs'])
#     available_bets = df.set_index('code').T.to_dict('list')
#     return available_bets


# def print_line():
#     code_names = load_code_names()
#     available_bets = load_available_bets()
#     now = datetime.now()
#     #dd/mm/YY H:M:S
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     print("\t"+dt_string)
#     print("\tFull Games/Halfs")
#     print("\tSpread MoneyLine O/U")
#     print("\n")
#     print("===============================================================")
#     print("NFL: FULL GAME")
#     print("===============================================================")
#     print("CODE     TEAM                 M.L     SPREAD OVER/UNDER")
#     print(" ---------------------------------------------------------------")
#     for key in range(0,len(available_bets)):
#         print(key)
#         for j in range(key+1,len(available_bets)):
#             print(key)
#             return

#         """
#         values_list = available_bets[key]
#         name = code_names[key]
#         print("%s     %s  %s  %s(%s)" %(key, name[0],values_list[2],values_list[0],values_list[1]))
#         #print(key, name[0],values_list[2],values_list[0],"(%s)" %values_list[1])"""
        




# #print(available_bets)

# #prints the keys in the dictionary
# #for key in available_bets:
# #    print(key)

# #for key in available_bets:
# #    print(key, '->', available_bets[key])

# #print_line()

# #print(load_code_names())
# print(load_available_bets())

import pandas as pd

code_names_file = "/home/gaza/Documents/sportsbook/sportsbook/codenames.csv"
available_bets_file = "/home/gaza/Documents/sportsbook/sportsbook/dailybets.csv"

data = pd.read_csv(code_names_file)
df = pd.DataFrame(data,columns=['code','name','league'])
code_names = df.set_index('code').T.to_dict('list')

data1 = pd.read_csv(available_bets_file)
df1 = pd.DataFrame(data1,columns=['code','spread','spreadodds','moneyline','date','over/under','o/u odds'])
df2 = pd.DataFrame(data1,columns=['vs','time'])
available_bets = df1.set_index('code').T.to_dict('list')
available_bets1 = df2.set_index('vs').T.to_dict('list')
print(available_bets)
print("=========================================================================")
print(available_bets1)

