import items
import world
import random, os
import enemies
import classes


class Player:

    def __init__(self, player_name, class_level):
        # Round count for spell timers
        self.rounds = 0

        # Starting location coordinates for the Player.
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.victory = False

        # Class of the starting player.
        self.name = player_name
        self.level = class_level
        self.exp = 0
        self.player_class = classes.Fighter()

        # Item inventory for the player.
        self.item_inventory = []
        self.map_inventory = []
        self.gold = 0

        # Weapon / Armor inventory for the player
        self.arms_inventory = [items.ShortSword()]
        self.armor_inventory = []
        
        self.ac_bonus = 0
        self.worn_armor = None
        self.worn_shield = None
        self.worn_weapon = items.ShortSword()

        # Ability Scores
        self.str = 16
        self.dex = 14
        self.con = 14
        self.wis = 14
        self.int = 10
        self.cha = 10
        
        # Ability Modifiers
        self.str_mod = int((self.str - 10) / 2)
        self.dex_mod = int((self.dex - 10) / 2)
        self.con_mod = int((self.con - 10) / 2)
        self.wis_mod = int((self.wis - 10) / 2)
        self.int_mod = int((self.int - 10) / 2)
        self.cha_mod = int((self.cha - 10) / 2)
        
        self.bab = self.player_class.base_attack[self.level]
        self.attack_bonus = self.bab + self.str_mod
        self.number_of_attacks = 0

        # Armor Class and HP Stats
        self.hit_dice = self.player_class.hit_dice
        self.max_hp = int(self.hit_dice + self.con_mod)
        self.hp = self.max_hp
        
        self.ac = int(10 + self.dex_mod + self.ac_bonus)
        
        # Base saves!
        self.base_fort = self.player_class.base_fort_save[self.level]
        self.base_ref = self.player_class.base_ref_save[self.level]
        self.base_will = self.player_class.base_will_save[self.level]

        # Total score for saves!
        self.fort_save = 0 + self.base_fort + self.con_mod
        self.ref_save = 0 + self.base_ref + self.dex_mod
        self.will_save = 0 + self.base_will + self.wis_mod
        
        # Misc things, will be organized later.
        self.buff_status = False
        self.last_round = 0
        self.attack_actions = ['melee']

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0
        
    def is_dead(self):
        return self.hp < 0
         
    def refresh_level(self):
        # This function refreshes all of the stat-dependant variables. All are in the Player __init__
        # Recalculating ability modifiers
        self.str_mod = int((self.str - 10) / 2)
        self.dex_mod = int((self.dex - 10) / 2)
        self.con_mod = int((self.con - 10) / 2)
        self.wis_mod = int((self.wis - 10) / 2)
        self.int_mod = int((self.int - 10) / 2)
        self.cha_mod = int((self.cha - 10) / 2)
        
        # Checking the base save numbers from player_class
        self.base_fort = int(self.player_class.base_fort_save[self.level])
        self.base_ref = int(self.player_class.base_ref_save[self.level])
        self.base_will = int(self.player_class.base_will_save[self.level])
        
        # Adding the base save with modifier value.
        self.fort_save = 0 + self.base_fort + self.con_mod
        self.ref_save = 0 + self.base_ref + self.dex_mod
        self.will_save = 0 + self.base_will + self.wis_mod
        
        # Refreshing BAB and attacks.
        self.bab = self.player_class.base_attack[self.level]
        self.number_of_attacks = self.generate_number_of_attacks(self.bab)
        self.attack_bonus = self.bab + self.str_mod
        
    def generate_number_of_attacks(self, base):
        # This just calculates the number of attacks based on BAB.
        filler = base
        noa = 0
        while True:
            if filler < 0:
                break
            else:
                filler -= 5
                noa += 1
        return noa  

    def print_inventory(self):
        # Prints a list of inventory
        print("\nArmor and Weapons:")
        for item in self.armor_inventory:
            print("* " + str(item))
        for item in self.arms_inventory:
            print("* " + str(item))
        print("Backpack:")
        for item in self.item_inventory:
            print("* " + str(item))

    #TODO Make a healing function
    def heal(self):
        pass
			
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
        
    def attack(self):
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy

        if len(enemy) > 1:
            print("\nWhich enemy do you want {} to attack?".format(self.name))
            for i, monster in enumerate(enemy, 1):
                if monster.is_alive():
                    print("{}. {}".format(i, monster))
            valid = False
            while not valid:
                choice = input("Choice: ")
                print()
                try:
                    if enemy[int(choice) - 1].is_alive():
                        to_attack = enemy[int(choice) - 1]
                        if len(self.attack_actions) == 1:
                            self.melee_attack(to_attack)
                            break
                        elif len(self.attack_actions) > 1:
                            print("\nWhat kind of action will you take?")
                            choice2 = input("Choice: ")
                            print()
                    else:
                        print("Invalid choice, try again.")
                    
                except (ValueError, IndexError):
                    print("Invalid choice, try again.")
        elif len(enemy) == 1:
            if len(self.attack_actions) == 1:
                self.melee_attack(enemy[0])
            elif len(self.attack_actions) > 1:
                print("\nWhat kind of action will you take?")
                choice2 = input("Choice: ")
                print()
        else:
            print("Something went wrong, you can't call an attack with no enemies in the room")

    def melee_attack(self, target, **kwargs):
        critical = 1
        ensure_hit = 0
        
        # A standard attack. Accounts for number of attacks.
        print("\n{} attack {}".format(self.name, target))
        
        # temp_attack_bonus is drained by 5 for each attack.
        temp_attack_bonus = self.attack_bonus
        
        for attacks in range(self.number_of_attacks):
            if target.is_alive():
                # Rolling the D20
                r20 = random.randint(1, 20)
                
                # Checking to see if the roll was a critial threat.
                if r20 >= self.worn_weapon.crit_range:
                
                    # Now rolling to confirm the critical
                    check_r20 = random.randint(1, 20) + self.str_mod
                    
                    # Checking if critical is confirmed.
                    if check_r20 >= target.ac:
                    
                        # Sets some variables to ensure correct damage.
                        print("Critical Hit!")
                        critical = self.worn_weapon.crit_multi
                        ensure_hit = 100
                
                # Adding remaining Base Attack and str mod.
                total_roll = r20 + (temp_attack_bonus - (5 * attacks)) + ensure_hit
                print("Rolled: ({} + {}) {}".format(r20, (temp_attack_bonus - (5 * attacks)), total_roll - ensure_hit))
                
                # comparing the total roll with the enemy's AC.
                if total_roll >= target.ac:
                    
                    # Counting damage dice and rolling each one.
                    damage_rolls = 0
                    for dice in range(self.worn_weapon.dice_amount):
                        damage_rolls += random.randint(1, self.worn_weapon.dice_number)
                        
                    # Adding damage and modifiers. 
                    total_damage = (damage_rolls + self.str_mod) * critical
                    target.hp -= total_damage
                    print("{} did {} damage to {}.".format(self.name, total_damage, target))
                    
                    if target.hp <= 0:
                        print("{} killed {}!".format(self.name, target))
                        
                # resetting the critical hit variables so nothing wonky happens for multi attacks.
                critical = 1
                ensure_hit = 0
            else:
                # The target was dead when attacked.
                print("Target has died.")
            
    def check_weight(self):
        pass
        
    def wait(self):
        pass
