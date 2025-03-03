namesDictionary= {
"alec": "Alec Burt",
"ArmyAmarillo": "Alec Burt",
"ari": "Ari Ordeix",
"simon": "Simon Furness",
"dad": "Norrie Burt"
}

def check_name(name):
    if name in namesDictionary:
        return namesDictionary[name]
    else:
        return name
