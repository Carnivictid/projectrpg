import world #
import classes #
import items #
import enemies #
import quests #
import random #
import os #
from ctxt import * #


class Player:
	def __init__(self, player_name, player_level):
		self.rounds = 0 # Round count, for spell timers
		self.quest_list = [] # Quests lists for journal
		
		# Coordinates for the player
		self.x = None
		self.y = None
		self.current_room = None
		self.victory = False
		
		# Class information
		self.name = player_name
		self.level = player_level
		self.exp = 0
		self.player_class = classes.Fighter()
		
		# Item inventory
		self.item_inventory = []
		self.map_inventory = []
		self.gold = 0
		
		# Ability Scores (this will be changed to unit test)
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
		
		# Combat stats
		self.bab = self.player_class.base_attack[self.level]
		self.attack_bonus = self.bab + self.str_mod
		self.number_of_attacks = 0
		
		# Worn items and AC bonus
		self.worn_armor = None
		self.worn_shield = None
		self.worn_weapon = None
		self.ac_bonus = self.get_ac_bonus()
		
		# Armor Class and HP Stats
		self.hit_dice = self.player_class.hit_dice
		self.max_hp = int(self.hit_dice + self.con_mod)
		self.hp = self.max_hp
		
		self.ac = int(10 + self.ac_bonus)
		
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
		return self.hp <= 0
		
	def set_x_y(self, x, y):
		self.x = x
		self.y = y

	def level_up(self):
		# up level and roll hp.
		self.level += 1
		print("You have leveled to Level: {}".format(self.level))
		
		hd_roll = random.randint(1, self.hit_dice) + self.con_mod
		self.max_hp += hd_roll
		self.hp = self.max_hp
		print("You have gained {} HP for a total of {} HP".format(hd_roll, self.max_hp))
		self.refresh_level()
	
	def refresh_ac_bonus(self):
		self.ac_bonus = self.get_ac_bonus()
		self.ac = int(10 + self.ac_bonus)
		
	def get_ac_bonus(self):
		# armor + shield + dex(no more than max dex from armor)
		total_ac_bonus = 0
		
		if self.worn_shield is not None:
			shield_ac = self.worn_shield.ac_bonus
		else:
			shield_ac = 0
		
		if self.worn_armor is not None:
			armor_ac = self.worn_armor.ac_bonus
			max_dex = self.worn_armor.max_dex
		else:
			armor_ac = 0
			max_dex = 100
		
		if self.dex_mod > max_dex:
			dex_ac = max_dex
		else:
			dex_ac = self.dex_mod
		
		total_ac_bonus = armor_ac + shield_ac + dex_ac
		
		return total_ac_bonus
		 
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
		
		print("="*16)
		print("Level: {} | EXP: {} | Gold: {}".format(self.level, self.exp, self.gold))
		print("HP: {}/{} | AC: {}".format(self.hp, self.max_hp, self.ac))
		print("\nEquipped:\nWeapon: {}\nArmor: {}\nShield: {}".format(self.worn_weapon, self.worn_armor, self.worn_shield))
		print("\nBackpack:")
		
		for item in self.item_inventory:
			if isinstance(item, items.Weapon):
				print("* " + str(item))
		
		for item in self.item_inventory:
			if isinstance(item, items.Shield):
				print("* " + str(item))
				
		for item in self.item_inventory:
			if isinstance(item, items.Armor):
				print("* " + str(item))
		
		for item in self.item_inventory:
			if isinstance(item, items.Consumable):
				print("* " + str(item))
				
		for item in self.item_inventory:
			if isinstance(item, items.Item):
				print("* " + str(item))

		print("="*16) 
		open = True
		while open:
			print("\nW: Equip Weapon\nA: Equip Armor\nS: Equip Shield\nH: Heal\nC: Close backpack")
			action_input = input("\nAction: ")
			print("----------------")
			if action_input.lower() == "w":
				self.equip("w")
				open = False
				
			elif action_input.lower() == "a":
				self.equip("a")
				open = False
				
			elif action_input.lower() == "s":
				self.equip("s")
				open = False
				
			elif action_input.lower() == "h":
				self.heal()
				open = False
				
			elif action_input.lower() == "c":
				return
				
				
			else:
				print("\nThat is not a valid action, try again.")

	def swap_item_inv(self, item, from_inv, to_inv):
		try:
			# remove the item from one
			from_inv.remove(item)
			# add the item to the new inv
			to_inv.append(item)
		except:
			print("There was an issue adding the item to your inv.") 

	def equip(self, type):
		# Temp containers to track if its a weapon, shield or armor.
		worn_item = None
		item_type = None
		
		if type == "w": # Getting the types for inventory parsing.
			worn_item = self.worn_weapon
			item_type = items.Weapon
		if type == "a":
			worn_item = self.worn_armor
			item_type = items.Armor
		if type == "s":
			worn_item = self.worn_shield
			item_type = items.Shield
		
		# creates a list of equipable items based on item type.
		inventory = [item for item in self.item_inventory if isinstance(item, item_type)]
		
		if worn_item != None: # If you have an item equipped, you can unequip it.
			print("U: Unequip worn {}".format(worn_item))
			
		for n, i in enumerate(inventory, 1): # Show the list of equipable items
			print("{}: Equip {}".format(n, i))
		
		print("\nC: Cancel") # Cancel out if you misclick or whatever.
		
		valid = False
		while not valid:
			choice = input("\nChoice: ")
			print("----------------")
			
			if choice.lower() == "c": # cancels the equip function
				return
				
			if choice.lower() == "u": # Unequip an item.
				print("You remove the {}".format(worn_item))
				if worn_item != None:
					self.item_inventory.append(worn_item)
					if type == "w":
						self.worn_weapon = None
					if type == "s":
						self.worn_shield = None
					if type == "a":
						self.worn_armor = None
					self.refresh_ac_bonus()
					valid = True
					break
			try: # This trys to equip an item.
				to_equ = inventory[int(choice) - 1] # Gets the item from the temp inv based on choice.
				print("You equip {}!".format(to_equ))
				
				if type == "w":
					self.worn_weapon = to_equ
				if type == "a":
					self.worn_armor = to_equ
				if type == "s":
					self.worn_shield = to_equ
					
				if worn_item != None:
					self.item_inventory.append(worn_item)
					
				self.item_inventory.remove(to_equ)
				self.refresh_ac_bonus()
				valid = True
			except (ValueError, IndexError): 
				print("Invalid choice, try again!")

	def heal(self):
		healing_items = [item for item in self.item_inventory 
						 if isinstance(item, items.Consumable)]
		
		if not healing_items:
			print("\nYou have nothing to heal with!")
			return
		
		print("="*16) 
		print("Choose an item to use:\n")
		for i, item in enumerate(healing_items, 1):
			print("{}: {}".format(i, item))
		print("\nc: Cancel healing action")
		print("="*16)	 
		valid = False
		while not valid:
			choice = input("")
			try:
				if choice == ("c" or "C"):
					return
				to_eat = healing_items[int(choice) - 1]
				print("You heal {} points of damage".format(to_eat.healing_value))
				
				self.hp += to_eat.healing_value
				if self.hp > self.max_hp:
					self.hp = self.max_hp
					
				self.item_inventory.remove(to_eat)
				valid = True
			except (ValueError, IndexError):
				print("Invalid choice, try again.")
			
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
		enemy = self.room.enemy

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

	def melee_attack(self, target):
		#VARS:
		ab = self.attack_bonus
		sb = self.str_mod
		noa = self.generate_number_of_attacks(self.bab)
		critm = self.worn_weapon.crit_multi if self.worn_weapon != None else 2
		critr = self.worn_weapon.crit_range if self.worn_weapon != None else 20
		wdc = self.worn_weapon.dice_count if self.worn_weapon != None else 1
		wdn = self.worn_weapon.dice_number if self.worn_weapon != None else 4
		e_ac = target.ac
		
		
		#check crit
		for num in range(noa):
			crit = False
			hit = False
			if target.is_alive():
				d20 = random.randint(1, 20)
				print("You attack {}. You rolled {} ({} + {})".format(target, (d20+ab), d20, ab), end=". ")
				if d20 >= critr and random.randint(1, 20)+ab >= e_ac:
					hit = True
					crit = True
					print("Critical hit confirmed!")
						
				elif d20+ab >= e_ac:
					hit = True
					print("The attack hits!")
					
				if hit: 
					damage = sb
					for dice in range(wdc):
						damage += random.randint(1, wdn)
					if crit:
						damage = damage * critm
						
					target.hp -= damage
					atkprint("You dealt {} damage to {}".format(damage, target))
					
				if target.is_dead():
					self.room.is_dangerous = False
					print("{} has died!".format(target))
					self.exp += target.exp
					print("The monster gives you", end=" ") 
					expprint("{} exp!".format(target.exp))
				if not hit:
					missprint("\nThe attack missed!")
			ab -= 5
		
	def check_weight(self):
		pass
		
	def wait(self):
		pass
		
	def check_for_level(self):
		# X is current level, (X + 1) * X * 500 = exp to desired level
		exp_to_level = ((self.level + 1) * (self.level) * 500)
		
		if self.exp >= exp_to_level:
			self.level_up()
			
	def trade(self):
		self.room.check_if_trade(self)
	
	def talk(self):
		self.room.talk(self)
		
	def get_quest(self, quest):
		for n, q in enumerate(self.quest_list):
			if isinstance(q, quest):
				return q
