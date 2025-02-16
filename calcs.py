import json

round = 1
print()
print(f"Round {round} results!")
print()

# Open and read the norwich JSON file
with open(f'round_{round}_norwich.json', 'r') as norwich_json:
    norwich_data = json.load(norwich_json)

# Open and read the player JSON file
with open(f'round_{round}_player.json', 'r') as player_json:
    player_data = json.load(player_json)
    for player in player_data:

        ### values
        norwich_result = norwich_data["result"]
        result = player["result"]

        norwich_home_goals = norwich_data["home_goals"]
        home_goals = player["home_goals"]

        norwich_away_goals = norwich_data["away_goals"]
        away_goals = player["away_goals"]
        
        norwich_goal_scorers = norwich_data["goal_scorer"]
        goal_scorer = player["goal_scorer"]

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
        name = name.capitalize()
        player_score = perfect_score + result_score + scorer_score
        
        table_dict = {
            "player" : name,
            "result" : result_score,
            "scorer" : scorer_score,
            "perfect" : single_perfect_score,
            "Total" : player_score
        }

        print(table_dict)
print()
