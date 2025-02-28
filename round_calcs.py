import json
from names import check_name

""" Update the round each game. For the first week a blank round 0 is needed with just empty curly brackets in JSON."""
round = 4
print()
print(f"Round {round} results!")
print()

table_list = []
this_round_data = {}
latest_scores = {}

# open the save data for the players and Norwich's actual score.
with open(f'round_{round}_norwich.json', 'r') as norwich_json:
    norwich_data = json.load(norwich_json)

with open(f'round_{round}_player.json', 'r') as player_json:
    player_data = json.load(player_json)

for player in player_data:
    ### get the values.  
    norwich_result = norwich_data["result"]
    result = player["result"]

    norwich_home_goals = norwich_data["home_goals"]
    home_goals = player["home_goals"]

    norwich_away_goals = norwich_data["away_goals"]
    away_goals = player["away_goals"]
    
    norwich_goal_scorers = norwich_data["goal_scorer"]
    goal_scorer = player["goal_scorer"]

    ### calculate the values.
    # games played
    games_played = 0
    if result == "win" or "lose" or "draw":
        games_played = games_played + 1
    # result
    if result == norwich_result:
        result_score = 1
    else:
        result_score = 0 
    # home goals
    if home_goals == norwich_home_goals:
        home_score = 1
    else:
        home_score = 0   
    # away goals
    if away_goals == norwich_away_goals:
        away_score = 1
    else:
        away_score = 0 
    # goal scorer
    for norwich_goal_scorer in norwich_goal_scorers:
        scorer_score = 0
        if goal_scorer == norwich_goal_scorer:
            scorer_score = scorer_score + 1
            break
    # perfect score
    if home_score + away_score == 2:
        perfect_score = 3
        single_perfect_score = 1
    else:
        perfect_score = 0
        single_perfect_score = 0

    ### total score
    name = player["name"]
    team_name = check_name(name)
    #team_name = team_name.capitalize()
    player_score = perfect_score + result_score + scorer_score
    result_list = [games_played, result_score, scorer_score, single_perfect_score, player_score]
    table_dict = {team_name: result_list}
    this_round_data.update(table_dict)

### compare last week to this week.
last_round = round - 1

# Open and read the last round JSON file
with open(f'round_{last_round}_results.json', 'r') as last_round_results_json:
    last_round_data = json.load(last_round_results_json)

all_players = last_round_data.copy()

print(f"Last Round - {last_round_data}")
print(f"This Round - {this_round_data}")

# add a new player in with 0 points.
for player in this_round_data:
    new_player = ""
    if player not in last_round_data:
        new_player = player
        new_player = this_round_data[player]
        new_player = [0, 0, 0, 0, 0]
        all_players.update({player: new_player})

# give 0 points for a player that didnt play
for player in last_round_data:
    if player not in this_round_data:
        not_played = last_round_data[player]
        not_played = [0, 0, 0, 0, 0]
        this_round_data.update({player: not_played})

# put all the players in alphabetical order.
all_players_order = sorted(all_players)

# add the values from last round to this round.
for player in all_players_order:
    all_players_order = all_players.get(player)
    this_round_order = this_round_data.get(player)
    player_sum = [
        all_players_order[0] + this_round_order[0],
        all_players_order[1] + this_round_order[1], 
        all_players_order[2] + this_round_order[2], 
        all_players_order[3] + this_round_order[3], 
        all_players_order[4] + this_round_order[4]
        ]
    latest_scores.update({player: player_sum})

print()
print(f"Latest Scores - {latest_scores}")
print()
   
with open(f'round_{round}_results.json', 'w') as ngw:
        json.dump(latest_scores, ngw, indent = 2)    

# TODO I want to save the JSON files in seperate folders. 
# TODO create a table. Start with pretty table in python then plotly / matplotlib

