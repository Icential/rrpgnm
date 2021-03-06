import random, os, sys, time, json

# Generic breakline output function
def br(): print("=============================================================================================")

# (ERROR) Generic retry alert function
def retry(): 
    print("Invalid answer please try again")
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Random name generator based of items in names folder function
def create_name():
    rng = random.randint(1, 2)
    if rng == 1:
        prerng = random.randint(0, len(pre) - 1)
        sufrng = random.randint(0, len(suf) - 1)
        name = pre[prerng] + suf[sufrng]
    elif rng == 2:
        adjrng = random.randint(0, len(adj) - 1)
        objrng = random.randint(0, len(obj) - 1)
        name = adj[adjrng] + " " + obj[objrng]
    rng0 = random.randint(1, 2)
    if rng0 == 1: return name
    elif rng0 == 2: return "The " + name

# Random array index picker function
def rng_arr(foo): return(foo[random.randint(0, len(foo) - 1)])

# Random damage picker based of weapon tier function
def new_dmg(tier):
    if tier == "Unique": return rng_arr(list(range(1, 26)))
    elif tier == "Rare": return rng_arr(list(range(26, 51)))
    elif tier == "Legendary": return rng_arr(list(range(51, 76)))
    elif tier == "Mythical": return rng_arr(list(range(76, 101)))

# Random damage type algorithm sorter function
def new_dmg():
    rng = random.randint(1, 4)
    if rng == 1: return rng_arr(damagetypes)
    elif rng == 2:
        dmg1, dmg2 = rng_arr(damagetypes), rng_arr(damagetypes)
        if dmg1 == dmg2: return new_dmg()
        else: return [dmg1, dmg2]
    elif rng == 3:
        dmg1, dmg2, dmg3 = rng_arr(damagetypes), rng_arr(damagetypes), rng_arr(damagetypes)
        if dmg1 == dmg2 or dmg1 == dmg3 or dmg2 == dmg3: return new_dmg()
        else: return [dmg1, dmg2, dmg3]
    elif rng == 4:
        dmg1, dmg2, dmg3, dmg4 = rng_arr(damagetypes), rng_arr(damagetypes), rng_arr(damagetypes), rng_arr(damagetypes)
        if dmg1 == dmg2 or dmg1 == dmg3 or dmg1 == dmg4 or dmg2 == dmg3 or dmg2 == dmg4 or dmg3 == dmg4: return new_dmg()
        else: return [dmg1, dmg2, dmg3, dmg4]

# Random weapon JSON creating function
def wjson(i, x):
    f = open("w" + str(i + 1) + ".json", "w")
    name = create_name()
    tier = rng_arr(tiers)
    j = {
        "name": name,
        "tier": tier,
        "type": rng_arr(types),
        "tradeable": rng_arr([True, False]),
        "damage": {
            "value": new_dmg(tier),
            "types": new_dmg()
        },
        "attackspeed": rng_arr(attackspeed)
    }
    js = json.dumps(j, indent=4)
    f.write(js)
    if x == 0: print("Ding ding! A new item has been created! (" + name + ")") 
    else: None


# Global objects
# Prefixes
with open("names/pre.txt") as f:
    pre = f.read().splitlines()
# Suffixes
with open("names/suf.txt") as f:
    suf = f.read().splitlines()
# Adjectives
with open("names/adj.txt") as f:
    adj = f.read().splitlines()
# Objects
with open("names/obj.txt") as f:
    obj = f.read().splitlines()
# Et cetera
tiers = ["Unique", "Rare", "Legendary", "Mythical"]
types = ["Staff", "Wand", "Foci", "Longsword", "Sword", "Greatbow", "Shortbow", "Mace", "Dagger", "Axe", "Pistol", "Rifle", "Spear", "Relic", "Rifle"]
damagetypes = ["Dark", "Light", "Physical", "Arcane", "Air", "Lightning", "Fire", "Water", "Air"]
attackspeed = ["Sluggish", "Slow", "Normal", "Fast", "Rapid"]


# Main
br()
# Startup message
print("What would you like to do? (Enter \"help\" for list of commands)")
br()
input = input().lower()
br()

# Help command
if input == "help":
    print(
        "List of commands:\n\n"
        "help| What you're seeing right now\n"
        "chance| Calculates the chance of a single name to be generated\n"
        "pre| Lists all the prefixes\n"
        "suf| Lists all the suffixes\n"
        "adj| Lists all the adjectives\n"
        "obj| lists all the objects/nouns\n"
        "fi| Create i new JSON file with randomly generated weapon specifications. If it's onlt f, create 1 JSON file\n"
        "r| Read the JSON file created beforehand\n"
        "ni| Creates multiple randomly generated names i times (Ex. n10, n9, n45). If it's only n, then 10 randomly generated names are created 10 times"
    )
    br()

# Names commands
elif input == "pre": 
    print(pre)
elif input == "suf": 
    print(suf)
elif input == "adj":
     print(adj)
elif input == "obj": 
    print(obj)

# Chance command (Shows the chance of one weapon name being created)
elif input == "chance":
    all = 4 * len(pre) * len(suf) * len(adj) * len(obj)
    chance = 1 / all
    print("Each name has a " + str(round(chance, 10)) + "% of being created! (1 in " + str(all) + ")")

# F command (Creates random JSON weapon files as many times you want)
elif input.startswith("f"):
    i = input.split("f", 1)[1]
    if i == "" or i == "1": print("Creating a new weapon item JSON...")
    else: print("Creating " + str(i) + " new weapon item JSONs...")
    if input == "f": wjson(1, 0)
    elif int(i) > 0 and int(i) < 101:
        names = ""
        for x in range(int(i)):
            wjson(x, 1)
            f = open("w" + str(x + 1) + ".json", "r").read()
            jsload = json.loads(f)
            names += jsload["name"] + ", "
        print("Ding ding! " + str(i) + " new items created! (" + names[:-2] + ")")
    else: print(i + " is too many generations!")

# (INCOMPLETE) R commands (Reads the JSON file(s))
elif input == "r":
    f = open("w1.json", "r").read()
    jsload = json.loads(f)
    print(
        "Weapon Name: " + jsload["name"] + "\n"
        "Weapon Tier: " + jsload["tier"] + "\n"
        "Weapon Type: " + jsload["type"] + "\n"
        "Tradeable: " + str(jsload["tradeable"]) + "\n"
        # "Damage Value: " + jsload["damage[value]"] + "\n"
        # "Damage Type(s): " + jsload["damage[types]"] + "\n"

    )
    br()

# N command (Creates random weapon names as many as you like)
elif input.startswith("n"):
    times = input.split("n", 1)[1]
    names = ""
    if times == "":
        for n in range(10):
            names += create_name() + ", "
        print(names[:-2])
    elif int(times) > 0 and int(times) < 101:
        for n in range(int(times)):
            names += create_name() + ", "
        print(names[:-2])
    else: print(times + " times is too many times!")
else: retry()