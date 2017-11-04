import items
import quests


class NPC():
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects")
		
	def __str__(self):
		return self.name
		
		
class Trader(NPC):
	def __init__(self):
		self.name = "Trader"
		self.gold = 100
		self.item_inventory = [items.LightHealingPotion(),
							   items.LightHealingPotion(),
							   items.LightHealingPotion()]


class QuestGiver(NPC):
	def __init__(self):
		self.name = "Quest Giver"
		self.gold = 100
		
	def talk_npc(self, player):
		if player.get_quest(quests.NoobQuest) is None:
			print("Can you kill the rat to the southeast for me? Ill reward you.")
			while True:
				choice = input("(y)es or (n)o: ")
				if choice.lower() == "n":
					print("Fine. Leave me be.")
					return
				elif choice.lower() == "y":
					print("Thank you! Come back when it is done.")
					if player.get_quest(quests.NoobQuest) == None:
						player.quest_list.append(quests.NoobQuest())
					player.get_quest(quests.NoobQuest).quest_status = 1
					player.get_quest(quests.NoobQuest).update_quest_log("An old man wants me to kill a rat. Why not. Its to his southeast")
					return
				else:
					print("Invalid choice, try again.")
		elif player.get_quest(quests.NoobQuest).quest_status == 1 and player.get_quest(quests.NoobQuest).complete is not True:
			print("Have you finished your task? Please, there is a good reward in it for you.")
		elif player.get_quest(quests.NoobQuest).quest_status == 2 and player.get_quest(quests.NoobQuest).complete is not True:
			print("Thank you so much for killing that beast! Here is your reward!")
			player.get_quest(quests.NoobQuest).give_reward(player)
			player.get_quest(quests.NoobQuest).complete = True
			player.get_quest(quests.NoobQuest).update_quest_log("I killed the rat and the old man gave me 250 gold and a sword!")
		elif player.get_quest(quests.NoobQuest).quest_status == 3 and player.get_quest(quests.NoobQuest).complete is not True:	
			print("I was going to ask you to kill the rat to the southeast...")
			print("But it looks like you did that already.")
			print("I will still give you the reward. Thank you!")
			player.get_quest(quests.NoobQuest).give_reward(player)
			player.get_quest(quests.NoobQuest).complete = True
			player.get_quest(quests.NoobQuest).update_quest_log("It turns out an old man wanted that rat dead. He gave me 250 gold and a sword!")
		elif player.get_quest(quests.NoobQuest).complete:
			print("Thank you again for your assistance")
			
			
			
			
			
			
			
			
			