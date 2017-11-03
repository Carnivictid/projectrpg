import world
import items

# Quests... How do we handle this.....
"""
What is needed for a quest?
Name, gold, exp, item rewards

Quest start location
Quest start requirements

Quest finish requirements
Quest failed requirements

If it has been accepted
Quest dialogue
"""


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
		self.quest_log = set([])
		self.complete = False
	
	
	def print_quest_log(self):
		print("Quest: {}".format(self.quest_name))
		for log in self.quest_log:
			print(log)

	def update_log(self, quest_log_text):
		if self.quest_status == 3:
			self.quest_log.add(quest_log_text)