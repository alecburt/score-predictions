from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import json

# window
root = Tk()

# title and icon
root.title("Score Predictions")
root.iconbitmap('C:/Users/Alec Burt/Desktop/python/canary_icon.ico')

# image
title_img = ImageTk.PhotoImage(Image.open("amarillo_army.png"))
title_label = Label(image = title_img)
title_label.grid(row = 0, column = 0, columnspan = 2)

norwich_label = Label(text = "Norwich Actual Score:  ", font = ('', 14))
norwich_label.grid(row = 1, column = 0, columnspan = 2, sticky = 'W')

# round number entry
round_label = Label(text = "What round is it?", font = ('', 10))
round_label.grid(row = 2, column = 0, sticky = 'W')
round_var = IntVar()
round_entry = Entry(width = 30, borderwidth = 2, textvariable = round_var)
round_entry.grid(row = 2, column = 1, sticky = 'NSEW')

# space
space = Label(text = "")
space.grid(row = 3, column = 0, columnspan = 2)

# win lose or draw entry
win_lose_draw_label = Label(text = "win, lose or draw?", font = ('', 10))
win_lose_draw_label.grid(row = 4, column = 0, sticky = 'W')

win_lose_draw = "win"

def clicked():
    wld = wld_var.get()
    global win_lose_draw
    win_lose_draw = wld
    return win_lose_draw

wld_var = StringVar()

win_button = Radiobutton(root, text = "Win", variable = wld_var, value = "win", command = clicked)
win_button.grid(row = 4, column = 1)
lose_button = Radiobutton(root, text = "Lose", variable = wld_var, value = "lose", command = clicked)
lose_button.grid(row = 5, column = 1)
draw_button = Radiobutton(root, text = "Draw", variable = wld_var, value = "draw", command = clicked)
draw_button.grid(row = 6, column = 1)

wld_var.set("Win")

# space
space = Label(text = "")
space.grid(row = 7, column = 0, columnspan = 2)

# home goals entry
home_goals_label = Label(text = "How many home goals?", font = ('', 10))
home_goals_label.grid(row = 8, column = 0, sticky = 'W')
home_goals_var = IntVar()
home_goals_entry = Entry(width = 30, borderwidth = 2, textvariable = home_goals_var)
home_goals_entry.grid(row = 8, column = 1, sticky = 'NSEW')

# away goals entry
away_goals_label = Label(text = "How many away goals?", font = ('', 10))
away_goals_label.grid(row = 9, column = 0, sticky = 'W')
away_goals_var = IntVar()
away_goals_entry = Entry(width = 30, borderwidth = 2, textvariable = away_goals_var)
away_goals_entry.grid(row = 9, column = 1, sticky = 'NSEW')

# space
space = Label(text = "")
space.grid(row = 10, column = 0, columnspan = 2)

# scorers
player_checkbox = ""
player_list = ["No Goalscorer", "Sargent", "Slimane", "Nunez", "Cordoba", "Gordon", "Springett", "Gibbs", "Crnac", "McLean", "Hernandez", "Hills", "Forson",
        "Duffy", "Sorensen", "Chrisene", "Myles", "Forsyth", "Sainz", "Doyle", "Marcondes", "Dobbin", "Jurasek", "Fisher", "Schwartau", "Stacey"
]
player_list_2 = player_list[1:]

first_scorer_label = Label(text = "first goalscorer or no goalscorer?", font = ('', 10))
first_scorer_label.grid(row = 11, column = 0, sticky = 'W')
first_scorer_combo = ttk.Combobox(root, values = player_list, state = "readonly")
first_scorer_combo.grid(row = 11, column = 1, sticky = 'NSEW')
first_scorer_combo.set("No Goalscorer")

second_scorer_label = Label(text = "Second goalscorer?", font = ('', 10))
second_scorer_label.grid(row = 12, column = 0, sticky = 'W')
second_scorer_combo = ttk.Combobox(root, values = player_list_2, state = "readonly")
second_scorer_combo.grid(row = 12, column = 1, sticky = 'NSEW')
second_scorer_combo.set("")

third_scorer_label = Label(text = "Third goalscorer?", font = ('', 10))
third_scorer_label.grid(row = 13, column = 0, sticky = 'W')
third_scorer_combo = ttk.Combobox(root, values = player_list_2, state = "readonly")
third_scorer_combo.grid(row = 13, column = 1, sticky = 'NSEW')
third_scorer_combo.set("")

fourth_scorer_label = Label(text = "Fourth goalscorer?", font = ('', 10))
fourth_scorer_label.grid(row = 14, column = 0, sticky = 'W')
fourth_scorer_combo = ttk.Combobox(root, values = player_list_2, state = "readonly")
fourth_scorer_combo.grid(row = 14, column = 1, sticky = 'NSEW')
fourth_scorer_combo.set("")

fifth_scorer_label = Label(text = "Fifth goalscorer?", font = ('', 10))
fifth_scorer_label.grid(row = 15, column = 0, sticky = 'W')
fifth_scorer_combo = ttk.Combobox(root, values = player_list_2, state = "readonly")
fifth_scorer_combo.grid(row = 15, column = 1, sticky = 'NSEW')
fifth_scorer_combo.set("")

sixth_scorer_label = Label(text = "Sixth goalscorer?", font = ('', 10))
sixth_scorer_label.grid(row = 16, column = 0, sticky = 'W')
sixth_scorer_combo = ttk.Combobox(root, values = player_list_2, state = "readonly")
sixth_scorer_combo.grid(row = 16, column = 1, sticky = 'NSEW')
sixth_scorer_combo.set("")

# save the data to variable on submit button click
def norwich_save_data():
    current_round = round_var.get()
    norwich_home_goals = home_goals_var.get()
    norwich_away_goals = away_goals_var.get()
    first_scorer = first_scorer_combo.get()
    first_scorer = first_scorer.lower()
    second_scorer = second_scorer_combo.get()
    second_scorer = second_scorer.lower()
    third_scorer = third_scorer_combo.get()
    third_scorer = third_scorer.lower()
    fourth_scorer = fourth_scorer_combo.get()
    fourth_scorer = fourth_scorer.lower()
    fifth_scorer = fifth_scorer_combo.get()
    fifth_scorer = fifth_scorer.lower()
    sixth_scorer = sixth_scorer_combo.get()
    sixth_scorer = sixth_scorer.lower()
    scorer_list = [first_scorer, second_scorer, third_scorer, fourth_scorer, fifth_scorer, sixth_scorer]

    # norwich dictionary
    norwich_dict = {
        "result" : win_lose_draw,
        "home_goals" : norwich_home_goals,
        "away_goals" : norwich_away_goals,
        "goal_scorer" : scorer_list
    }

    # convert to json
    with open(f'round_{current_round}_norwich.json', 'w') as ngw:
        json.dump(norwich_dict, ngw, indent = 2)


### buttons
button_submit = Button(root, text = "Submit", command = norwich_save_data)
button_submit.grid(pady = 10,row = 17, column = 0, sticky = 'NSEW')


root.mainloop()