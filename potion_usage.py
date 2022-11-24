# testing
import random
from collections import defaultdict
import inventory as inv

# variable for loop
loop_health = True
loop_staminia = True

# stats to be effected by potions
player_stats = {"staminia": 0, "health": 0}

item1 = "health potion"
item2 = "staminia potion"

random = random.choice(["item1", "item2"])

# adds 10 health to the user stats
if random == "item1":
    while loop_health == True:
        if inv.inventory.count("item1") < 1:
            print("you do not have any more potion(s) to consume")
            loop_health = False
        else:
            use = input("use {}?\n".format(item1))
            if use.lower() in ["yes", "y", "yep"]:
                player_stats["health"] += 10
                print("uses {}".format(item1))
                print(player_stats)
                inv.inventory.remove("item1")
                if inv.inventory.count("item1") >= 1:
                    repeat = input("use another health potion?\n")
                    if repeat.lower() in ["no", "n", "nope"]:
                        print("process ended")
                        loop_health = False
                    elif repeat.lower() in ["yes", "y", "yep"]:
                        print("potion menu reloaded")
                    else:
                        print("you have selected an incorrect value")
            elif use.lower() in ["no", "n", "nope"]:
                print("process ended")
                loop_health = False
            else:
                print("incorrect value, try again")

# adds 10 stamina (staminia) to the user stats
if random == "item2":
    while loop_staminia == True:
        if inv.inventory.count("item2") < 1:
            print("you do not have any more potion(s) to consume")
            loop_staminia = False
        else:
            use = input("use {}?\n".format(item2))
            if use.lower() in ["yes", "y", "yep"]:
                player_stats["staminia"] += 10
                print("uses {}".format(item2))
                print(player_stats)
                inv.inventory.remove("item2")
                if inv.inventory.count("item2") >= 1:
                    repeat = input("use another staminia potion?\n")
                    if repeat.lower() in ["no", "n", "nope"]:
                        print("process ended")
                        loop_staminia = False
                    elif repeat.lower() in ["yes", "y", "yep"]:
                        print("potion menu reloaded")
                    else:
                        print("you have selected an incorrect value")
            elif use.lower() in ["no", "n", "nope"]:
                print("process ended")
                loop_staminia = False
            else:
                print("incorrect value, try again")

print(player_stats)