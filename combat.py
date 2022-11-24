import random
import weapons as weapons
import enemies as en
import inventory as inventory

enemy = random.choice(list(en.enemies))
print("You have entered combat! Your opponent is " + enemy + "!")

