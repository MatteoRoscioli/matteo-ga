# 100 Health
# 100 Mana
# 30 Shield
#
#
# Spells:
#     Staff Bonk | 10 damage to one enemy | 0 mana
#     Lightning bolt | 20 damage to one enemy | 20 damage to all enemies if coated in water | 15 mana
#     Healing spell | Heals 10 health | 6 mana
#     Shield spell | Gives you 30 shield | 18 mana
#     Fireball | 100 damage to one enemy, 50 damage to player | 30 mana
#     Hydroball | 50 damage to one enemy | Coats area in water | 20 mana
import random

current_player_health = 100
current_player_mana = 100
current_player_shield = 0

player_spells_unlocked = [
    "Staff Bonk",
    "Flee!"
]

snapper_health = 50


# Snapper Moves:
#     Snap | 10 damage to player | 70%
#     Digest | 40 damage to player | 20%
#     Eat | Stuns the player so they can't run | 5 damage per turn | 10%

def print_moves():
    print("Moves:")
    c = 1
    for spell in player_spells_unlocked:
        print(str(c) + ") " + spell)
        c = c + 1


def print_player_health():
    print("Health: " + str(current_player_health))
    print("Mana: " + str(current_player_mana))


def print_snapper_health():
    print("Snapper Health: " + str(snapper_health))


player_being_eaten = 0
vine_whip = 0

def snapper_attack():
    global current_player_health
    global player_being_eaten
    attack_num = random.randint(1, 100)
    if attack_num <= 70:
        print("The Snapper snaps at you!")
        current_player_health -= 10
    elif attack_num <= 90:
        print("The Snapper digests you!")
        current_player_health -= 40
    else:
        print("The Snapper eats you!")
        current_player_health -= 5
        player_being_eaten += 1


def piclops_attack():
    global current_player_health
    global player_being_eaten
    attack_num = random.randint(1, 100)
    if attack_num <= 70:
        print("The dreaded pi-clops pokes at you with his dagger!")
        current_player_health -= 10
    elif attack_num <= 90:
        print("The pi-clops throws his hook at you!")
        current_player_health -= 35
    else:
        print("The pi-clops boomerangs his hat at you, hitting you will all three points! Critical hit!")
        current_player_health -= 90

def polty_attack():
    global current_player_health
    global player_being_eaten
    attack_num = random.randint(1, 100)
    if attack_num <= 70:
        print("The Poltergeist lifts you in the air and throws you on the ground! Critical hit!")
        current_player_health -= 20
    elif attack_num <= 90:
        print("The Poltergeist throws you out the window, sending glass shards EVERYWHERE!")
        current_player_health -= 40
    else:
        print("The Poltergeist uses a spell on you so strong it kills you! The end.....")
        current_player_health -= 90


def damage_player_tick():
    global current_player_health
    if player_being_eaten:
        damage = 5 * player_being_eaten
        print("You take " + str(damage) + " damage from being eaten!")
        current_player_health -= damage


def moms_letter():
    print("Dear Player,\n",
          "You are a failure.\n",
          "Love, Mom")


def check_player_death():
    global current_player_health
    if current_player_health <= 0:
        print("You died! You are a failure.")
        exit()


print("You've encountered a Snapper! What do you do?")
print_moves()
while snapper_health > 0:
    print_player_health()
    print_snapper_health()
    choice = input("Enter your choice: ")
    if choice == '1':
        print("You use Staff Bonk on the Snapper!")
        snapper_health = snapper_health - 10
    if choice == '2':
        print(
            "You fled... you've been crowned as the village coward. Mom is VERY disappointed in you. Here is a letter from her:")
        moms_letter()
        exit()
    snapper_attack()
    damage_player_tick()
    check_player_death()

print("Congratulations. You defeated the snapper with a stick... what's your problem???")

print("The viney, earthy stone has been added to your staff.. new ability unlocked: Vine Whip!")
player_spells_unlocked.append("Vine Whip")

print("You walk down the road.. towards the beach... you see a mysterious figure in the distance...")
print("YOU HAVE ENCOUNTERED THE DREADED PIRATE PI-CLOPS!!")

polty_health = 110

while polty_health > 0:
    print_player_health()
    print("Pirate Pi-Clops Health: " + str(polty_health))
    print_moves()
    choice = input("Enter your choice: ")
    if choice == '1':
        print("You use Staff Bonk on Pirate Pi-Clops!")
        polty_health = polty_health - 10
    if choice == '3':
        if current_player_mana < 15:
            print("You don't have enough mana!")
            continue
        print("You use Vine Whip on Pirate Pi-Clops!")
        polty_health = polty_health - 30
        vine_whip += 1
        current_player_mana -= 15
    if choice == '2':
        print(
            "You fled... you've been crowned as the village coward. Mom is VERY disappointed in you. Here is a letter from her:")
        moms_letter()
        exit()
    if vine_whip >= 1:
        print("The pi-clops is stunned by the vine whip!")
        vine_whip -= 1
    else:
        piclops_attack()
    damage_player_tick()
    check_player_death()
print("You defeated the pi-clops. His HEART falls out of his chest! You pick it up and it fuses with your staff.... health increased!")
print("You've gained 50 health!")
current_player_health += 50
print("Congratulations. You have found a mysterious ball of sand... you crack it open with your vine staff, and you see... a hydroball! New ability unlocked!")
print("You've unlocked the ability: Hydroball!")

player_spells_unlocked.append("Hydroball")

print("Moving on, you start walking along the path. It starts raining, but there is a mansion in the distance. You take shelter there. But all of a sudden, strange things start happening....")

print("The world starts swirling around you... You hear wailing... An almighty lightning bolt crashes down...")
print("YOU HAVE ENCOUNTERED THE FEARED POLTERGEIST!!")

polty_health = 150

while polty_health > 0:
    print_player_health()
    print("Pirate Poltergeist Health: " + str(polty_health))
    print_moves()
    choice = input("Enter your choice: ")
    if choice == '1':
        print("You use Staff Bonk on the Poltergeist!")
        polty_health = polty_health - 10
    if choice == '3':
        if current_player_mana < 15:
            print("You don't have enough mana!")
            continue
        print("You use Vine Whip on Poltergeist!")
        polty_health = polty_health - 30
        vine_whip += 1
        current_player_mana -= 15
    if choice == '2':
        print(
            "You fled... you've been crowned as the village coward. Mom is VERY disappointed in you. Here is a letter from her:")
        moms_letter()
        exit()
    if vine_whip >= 1:
        print("The Poltergeist is stunned by the Vine Whip!")
        vine_whip -= 1
    else:
        piclops_attack()
    damage_player_tick()
    check_player_death()
print("You defeated the Poltergeist! He drops something. You pick it up and you recover ALL of your health!!!")
current_player_health += 100
print("Congratulations. You have uncovered a strange artifact... you accidently drop it. It breaks and you get a new spell! New ability unlocked!")
print("You've unlocked the ability: Psychic!")

player_spells_unlocked.append("Psychic")
print("What happens next? The answer, as the journey continues!!!")