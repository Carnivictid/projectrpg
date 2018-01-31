import world
import items



class Quest:
	def __init__(self):
		raise NotImplementedError("Do not create raw quest classes")
		
	def __str__(self):
		return self.quest_name
	
	def give_reward(self, player):
		print("You receive: \n{} gold\n{} exp".format(self.reward_gold, self.reward_exp))
		for item in self.reward_item:
			print(item)
		player.gold += self.reward_gold
		player.exp += self.reward_exp
		for item in self.reward_item:
			player.item_inventory.append(item)
		self.complete = True



class NoobQuest(Quest):
	def __init__(self):
		self.quest_status = 0
		self.quest_name = "Kill the Rat!"
		self.reward_gold = 250
		self.reward_exp = 500
		self.reward_item = [items.Longsword()]
		self.quest_log = []
		self.complete = False
	
	
	def print_quest_log(self):
		print("Quest: {}".format(self.quest_name))
		for n, q in enumerate(self.quest_log, 1):
			print("{}: {}".format(n, q))

	def update_quest_log(self, quest_log_text):
		self.quest_log.append(quest_log_text)

''' #### Working on new quest architecture ####
class QuestObject:
	def __init__(self):
		self.quest_status = 0
		self.complete_status = 0
		self.quest_name = "Quest Name"
		self.reward_gold = 0
		self.reward_exp = 0
		self.reward_item = []
		self.quest_logs = []
		self.player_log = []
		self.complete = False
	
	def __str__(self):
		return self.quest_name

	def give_reward(self, player):
		if self.complete:
			print("You tried to get rewards twice! Something broke!")
			return
		print("You completed the quest: {}".format(self.quest_name))
		print("Here is your reward:")
		for item in self.reward_item:
			print("* {}".format())
			player.item_inventory.append(item)
		print("* {} Gold\n* {} Exp".format(self.reward_gold, self.reward_exp))
		player.gold += self.reward_gold
		player.exp += self.reward_exp
		self.complete = True
	
	def set_quest_status(self, status):
		self.quest_status = status
	
	def update_player_log(self, index):
		self.player_log.append(self.quest_logs[index])
	
	def can_be_completed(self):
		return self.quest_status == self.complete_status
'''
