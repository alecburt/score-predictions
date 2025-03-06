import json
from prettytable import PrettyTable 

round = 2

with open(f'round_{round}_results.json', 'r') as results_json:
    table_data = json.load(results_json)

# sort the table by total 
sorted_table_data = sorted(table_data.items(), key=lambda x: x[1][5], reverse = True)    

# create table
score_prediction_table = PrettyTable(["Position", "Player", "Games Played", "Correct Score", "Correct Result", "Goalscorer", "Perfect", "Total"]) 
  
# add rows
index = 0 
for player_score in sorted_table_data:
    index += 1
    sorted_player_list = [index, player_score[0], player_score[1][0], player_score[1][1], player_score[1][2], player_score[1][3], player_score[1][4], player_score[1][5]]
    score_prediction_table.add_row(sorted_player_list) 

  
print(score_prediction_table)
