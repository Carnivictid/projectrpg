import items
import random
import enemies
import npc
import quests

# This files contains the basic tiles that can be made in the game
# This allows for combat, healing, trading, questing and saving progress
# From here, time is going to be spent refactoring code to make sure the 
# following code runs efficiently, correctly, and is documented.



#========== Blank Maptile Class ==========#
class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.round_count = 0
		self.is_dangerous = False
		self.enemy = []
		self.npc = None
				

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead")

	def modify_player(self, player):
		pass
		
	def enemy_attacks(self, player):
		if len(self.enemy) > 0:
			for number, monster in enumerate(self.enemy, 1):
				if monster.is_alive():
					monster.attack_player(player)
				elif monster.is_dead():
					self.enemy.remove(monster)
		for number, monster in enumerate(self.enemy, 1):
			if monster.is_dead():
				self.enemy.remove(monster)
		if len(self.enemy) <= 0:
			self.is_dangerous = False
	
	def check_if_trade(self, player):
		while True:
			print("\nWould you like to (B)uy, (S)ell, or (Q)uit?")
			user_input = input()
			if user_input.lower() == "q":
				return
			elif user_input.lower() == "b":
				print("\nHere is what's available to buy: ")
				self.trade(buyer = player, seller = self.npc)
			elif user_input.lower() == "s":
				print("\nHere is what's available to sell: ")
				self.trade(buyer = self.npc, seller = player)
			else:
				print("Invalid choice!")
	
	def trade(self, buyer, seller):		  
		while True:
			for i, item in enumerate(seller.item_inventory, 1):
				print("{}. {} - {} gold".format(i, item.name, item.value))
			user_input = input("Choose an item or press Q to exit: ")
			if user_input.lower() == "q":
				return
			else:
				try: 
					choice = int(user_input)
					to_swap = seller.item_inventory[choice - 1]
					self.swap(buyer, seller, to_swap)
				except ValueError:
					print("Invalid choice!")
					
	def swap(self, buyer, seller, item):
		if item.value > buyer.gold:
			print("That's too expensive\n")
			return
		seller.item_inventory.remove(item)
		buyer.item_inventory.append(item)
		seller.gold += item.value
		buyer.gold -= item.value
		print("Trade complete!\n")


#========== Starting tile for testing. ==========#
class StartingTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		if self.round_count == 0:
			return "StartingTile.intro_text() first round. You got a sword."
		else:
			return "StartingTile.intro_text() second round and on."
		
	def title_text(self):
		if self.round_count == 0:
			return "StartingTile.title_text() first round."
		else:
			return "StartingTile.title_text() second round and on."
		
	def modify_player(self, player):
		if self.round_count == 0:
			player.give_item(items.RustySword())
			
		# this should be on any tile that could have an enemy. 
		if len(self.enemy) > 0:
			self.enemy_attacks(player)
			
		self.round_count += 1


#========== Victory tile for testing. ==========#
class VictoryTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		return "VictoryTile.title_text()."
		
	def title_text(self):
		return "VictoryTile.intro_text(). You win, nice job."

	def modify_player(self, player):
		player.victory = True		


#========== Tile1 throws a rat at you. ==========#
class Tile1(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.enemy = [enemies.LargeRat()]
		self.is_dangerous = True

	def intro_text(self):
		if self.round_count == 0:
			return "Tile1.intro_text() first round. Watch out, a rat..."
		else:
			return "Tile1.intro_text() second round and on."
		
	def title_text(self):
		if self.round_count == 0:
			return "Tile1.title_text() first round."
		else:
			return "Tile1.title_text() second round and on."
		
	def modify_player(self, player):
		# this should be on any tile that could have an enemy. 
		if len(self.enemy) > 0:
			self.enemy_attacks(player)
			
		self.round_count += 1


#========== Tile2 has a quest giver. ==========#
class Tile2(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.npc = npc.QuestGiver()

	def intro_text(self):
		if self.round_count == 0:
			return "Tile2.intro_text() first round. There is a guy here."
		else:
			return "Tile2.intro_text() second round and on. A guy is here."
		
	def title_text(self):
		if self.round_count == 0:
			return "Tile2.title_text() first round."
		else:
			return "Tile2.title_text() second round and on."
		
	def modify_player(self, player):	
		# this should be on any tile that could have an enemy. 
		if len(self.enemy) > 0:
			self.enemy_attacks(player)
			
		self.round_count += 1

	def talk(self, player):
		self.npc.talk_npc(player)


#========== Tile2 has a healing item. ==========#
class Tile3(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		if self.round_count == 0:
			return "Tile3.intro_text() first round. You got bandages."
		else:
			return "Tile3.intro_text() second round and on."
		
	def title_text(self):
		if self.round_count == 0:
			return "Tile3.title_text() first round."
		else:
			return "Tile3.title_text() second round and on."
		
	def modify_player(self, player):
		if self.round_count == 0:
			player.give_item(items.LightBandage())
			
		self.round_count += 1


#========== Tile4 has a quest monster. ==========#
class Tile4(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.is_dangerous = True
		self.enemy = [enemies.LargeRat()]
	
	def intro_text(self):
		return "Tile4.intro_text()"
		
	def title_text(self):
		return "Tile4.title_text()"
		
	def modify_player(self, player): # when you enter the tile, it gives you the quest.
		if player.get_quest(quests.NoobQuest) == None:
			player.quest_list.append(quests.NoobQuest())
		self.enemy_attacks(player)
		if len(self.enemy) <= 0: # you are given the quest if you complete the task anyways.
			if player.get_quest(quests.NoobQuest).quest_status == 0: #if you didn't take the quest, you get an alternate ending.
				player.get_quest(quests.NoobQuest).quest_status = 3
				player.get_quest(quests.NoobQuest).update_quest_log("There was something unusual about this rat...")
			else:
				player.get_quest(quests.NoobQuest).quest_status = 2
				player.get_quest(quests.NoobQuest).update_quest_log("The rat is dead, I should talk to the old man.")


#========== Tile5 has a trader. ==========#				
class Tile5(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.npc = npc.Trader()

	def intro_text(self):
		return "Tile5.intro_text() there is a trader here."
		
	def title_text(self):
		return "Tile5.title_text()"

