import json

# Open and read the JSON file
with open('gw_1_norwich.json', 'r') as norwich:
    norwich_data = json.load(norwich)

# Print the data
print(norwich_data)
print()

# Open and read the JSON file
with open('gw_1_player.json', 'r') as player:
    player_data = json.load(player)

# Print the data
print(player_data)
print()

### values
norwich_result = norwich_data["result"]
print(norwich_result)
for player in player_data:
    result = player["result"]
    print(result)
    print()

norwich_home_goals = norwich_data["home_goals"]
print(norwich_home_goals)
for player in player_data:
    home_goals = player["home_goals"]
    print(home_goals)
    print()

norwich_away_goals = norwich_data["away_goals"]
print(norwich_away_goals)
for player in player_data:
    away_goals = player["away_goals"]
    print(away_goals)
    print()

norwich_goal_scorer = norwich_data["goal_scorer"]
print(norwich_goal_scorer)
for player in player_data:
    goal_scorer = player["goal_scorer"]
    print(goal_scorer)
    print()

### calculator
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
# TODO the goal scorer is not being added because norwich_goal_scorer is a list. needs looking at.
if goal_scorer == norwich_goal_scorer:
    scorer_score = 1
else:
    scorer_score = 0

# perfect score
if home_score + away_score == 2:
    perfect_score = 3
else:
    perfect_score = 0

# score
player_score = perfect_score + result_score + scorer_score
print()
if player_score == 1:
    print(f"You got {player_score} point.")
else:
    print(f"You got {player_score} points.")

# TODO so far only works with 1 player I need to run it through a for loop for each player.
