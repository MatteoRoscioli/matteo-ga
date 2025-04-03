import random
import time

class AdventureGame:
    def __init__(self):
        self.player = {
            "name": "",
            "health": 100,
            "max_health": 100,
            "inventory": [],
            "gold": 0,
            "equipped_weapon": None
        }
        
        # Dungeon rooms
        self.dungeon_rooms = {
            "entrance": {
                "description": "You stand at the entrance of a dark dungeon. Torches flicker on the walls.",
                "connections": ["hallway", "outside_cave"],
                "items": ["torch"],
                "enemies": []
            },
            "hallway": {
                "description": "A long hallway stretches before you. The floor is dusty with footprints.",
                "connections": ["entrance", "treasure_room", "monster_den"],
                "items": ["rusty_key"],
                "enemies": ["goblin"]
            },
            "treasure_room": {
                "description": "Glittering gold and jewels line the walls of this small chamber.",
                "connections": ["hallway", "exit"],
                "items": ["golden_chalice", "jeweled_sword"],
                "enemies": ["skeleton"]
            },
            "monster_den": {
                "description": "The stench of something foul fills this cavern. Bones litter the floor.",
                "connections": ["hallway"],
                "items": ["healing_potion"],
                "enemies": ["troll"]
            },
            "exit": {
                "description": "Daylight streams in from an opening in the ceiling. A natural staircase leads upward.",
                "connections": ["treasure_room", "outside_cave"],
                "items": [],
                "enemies": []
            }
        }
        
        # Outside world locations
        self.outside_rooms = {
            "outside_cave": {
                "description": "You stand outside a dark cave entrance. A dense forest surrounds you, and birds chirp in the trees.",
                "connections": ["entrance", "forest_path", "mountain_trail"],
                "items": ["berry_bush"],
                "enemies": []
            },
            "forest_path": {
                "description": "A winding path leads through the ancient forest. Sunlight filters through the canopy.",
                "connections": ["outside_cave", "clearing", "river_crossing"],
                "items": ["wild_herbs"],
                "enemies": ["wolf"]
            },
            "clearing": {
                "description": "A peaceful clearing in the forest. Wildflowers bloom and a small pond reflects the sky.",
                "connections": ["forest_path", "old_cabin"],
                "items": ["fishing_rod"],
                "enemies": []
            },
            "river_crossing": {
                "description": "A wide river blocks your path. A rickety bridge offers a way across.",
                "connections": ["forest_path", "village_outskirts"],
                "items": [],
                "enemies": ["river_troll"]
            },
            "old_cabin": {
                "description": "An abandoned woodcutter's cabin stands in the clearing. It looks weathered but intact.",
                "connections": ["clearing"],
                "items": ["woodcutter_axe", "old_map"],
                "enemies": ["ghost"]
            },
            "mountain_trail": {
                "description": "A steep trail winds up the mountainside. The view of the surrounding lands is breathtaking.",
                "connections": ["outside_cave", "mountain_peak"],
                "items": ["climbing_rope"],
                "enemies": ["mountain_lion"]
            },
            "mountain_peak": {
                "description": "The windswept peak offers a panoramic view of the entire region. You can see for miles in every direction.",
                "connections": ["mountain_trail"],
                "items": ["eagle_feather"],
                "enemies": ["ice_elemental"]
            },
            "village_outskirts": {
                "description": "The edge of a small village. Simple houses with thatched roofs line the dirt road.",
                "connections": ["river_crossing", "village_square"],
                "items": [],
                "enemies": []
            },
            "village_square": {
                "description": "The heart of the village. Villagers go about their business, and a market sells various goods.",
                "connections": ["village_outskirts", "tavern", "blacksmith"],
                "items": [],
                "enemies": []
            },
            "tavern": {
                "description": "A cozy tavern filled with the aroma of food and sound of laughter. A good place to rest and gather information.",
                "connections": ["village_square"],
                "items": [],
                "enemies": []
            },
            "blacksmith": {
                "description": "The village blacksmith's shop. The sound of hammering metal and the heat of the forge greet you.",
                "connections": ["village_square"],
                "items": ["steel_shield"],
                "enemies": []
            }
        }
        
        # Combine all rooms
        self.rooms = {**self.dungeon_rooms, **self.outside_rooms}
        
        # All enemies
        self.enemies = {
            # Dungeon enemies
            "goblin": {"health": 30, "damage": 10, "description": "A small, green creature with sharp teeth"},
            "skeleton": {"health": 40, "damage": 15, "description": "A walking pile of bones wielding a rusty sword"},
            "troll": {"health": 80, "damage": 25, "description": "A massive, ugly brute with bulging muscles"},
            
            # Outside world enemies
            "wolf": {"health": 35, "damage": 12, "description": "A fierce wild wolf with gleaming teeth"},
            "river_troll": {"health": 70, "damage": 20, "description": "A slimy troll that lurks beneath the bridge"},
            "ghost": {"health": 45, "damage": 15, "description": "A translucent apparition that moans eerily"},
            "mountain_lion": {"health": 50, "damage": 18, "description": "A sleek predator with sharp claws"},
            "ice_elemental": {"health": 90, "damage": 25, "description": "A swirling mass of ice and snow in vaguely humanoid form"}
        }
        
        # All items
        self.items = {
            # Dungeon items
            "torch": "A flickering torch that provides light",
            "rusty_key": "An old key, possibly opening something important",
            "golden_chalice": "A valuable cup made of solid gold",
            "jeweled_sword": "A magnificent sword adorned with precious gems",
            "healing_potion": "A red liquid that restores health",
            
            # Outside world items
            "berry_bush": "A bush with sweet, edible berries that provide a small health boost",
            "wild_herbs": "Medicinal herbs that can be used to create healing remedies",
            "fishing_rod": "A simple rod for catching fish from ponds or rivers",
            "woodcutter_axe": "A sturdy axe useful for chopping wood or as a weapon",
            "old_map": "A weathered map showing points of interest in the region",
            "climbing_rope": "A strong rope useful for scaling cliffs or steep inclines",
            "eagle_feather": "A beautiful feather with possible magical properties",
            "steel_shield": "A well-crafted shield that reduces damage in combat"
        }
        
        # Weapons with damage bonus
        self.weapons = {
            "jeweled_sword": 15,
            "woodcutter_axe": 10
        }
        
        # Armor/shields with damage reduction
        self.armor = {
            "steel_shield": 5
        }
        
        # Character status trackers
        self.has_visited_village = False
        self.has_completed_dungeon = False
        self.dungeon_enemies_defeated = 0
        self.total_enemies_defeated = 0
        
        self.current_room = "entrance"
        self.game_over = False
        
    def start_game(self):
        print("\n" + "=" * 50)
        print("WELCOME TO THE EXPANDED ADVENTURE!")
        print("=" * 50)
        
        self.player["name"] = input("\nWhat is your name, brave adventurer? ")
        print(f"\nWelcome, {self.player['name']}! Your adventure begins now...")
        
        while not self.game_over:
            self.display_room()
            command = input("\nWhat would you like to do? ").lower().strip()
            self.process_command(command)
            
    def display_room(self):
        room = self.rooms[self.current_room]
        print("\n" + "-" * 50)
        print(f"Location: {self.current_room.replace('_', ' ').title()}")
        print(room["description"])
        
        if room["items"]:
            print("You see:", ", ".join(item.replace("_", " ") for item in room["items"]))
            
        if room["enemies"]:
            for enemy in room["enemies"]:
                print(f"A {enemy.replace('_', ' ')} is here! {self.enemies[enemy]['description']}.")
                
        print(f"Exits: {', '.join(exit.replace('_', ' ').title() for exit in room['connections'])}")
        print(f"Health: {self.player['health']}/{self.player['max_health']}  Gold: {self.player['gold']}")
        
        if self.player["inventory"]:
            print(f"Inventory: {', '.join(item.replace('_', ' ') for item in self.player['inventory'])}")
            
        if self.player["equipped_weapon"]:
            print(f"Equipped: {self.player['equipped_weapon'].replace('_', ' ')}")
            
    def process_command(self, command):
        if command == "quit":
            self.game_over = True
            print("\nThanks for playing! Goodbye.")
            return
            
        if command == "help":
            self.display_help()
            return
            
        command_parts = command.split()
        
        if not command_parts:
            print("Please enter a command.")
            return
            
        action = command_parts[0]
        
        if action == "go":
            if len(command_parts) < 2:
                print("Go where? Try 'go [location]'")
                return
                
            location = " ".join(command_parts[1:]).lower()
            
            # Handle "go to X" format
            if location.startswith("to "):
                location = location[3:]
                
            # Convert spaces to underscores for matching
            location_key = location.replace(" ", "_")
            
            # Check for partial matches
            matched_connection = None
            for connection in self.rooms[self.current_room]["connections"]:
                if location_key == connection or location in connection.replace("_", " "):
                    matched_connection = connection
                    break
                    
            if matched_connection:
                # Check if there are enemies in the current room
                if self.rooms[self.current_room]["enemies"] and matched_connection != "entrance" and matched_connection != "outside_cave":
                    print("You can't leave while enemies are present!")
                    return
                    
                # Special case for the exit to outside world
                if self.current_room == "exit" and matched_connection == "outside_cave":
                    if "golden_chalice" in self.player["inventory"] and not self.has_completed_dungeon:
                        self.has_completed_dungeon = True
                        print("\n" + "=" * 50)
                        print("CONGRATULATIONS!")
                        print(f"{self.player['name']}, you have escaped the dungeon with the golden chalice!")
                        print("You now can explore the wider world beyond the dungeon.")
                        print("=" * 50)
                        self.dungeon_enemies_defeated = self.total_enemies_defeated
                        
                # Now move to the new room
                self.current_room = matched_connection
                
                # Special descriptions for first-time visits
                if matched_connection == "outside_cave" and not self.has_visited_village:
                    print("\nAs you step outside the cave, the fresh air fills your lungs.")
                    print("The world is vast and full of possibilities. Adventure awaits!")
                
                if matched_connection == "village_square" and not self.has_visited_village:
                    self.has_visited_village = True
                    print("\nThe villagers look at you with curiosity. One approaches:")
                    print("'Welcome, traveler! Our village is small but friendly. Feel free to explore.'")
                
                return
                    
            print(f"You can't go to '{location}' from here.")
            
        elif action == "take" or action == "get":
            if len(command_parts) < 2:
                print("Take what? Try 'take [item]'")
                return
                
            item = " ".join(command_parts[1:]).lower()
            
            # Handle "take the X" format
            if item.startswith("the "):
                item = item[4:]
                
            # Convert to item key format
            item_key = item.replace(" ", "_")
            
            for room_item in self.rooms[self.current_room]["items"]:
                if item_key == room_item or item in room_item.replace("_", " "):
                    self.player["inventory"].append(room_item)
                    self.rooms[self.current_room]["items"].remove(room_item)
                    print(f"You picked up the {room_item.replace('_', ' ')}.")
                    
                    # Special item effects
                    if room_item == "golden_chalice":
                        gold_value = random.randint(30, 80)
                        self.player["gold"] += gold_value
                        print(f"The chalice contained {gold_value} gold coins!")
                    elif room_item == "healing_potion":
                        self.player["inventory"].remove(room_item)  # Remove and use immediately
                        health_restored = random.randint(30, 50)
                        self.player["health"] = min(self.player["max_health"], self.player["health"] + health_restored)
                        print(f"You drink the healing potion. Health restored by {health_restored} points.")
                    elif room_item == "berry_bush":
                        self.player["inventory"].remove(room_item)  # Remove and use immediately
                        health_restored = random.randint(5, 15)
                        self.player["health"] = min(self.player["max_health"], self.player["health"] + health_restored)
                        print(f"You eat some berries from the bush. Health restored by {health_restored} points.")
                    elif room_item == "old_map":
                        print("The map reveals the locations of the village, mountain peak, and a mysterious X marking something beyond the river.")
                        
                    # Auto-equip weapons if nothing is equipped
                    if room_item in self.weapons and not self.player["equipped_weapon"]:
                        self.player["equipped_weapon"] = room_item
                        print(f"You equip the {room_item.replace('_', ' ')}.")
                        
                    return
                    
            print(f"There's no '{item}' here to take.")
            
        elif action == "fight" or action == "attack":
            if len(command_parts) < 2:
                print("Attack what? Try 'attack [enemy]'")
                return
                
            enemy = " ".join(command_parts[1:]).lower()
            
            # Convert to enemy key format
            enemy_key = enemy.replace(" ", "_")
            
            for room_enemy in self.rooms[self.current_room]["enemies"]:
                if enemy_key == room_enemy or enemy in room_enemy.replace("_", " "):
                    self.fight(room_enemy)
                    return
                    
            print(f"There's no '{enemy}' here to fight.")
            
        elif action == "look":
            # Just redisplay the room
            return
            
        elif action == "use":
            if len(command_parts) < 2:
                print("Use what? Try 'use [item]'")
                return
                
            item = " ".join(command_parts[1:]).lower()
            item_key = item.replace(" ", "_")
            
            for inv_item in self.player["inventory"]:
                if item_key == inv_item or item in inv_item.replace("_", " "):
                    if inv_item == "healing_potion":
                        health_restored = random.randint(30, 50)
                        self.player["health"] = min(self.player["max_health"], self.player["health"] + health_restored)
                        self.player["inventory"].remove(inv_item)
                        print(f"You drink the healing potion. Health restored by {health_restored} points.")
                    elif inv_item == "torch":
                        print("You hold the torch high, illuminating the dark corners of the room.")
                        if self.current_room in ["entrance", "hallway", "treasure_room", "monster_den"]:
                            print("The flickering light reveals ancient inscriptions on the walls.")
                    elif inv_item == "fishing_rod" and self.current_room in ["clearing", "river_crossing"]:
                        success = random.random() > 0.5
                        if success:
                            self.player["inventory"].append("fresh_fish")
                            print("You caught a fish! This could be useful for food later.")
                        else:
                            print("No luck with fishing right now.")
                    elif inv_item == "old_map":
                        print("You study the old map carefully.")
                        print("It shows: the mountain peak to the north, the village to the east,")
                        print("and marks a mysterious X beyond the river. Could be treasure!")
                    else:
                        print(f"You're not sure how to use the {inv_item.replace('_', ' ')} right now.")
                    return
                    
            print(f"You don't have a '{item}' to use.")
            
        elif action == "equip":
            if len(command_parts) < 2:
                print("Equip what? Try 'equip [weapon/armor]'")
                return
                
            item = " ".join(command_parts[1:]).lower()
            item_key = item.replace(" ", "_")
            
            for inv_item in self.player["inventory"]:
                if item_key == inv_item or item in inv_item.replace("_", " "):
                    if inv_item in self.weapons:
                        self.player["equipped_weapon"] = inv_item
                        print(f"You equip the {inv_item.replace('_', ' ')}.")
                    elif inv_item in self.armor:
                        self.player["equipped_armor"] = inv_item
                        print(f"You equip the {inv_item.replace('_', ' ')}.")
                    else:
                        print(f"You can't equip the {inv_item.replace('_', ' ')}.")
                    return
                    
            print(f"You don't have a '{item}' to equip.")
            
        elif action == "talk" and len(command_parts) > 1:
            location = self.current_room
            
            if location == "tavern":
                print("\nThe tavern keeper leans over the bar:")
                print("'Heard rumors of treasure in these parts. They say a golden chalice")
                print("from the old dungeon is worth a fortune to the right buyer.'")
                
            elif location == "village_square":
                print("\nAn old villager approaches you:")
                print("'Beware the mountain peak, traveler. They say an ice elemental")
                print("has made its home there. Only the bravest dare to climb that high.'")
                
            elif location == "blacksmith":
                print("\nThe blacksmith looks up from his work:")
                print("'Need a weapon or armor? I can sell you some, or upgrade what you have.")
                print("Just bring me materials and coin, and I'll see what I can do.'")
                
            else:
                print("There's no one here to talk to.")
                
        elif action in ["rest", "sleep"]:
            if self.current_room in ["tavern", "old_cabin", "clearing"]:
                print("You take some time to rest and recover your strength.")
                health_restored = min(self.player["max_health"] - self.player["health"], 30)
                if health_restored > 0:
                    self.player["health"] += health_restored
                    print(f"You've recovered {health_restored} health points.")
                else:
                    print("You're already at full health.")
                    
                # Time passes
                print("Time passes peacefully...")
            else:
                print("This doesn't seem like a safe place to rest.")
                
        elif action == "status":
            self.display_status()
            
        else:
            print(f"I don't understand '{command}'. Type 'help' for commands.")
            
    def fight(self, enemy):
        enemy_stats = self.enemies[enemy].copy()
        print(f"\nYou engage the {enemy.replace('_', ' ')} in combat!")
        
        # Base damage
        player_damage = 15
        
        # Weapon bonus
        if self.player["equipped_weapon"]:
            weapon_bonus = self.weapons.get(self.player["equipped_weapon"], 0)
            player_damage += weapon_bonus
            print(f"Your {self.player['equipped_weapon'].replace('_', ' ')} gives you +{weapon_bonus} damage!")
            
        # Armor bonus (damage reduction)
        damage_reduction = 0
        if hasattr(self.player, "equipped_armor") and self.player["equipped_armor"]:
            damage_reduction = self.armor.get(self.player["equipped_armor"], 0)
            
        while enemy_stats["health"] > 0 and self.player["health"] > 0:
            # Player attacks first
            damage_dealt = random.randint(player_damage - 5, player_damage + 5)
            enemy_stats["health"] -= damage_dealt
            print(f"You hit the {enemy.replace('_', ' ')} for {damage_dealt} damage!")
            
            if enemy_stats["health"] <= 0:
                print(f"You defeated the {enemy.replace('_', ' ')}!")
                self.rooms[self.current_room]["enemies"].remove(enemy)
                self.total_enemies_defeated += 1
                
                # Reward for defeating enemy
                gold_reward = random.randint(10, 30)
                self.player["gold"] += gold_reward
                print(f"You found {gold_reward} gold on the {enemy.replace('_', ' ')}.")
                
                # Special loot drops
                if enemy == "skeleton" and random.random() > 0.7:
                    self.rooms[self.current_room]["items"].append("bone_amulet")
                    print("The skeleton was wearing a strange bone amulet. You can now take it.")
                    
                elif enemy == "ice_elemental":
                    self.rooms[self.current_room]["items"].append("frost_essence")
                    print("The ice elemental left behind a glowing frost essence. You can now take it.")
                    
                # Check for special victory conditions
                if self.total_enemies_defeated >= 5 and not self.has_completed_dungeon:
                    print("\nYou've proven yourself to be a formidable warrior!")
                    
                return
                
            # Enemy attacks back
            time.sleep(0.5)  # Small pause for effect
            enemy_damage = random.randint(enemy_stats["damage"] - 5, enemy_stats["damage"] + 5)
            
            # Apply damage reduction from armor
            if damage_reduction > 0:
                reduced_damage = max(1, enemy_damage - damage_reduction)
                print(f"Your armor absorbs {enemy_damage - reduced_damage} damage!")
                enemy_damage = reduced_damage
                
            self.player["health"] -= enemy_damage
            print(f"The {enemy.replace('_', ' ')} hits you for {enemy_damage} damage!")
            
            if self.player["health"] <= 0:
                print(f"\nYou have been defeated by the {enemy.replace('_', ' ')}...")
                print("GAME OVER")
                self.game_over = True
                return
                
            # Display current health
            print(f"Your health: {self.player['health']}  {enemy.replace('_', ' ').title()}'s health: {enemy_stats['health']}")
            
            # Option to continue fighting or try to flee
            choice = input("Continue fighting (f) or try to run away (r)? ").lower()
            if choice.startswith('r'):
                # 60% chance to escape
                if random.random() > 0.4:
                    print("You managed to escape!")
                    return
                else:
                    print("You couldn't escape!")
                    # Enemy gets a free attack
                    enemy_damage = random.randint(enemy_stats["damage"] - 5, enemy_stats["damage"] + 5)
                    
                    # Apply damage reduction from armor
                    if damage_reduction > 0:
                        reduced_damage = max(1, enemy_damage - damage_reduction)
                        print(f"Your armor absorbs {enemy_damage - reduced_damage} damage!")
                        enemy_damage = reduced_damage
                        
                    self.player["health"] -= enemy_damage
                    print(f"The {enemy.replace('_', ' ')} hits you for {enemy_damage} damage as you try to flee!")
                    
                    if self.player["health"] <= 0:
                        print(f"\nYou have been defeated by the {enemy.replace('_', ' ')}...")
                        print("GAME OVER")
                        self.game_over = True
                        return
                        
    def display_help(self):
        print("\n===== COMMAND HELP =====")
        print("go [location] - Move to a new location")
        print("take/get [item] - Pick up an item")
        print("fight/attack [enemy] - Fight an enemy")
        print("use [item] - Use an item from your inventory")
        print("equip [item] - Equip a weapon or armor")
        print("look - Look around the current room")
        print("talk - Talk to characters in the area")
        print("rest/sleep - Recover health in safe locations")
        print("status - Display detailed character status")
        print("help - Display this help message")
        print("quit - End the game")
        
    def display_status(self):
        print("\n===== CHARACTER STATUS =====")
        print(f"Name: {self.player['name']}")
        print(f"Health: {self.player['health']}/{self.player['max_health']}")
        print(f"Gold: {self.player['gold']}")
        
        if self.player["equipped_weapon"]:
            weapon = self.player["equipped_weapon"]
            bonus = self.weapons[weapon]
            print(f"Weapon: {weapon.replace('_', ' ')} (+{bonus} damage)")
        else:
            print("Weapon: None")
            
        if hasattr(self.player, "equipped_armor") and self.player["equipped_armor"]:
            armor = self.player["equipped_armor"]
            reduction = self.armor[armor]
            print(f"Armor: {armor.replace('_', ' ')} (-{reduction} damage taken)")
        else:
            print("Armor: None")
            
        if self.player["inventory"]:
            print("\nInventory:")
            for item in self.player["inventory"]:
                print(f"- {item.replace('_', ' ')}")
        else:
            print("\nInventory: Empty")
            
        print(f"\nEnemies defeated: {self.total_enemies_defeated}")
        
        if self.has_completed_dungeon:
            print("\nAchievements:")
            print("- Escaped the dungeon with the golden chalice!")

# Start the game
if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
