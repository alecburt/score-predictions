### score-predictions

This is my score prediction league I use for my football group Amarillo Army.

Rules are simple:
Each player predicts the result, the score and an anytime goals scorer and recieves between 0-5 pts.
Each game week I need to create a table to show all the results calculated

Written in python with a TKinter gui and Prett Table for the final display.

Currently:
If you run the player_tk you can add in multiple players and print off a .JSON file for which ever round is chosen.
Similarly the norwich_tk will print the actual score to a .JSON file.
Then go to calcs and it will work out the total score of each player. 
Round 0 should be just empty curly brackets. When setting the round to 1 it will add the players scores and put in round_1_results.json.
Round 2 etc. will add any new players, give a blank score to anyone who didn't play who has played before and tally up the following columns.
Player, Games Played, Correct Score (this is worth 3 points), Result, Scorer, Perfect and Total.

The player names go through the format_name function if the name is new it will prompt for the formatted name (currently in the terminal) and add to the formatted_names.json dictionary. 
If the name is already in the dictionary it will continue and add the results as usual.

I now have a working table using PrettyTable the table_pt orders the players in descending order by the Total. 
I would like to add a second and third order to this for in the event of equal points more perfect scores would go above less and then games played.

Future:
Currently the JSON files are a bit of a mess all saving in the main folder I need to learn using Pathlib or similar to tidy up the directories.
Update the table library so it is something a bit more colourful than the ASCII table in pretty table.
I would like to learn more about OOP first but I believe eventually the set up will be better with a Player Class.
