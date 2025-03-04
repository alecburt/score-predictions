import json

""" Update the names each round. For the first week a blank dictionary is needed with just empty curly brackets in JSON."""

with open(f'formatted_names.json', 'r') as names_json:
    names_dict = json.load(names_json)
    

def format_name(name):
    """In player_input_tk this takes the input name and if it is not in the formatted_names.json dictionary 
    it will prompt to add the formatted name and add it to the dictionary"""
    if name in names_dict:
        return names_dict[name]
    else:
        print(f"{name} is not in the system!")
        formatted_name = input("What is the formatted name? ")
        names_dict.update({name: formatted_name})
        with open(f'formatted_names.json', 'w') as ngw:
            json.dump(names_dict, ngw, indent = 2)
        return formatted_name


def check_name(name):
    if name in names_dict:
        return names_dict[name]
    else:
        return name
