### score-predictions

This is my score prediction league I use for my football group Amarillo Army.

Rules are simple:
Each player predicts the result, the score and an anytime goals scorer and recieves between 0-5 pts.
Each game week I need to create a table to show all the results calculated

Written in python with a TKinter gui.

Currently:
If you run the player_tk you can add in multiple players and print of a .JSON file for which ever round is chosen.
Similarly the norwich_tk will print the actual score to a .JSON file.
Then go to calcs and it will work out currently just the total score of each player on a single round.

Future:
I need to expand the calculations so that it can tally up across multiple rounds.
Increase the outputs so I get record the whole table ie. matches played, and the points broken down where they came from.
Create a table maybe in python first then look at plotly or similar for the graphics this will take some learning though.

Problems:
I think the name is going to be a bit of a pain but inthery I can use either the X handle or facebook name as an input then have it change to a chosen team name like in fantasy football.
I need to work out the best way to add up over the season either calculate all .JSON files at once or have a rolling tally and create a new updated table each round and simply add the next week onto the last week.
