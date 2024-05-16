# Ship Class Assignment

# Instructions:
# 1. Fill in the missing code sections indicated by comments.
# 2. Implement a program that defines a Ship class with different weapons, each having fire rates and damage.
# 3. Test your program with different input values to ensure correctness.


# Section 1: Define a class called 'Ship' with the following attributes:
# - name (string): The name of the ship.
# - speed (integer): The speed of the ship in units per second.
# - weapons (dictionary): A dictionary containing weapons as keys and their attributes as values.
class Ship:
    def __init__(self, name, speed, weapons):
        self.name = name
        self.speed = speed
        self.weapons = weapons
        print(self.name, self.speed, self.weapons)
    # Define a method called 'fire_weapon' that takes the weapon name as input.
    # This method should print a message indicating the weapon firing with its fire rate and damage.
    def fire_weapon(self, weapon_name):
        self.weapon_name = weapon_name
        print(self.weapon_name)

# Section 2: Define a function called 'main' which will be the entry point of your program.
# Inside this function, create an instance of the Ship class with different weapons.
# Test the fire_weapon method with different weapons.
def main():
    # Define weapons with their attributes (fire rate and damage)
    weapons = {
        "Laser": {"fire_rate": 2, "damage": 10},
        "Missile": {"fire_rate": 1, "damage": 50},
        "Plasma Cannon": {"fire_rate": 3, "damage": 30},
    }

    # Create an instance of the Ship class with the defined weapons
    ship = Ship("the Flamerod", 500, weapons)
    pass
    # Test the fire_weapon method with different weapons
    ship.fire_weapon("Laser")
    ship.fire_weapon("Missile")
    ship.fire_weapon("Plasma Cannon")


# Call the main function to run the program
if __name__ == "__main__":
    main()
