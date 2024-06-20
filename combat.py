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
#     Waterball | 50 damage to one enemy | Coats area in water | 20 mana
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


def print_snapper_health():
    print("Snapper Health: " + str(snapper_health))


player_being_eaten = 0


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


def damage_player_tick():
    global current_player_health
    if player_being_eaten:
        damage = 5 * player_being_eaten
        print("You take " + str(damage) + " damage from being eaten!")
        current_player_health -= damage


def moms_letter():
    print("Dear player,\n",
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