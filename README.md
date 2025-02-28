### score-predictions

This is my score prediction league I use for my football group Amarillo Army.

Rules are simple:
Each player predicts the result, the score and an anytime goals scorer and recieves between 0-5 pts.
Each game week I need to create a table to show all the results calculated

Written in python with a TKinter gui.

Currently:
If you run the player_tk you can add in multiple players and print off a .JSON file for which ever round is chosen.
Similarly the norwich_tk will print the actual score to a .JSON file.
Then go to calcs and it will work out the total score of each player. 
Round 0 should be just empty curly brackets. When setting the round to 1 it will add the players scores and put in round_1_results.json.
Round 2 etc. will add any new players, give a blank score to anyone who didn't play who has played before and tally up the following columns.
Player, Games Played, Result, Scorer, Perfect (this is worth 3 points) and Total.

The player names go through the check_name function if the name has already been registered I will be able to copy and paste a Twitter handle and it will format to the desired name or if un-registered it will save the Twitter handle as the team_name. It is functional but once I've used it a few times I think it will need to be made a bit more user friendly.

Future:
Currently the JSON files are a bit of a mess all saving in the main folder I need to learn using Pathlib or similar to tidy up the directories.
Create a table maybe in python first then look at plotly or similar for the graphics this will take some learning though.
I would like to learn more about OOP first but I believe eventually the set up will be better with a Player Class.



