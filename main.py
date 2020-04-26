import random
import time

monsters = {
    "dragon": {
        "name": "dragon",
        "life": 100,
        "attack": [15, 45],
        "defense": [15, 25]
    },
    "shark": {
        "name": "shark",
        "life": 80,
        "attack": [20, 35],
        "defense": [20, 25]
    },
    "bear": {
        "name": "bear",
        "life": 110,
        "attack": [25, 45],
        "defense": [5, 30] 
    },
    "zombie": {
        "name": "zombie",
        "life": 30,
        "attack": [25,30],
        "defense": [1, 10]
    },
    "skeleton": {
        "name": "skeleton",
        "life": 70,
        "attack": [30, 40],
        "defense": [10, 15]
    }
}

monsters_list = []
for a in monsters:
    monsters_list.append(a)

def attack(monster):

    global monsters

    monster = monsters[str(monster)]
    point1 = monster["attack"][0]
    point2 = monster["attack"][1]

    attack = random.choice(range(point1, point2))

    return attack

def defense(monster):

    global monsters

    monster = monsters[str(monster)]
    point1 = monster["defense"][0]
    point2 = monster["defense"][1]

    defense = random.choice(range(point1, point2))

    return defense

list = ""
for a in monsters:
    list += f"- {a} | {monsters[a]['life']}HP | {monsters[a]['attack'][0]} to {monsters[a]['attack'][1]} attack | {monsters[a]['defense'][0]} to {monsters[a]['defense'][1]} defense\n"

pass_ = False

while not pass_:
    monster_ask = input(f"Choose a monster from this list:\n{list}")
    try:
        monster = monsters[monster_ask.lower()]
        pass_ = True
    except KeyError:
        print("Not a valid monster, retry!")
        pass_ = False

monster_life = int(monster["life"])
monster_pc = monsters[str(random.choice(monsters_list))]
monster_pc_life = int(monster_pc["life"])

time.sleep(1)
print("Let's Start!")

# turn = "player" <-- will add this in multiplayer mod

end = False

while not end:
    
    time.sleep(1)
    print(f"""
[you] {monster['name']}'s life: {monster_life}HP
[pc] {monster_pc['name']}'s life: {monster_pc_life}HP

What do you want to do?

- Attack
- Defense

(reply)
""")
    pass_ = False
    while not pass_:
        response = input("\n")

        if response.lower() == "attack":    
            pass_ = True

        elif response.lower() == "defense":
            pass_ = True

        else:
            print("Not a valid action. Re-Type.")
            pass_ = False
    
    if response.lower() == "attack":
        a = attack(monster["name"])    
        monster_pc_life -= int(a)
        print(f"[you] {monster['name']} attacked [pc] {monster_pc['name']} who lost {a}HP")

    elif response.lower() == "defense":
        b = defense(monster["name"])
        monster_life += int(b)
        print(f"[you] {monster['name']} increased his life of {b}HP!")

    if monster_life <= 0:
        print(f"GAME OVER!\n[pc] {monster_pc['name']} Won! Re-Try, you'll be like next time!")
        end = True
        break

    elif monster_pc_life <= 0:
        print(f"GAME OVER!\n[you] {monster['name']} Won! GG!")
        end = True
        break

    else:
        pass

    time.sleep(1)
    print(f"""
[you] {monster['name']}'s life: {monster_life}HP
[pc] {monster_pc['name']}'s life: {monster_pc_life}HP    
""")

    time.sleep(1)
    print("It's my turn!")

    r = random.choice(["attack", "defense"])

    if r == "attack":
        a = attack(monster_pc["name"])    
        monster_life -= int(a)
        print(f"[pc] {monster_pc['name']} attacked [you] {monster['name']} who lost {a}HP")

    elif r == "defense":
        b = defense(monster_pc["name"])
        monster_pc_life += int(b)
        print(f"[pc] {monster_pc['name']} increased his life of {b}HP!")

    if monster_life <= 0:
        print(f"GAME OVER!\n[pc] {monster_pc['name']} Won! Re-Try, you'll be like next time!")
        end = True
        break

    elif monster_pc_life <= 0:
        print(f"GAME OVER!\n[you] {monster['name']} Won! GG!")
        end = True
        break

    else:
        pass
    