import json

### player inputs 
print("Add a players prediction.")
print()
player_list = []

for player in range(100): 
    name = input("Player name?  ").lower()
    result = input("Win, Lose or Draw?  ").lower()
    home_goals = input("Home goals?  ")
    home_goals = int(home_goals)
    away_goals = input("Away goals?  ")
    away_goals = int(away_goals)
    goal_scorer = input("Goal Scorer?  ").lower()

    print()
    again = input("Again y/n?  ")
    print()

    player_dict = {
    "name" : name,
    "result" : result,
    "home_goals" : home_goals,
    "away_goals" : away_goals,
    "goal_scorer" : goal_scorer
    }

    player_dict.update({"name": name,  "result": result, "home_goals": home_goals,  "away_goals": away_goals, "goal_scorer": goal_scorer})
    player_list.append(player_dict)

    
    if again == "n":
        print(player_list)
        with open('gw_1_player.json', 'w', encoding = "utf-8") as pgw:
            json.dump(player_list, pgw)
        break


### norwich inputs
print()
print("What was the actual score?")
print()
norwich_result = input("Result? Win, lose or draw.  ")
norwich_home_goals = input("Home goals?  ")
norwich_home_goals = int(norwich_home_goals)
norwich_away_goals = input("Away goals?  ")
norwich_away_goals = int(norwich_away_goals)

scorer_list = []
for scorer in range(10): 
    first_goal_scorer = input("First Goal Scorer or No Goal Scorer?  ").lower()
    scorer_list.append(first_goal_scorer)
    again = input("Again y/n?  ")
    print()
    if again == "n":
        break
    second_goal_scorer = input("Second Goal Scorer?  ").lower()
    scorer_list.append(second_goal_scorer)
    again = input("Again y/n?  ")
    break

# norwich dictionary
norwich_dict = {
    "result" : norwich_result,
    "home_goals" : norwich_home_goals,
    "away_goals" : norwich_away_goals,
    "goal_scorer" : scorer_list
}

# convert to json
with open('gw_1_norwich.json', 'w') as ngw:
    json.dump(norwich_dict, ngw)
