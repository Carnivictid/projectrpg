import random


class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0

	def is_dead(self):
		return self.hp <= 0

	def attack_player(self, player):
		if self.is_alive(): 
			print("\n{} attacks {}.".format(self.name, player), end=' ') # refactor for linux. end=" " doesn't work
			roll = random.randint(1, 20) + self.ab + self.str
			damage_roll = random.randint(1, self.damage) + self.str
			if roll >= player.ac:
				player.hp -= damage_roll
				print("{} takes {} damage. {} HP remaining.".format(player.name, damage_roll, player.hp))
			else:
				print("{}'s attack misses {}!".format(self, player.name))
		else:
			print("Something broke. A dead enemy should not have called attack_player(self, player, number)")


def get_exp(cr):
	if cr == "1/4":
		return 75
	if cr == "1/3":
		return 100
	if cr == "1/2":
		return 150
	if cr == "1":
		return 300
			
			
			
			
# ====== CR Lower than 1 ======= #
class LargeRat(Enemy):
	def __init__(self):
		self.name = "Dire Rat"
		self.hp = (random.randint(1, 8) + 1)
		self.damage = 4
		self.ab = 4
		self.str = 0
		self.ac = 15
		self.exp = get_exp("1/3")


class SmallGoblin(Enemy):
	def __init__(self):
		self.name = "Small Goblin"
		self.hp = (random.randint(1, 8))
		self.damage = 8
		self.ab = 1
		self.str = -1
		self.ac = 15
		self.exp = get_exp("1/4")

