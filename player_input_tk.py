from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import json
from names import format_name

# window
root = Tk()

# title and icon
root.title("Score Predictions")
root.iconbitmap('C:/Users/Alec Burt/Desktop/python/canary_icon.ico')

# image
title_img = ImageTk.PhotoImage(Image.open("amarillo_army.png"))
title_label = Label(image = title_img)
title_label.grid(row = 0, column = 0, columnspan = 5)

norwich_label = Label(text = "Player Scores:", font = ('', 14))
norwich_label.grid(row = 1, column = 0, columnspan = 5, sticky = 'W')

# round number entry
round_label = Label(text = "What round is it?", font = ('', 10))
round_label.grid(row = 2, column = 0, sticky = 'W')
round_var = IntVar()
round_entry = Entry(borderwidth = 2, textvariable = round_var)
round_entry.grid(row = 2, column = 1, sticky = 'NSEW')

# platform buttons
platform_label = Label(text = "Which Platform?", font = ('', 10))
platform_label.grid(row = 1, column = 2, sticky = 'W')

which_platform = "WA"

def platform_clicked():
    platform = platform_var.get()
    global which_platform
    which_platform = platform
    return which_platform

platform_var = StringVar()

wa_button = Radiobutton(root, text = "WA", variable = platform_var, value = "WA", command = platform_clicked)
wa_button.grid(row = 2, column = 2)
fb_button = Radiobutton(root, text = "FB", variable = platform_var, value = "FB", command = platform_clicked)
fb_button.grid(row = 2, column = 3)
x_button = Radiobutton(root, text = "X", variable = platform_var, value = "X", command = platform_clicked)
x_button.grid(row = 2, column = 4)

platform_var.set("WA")

# space
space = Label(text = "")
space.grid(row = 3, column = 0, columnspan = 5)

### headers and entries
# name
name_label = Label(text = "Name?", font = ('', 10))
name_label.grid(row = 4, column = 0, sticky = 'W')

name_var = StringVar()
name_entry = Entry(borderwidth = 2, textvariable = name_var)
name_entry.grid(row = 5, column = 0, sticky = 'NSEW')

# win lose or draw entry
wld_label = Label(text = "Win Lose or Draw?", font = ('', 10))
wld_label.grid(row = 4, column = 1, sticky = 'W')

wld_checkbox = ""
wld_list = ["Win", "Lose", "Draw"]

wld_combo = ttk.Combobox(root, values = wld_list, state = "readonly")
wld_combo.grid(row = 5, column = 1, sticky = 'NSEW')
wld_combo.set("Win")

# home goals entry
home_label = Label(text = "Home Goals?", font = ('', 10))
home_label.grid(row = 4, column = 2, sticky = 'W')

home_var = StringVar()
home_entry = Entry(borderwidth = 2, textvariable = home_var)
home_entry.grid(row = 5, column = 2, sticky = 'NSEW')

# away goals entry
away_label = Label(text = "Away Goals?", font = ('', 10))
away_label.grid(row = 4, column = 3, sticky = 'W')

away_var = StringVar()
away_entry = Entry(borderwidth = 2, textvariable = away_var)
away_entry.grid(row = 5, column = 3, sticky = 'NSEW')

# goal scorer entry
scorer_label = Label(text = "Goal Scorer?", font = ('', 10))
scorer_label.grid(row = 4, column = 4, sticky = 'W')

# scorers
scorer_list = ["No Goalscorer", "Tonto", "Sargent", "Crnac", "Schwartau", "Kvistgaarden", "Jurasek", "Nunez", "Gibbs", "Marcondes", "McLean", "Wright", "Forson",
        "Duffy", "Cordoba", "Chrisene", "Darling", "Medic", "McConville", "Fisher", "Stacey", "Forsyth", "Aboh", "Myles", "Springett", "Tomkinson", "Hills", "Kovacevic"
]

scorer_combo = ttk.Combobox(root, values = scorer_list, state = "readonly")
scorer_combo.grid(row = 5, column = 4, sticky = 'NSEW')
scorer_combo.set("No Goalscorer")

player_list = []

def player_save_listbox():
    player_name = name_var.get()
    team_name = format_name(player_name)
    name_listbox.insert(0, team_name)
    team_name = team_name.title()
    
    player_win_lose_draw = wld_combo.get()
    wld_listbox.insert(0, player_win_lose_draw)
    player_win_lose_draw = player_win_lose_draw.lower()
    player_home_goals = home_var.get()
    home_listbox.insert(0, player_home_goals)
    player_home_goals = int(player_home_goals)
    player_away_goals = away_var.get()
    away_listbox.insert(0, player_away_goals)
    player_away_goals = int(player_away_goals)
    player_scorer = scorer_combo.get()
    scorer_listbox.insert(0, player_scorer)
    player_scorer = player_scorer.lower()
    
    player_dict = {
        "name" : team_name,
        "result" : player_win_lose_draw,
        "home_goals" : player_home_goals,
        "away_goals" : player_away_goals,
        "goal_scorer" : player_scorer,
        "platform" : which_platform,
        }

    player_dict.update({"name": team_name,  "result": player_win_lose_draw, "home_goals": player_home_goals,  "away_goals": player_away_goals, "goal_scorer": player_scorer, "platform": which_platform})
    player_list.append(player_dict)


# submit player button
player_submit_button = Button(root, text = "Submit Player", command = player_save_listbox)
player_submit_button.grid(row = 6, column = 0, sticky = 'NSEW')

# space
space = Label(text = "")
space.grid(row = 7, column = 0, columnspan = 5)

### listboxes
# name listbox
name_listbox = Listbox(root)
name_listbox.grid(row = 8, column = 0)

# win lose or dray listbox
wld_listbox = Listbox(root)
wld_listbox.grid(row = 8, column = 1)

# home goals listbox
home_listbox = Listbox(root)
home_listbox.grid(row = 8, column = 2)

# away goals listbox
away_listbox = Listbox(root)
away_listbox.grid(row = 8, column = 3)

# scorer listbox
scorer_listbox = Listbox(root)
scorer_listbox.grid(row = 8, column = 4)

def player_submit_all():
    messagebox.askquestion("", "Are all the players in?")
    messagebox.showinfo("", "Good Job!")
    current_round = round_var.get()

    # convert to json
    with open(f'round_{current_round}_player.json', 'w') as ngw:
            json.dump(player_list, ngw, indent = 2)

# submit all button
button_submit = Button(root, text = "Submit All", command = player_submit_all)
button_submit.grid(row = 9, column = 0, sticky = 'NSEW')

# TODO make it so i can add to an existing json so that i can fill out in stages rather than all at once, i think currently i replace.

root.mainloop()
