import random
from ctxt import *


class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create empty Enemy objects.")
		
	def __str__(self):
		return self.name
		
	def is_alive(self):
		return self.hp > 0
		
	def is_dead(self):
		return self.hp <= 0
	
	def attack_player(self, player):
		if self.is_alive(): 
			print("\n{} attacks {}.".format(self.name, player))
			roll = random.randint(1, 20) + self.ab + self.str
			damage_roll = random.randint(1, self.damage) + self.str
			if roll >= player.ac:
				player.hp -= damage_roll
				atkprint("{} take {} damage. {} HP remaining.".format(player.name, damage_roll, player.hp))
			else:
				missprint("{}'s attack misses {}!".format(self, player.name))
		else:
			print("Something broke. A dead enemy should not have called attack_player(self, player)")
	
	def get_exp(self, cr):
		if cr == "1/4":
			return 75
		if cr == "1/3":
			return 100
		if cr == "1/2":
			return 150
		if cr == "1":
			return 300
	
	def set_as_quest_obj(self, obj)
		self.quest_obj = obj


# ====== CR Lower than 1 ======= #
class LargeRat(Enemy):
	def __init__(self):
		self.name = "Dire Rat"
		self.hp = (random.randint(1, 8) + 1)
		self.damage = 4
		self.ab = 4
		self.str = 0
		self.ac = 15
		self.exp = self.get_exp("1/3")
		self.quest_obj = None


class SmallGoblin(Enemy):
	def __init__(self):
		self.name = "Small Goblin"
		self.hp = (random.randint(1, 8))
		self.damage = 8
		self.ab = 1
		self.str = -1
		self.ac = 15
		self.exp = self.get_exp("1/4")
		self.quest_obj = None

