from collections import OrderedDict
import playeractions
from players import Player
import os, time, sys, textwrap #world
import colorama
from colorama import Fore, Back, Style
import pickle

import newworld
import newplayers

import pickle

# some constants
LOAD = "load"
NEW  = "new"
CWD = os.path.dirname(os.path.realpath(__file__)) + "\\saves\\"
PK = ".pk"


class GameState:
	def __init__(self, savename, world, player):
		self.savename = savename
		self.world = world
		self.player = player
		self.npcs = None
		self.quests = None
		self.time = None
		
		self.CWD = os.path.dirname(os.path.realpath(__file__)) + "\\saves\\"
		self.PK = ".pk"
		
	def __str__(self):
		return("Save Name: {}\nSaved: {}".format(self.savename, self.time))
		
	def setNPCs(self, npcs):
		self.npcs = npcs
		
	def setQuests(self, quests):
		self.quests = quests
	
	def getName(self):
		return self.savename
		
	def gameStateValid(self):
		return (self.savename or self.world or self.player 
				 or self.npcs or self.quests) is not None
	
	def loadGame(self):
		# pickles go here.
		pass
		
	def savePathExists(self):
		return os.path.exists(CWD + savename + PK)

		
		
def play():
	savename = 'player'
	print("Welcome to ProjectRPG. A game made by a nerd for himself.")
	
	# initialize colorama for fluffy text colors.
	# if more things need initialization, then I will make a func.
	colorama.init()
	
	# ask the player to load or save game.
	start_game = newOrLoadGame()
	if start_game == LOAD:
		gs = load_game()
	elif start_game == NEW:
		gs = GameState(savename, newworld.WorldClass(), newplayers.Player("You", 1))
		gs.player.refresh_level()
		gs.player.set_x_y(gs.world.start_tile_location[0],
						  gs.world.start_tile_location[1])
	
	gameLoop(gs)


def gameLoop(gs):
	while not gs.player.victory and gs.player.is_alive():
		room = gs.world.tile_at(gs.player.x, gs.player.y)
		gs.player.room = room
		print(room.intro_text())
		while gs.player.is_alive() and not gs.player.victory:
			print(room.title_text())
			room.modify_player(gs.player)
			if gs.player.is_alive() and not gs.player.victory:
				gs.player.check_for_level()
				choose_action(room, gs.player, gs)
				check_room = gs.world.tile_at(gs.player.x, gs.player.y)
				if check_room != room:
					break
			elif gs.player.is_alive() and gs.player.victory:
				break
	if gs.player.is_dead():
		print("\nYour journey has come to an early end! But it's not over yet.")

		
def newOrLoadGame():
	# Prompt player to start a new game, load a save, or quit the program
	while True:
		print("\nWould you like to start a new game or load a previous save?")
		print("1) New Game\n2) Load Game\nQ) Quit Game")
		choice = input("Choose action: ")
		if choice == "1" or choice.lower() == "n":
			return NEW
		elif choice == "2" or choice.lower() == "l":
			return LOAD
		elif choice.lower() == "q":
			quit()
		else:
			print("Invalid choice, try again!")
	return start_game
	
	
def save_game(gs):
	if os.path.exists(CWD + gs.savename + PK):
		ow = input("Do you want to override your save: {}? y/n\n>>> ".format(gs.savename))
		if ow.lower() == "y":
			pickle.dump(gs, open(CWD + gs.savename + PK, "wb"))
			print("Game saved. Quiting.")
			exit()
		elif ow.lower() == "n":
			print("Okay, back to the game, then!")
		else:
			print("Invalid option.")
	else:
		pickle.dump(gs, open(CWD + gs.savename + PK, "wb"))
		print("Game saved. Quiting.")
		exit()
		
		
def load_game():
	saved_games = []
	for file in os.listdir(CWD):
		if file.endswith(PK):
			saved_games.append(file)
	print("Which one do you want to load?")
	for i, saved_game in enumerate(saved_games, 1):
		print("{}: {}".format(i, saved_game[:-3]))
	choice = input("Choose a save game: ")
	savename = saved_games[int(choice)-1]
	print("Loading: {}".format(savename))
	return pickle.load(open(CWD + savename, "rb"))


def choose_action(room, player, gs):
	action = None
	while not action:
		print("----------------", end="")
		available_actions = playeractions.get_available_actions(room, player, gs)
		action_input = input("\nAction: ")
		action = available_actions.get(action_input)
		print("----------------")
		# If an action is type out, this will always run.
		if action:
			action()

		# Now begins the fully typed commands.
		elif action_input == 'help':
			print("\nThere are several commands you can use at any time! Be careful, they take 1 round.")
			print("Commands:")
			print("wait: waits for 1 round.")
			print("party: opens the party management window.")
			print("quests: shows the quest list")
			print("more commands comming soon.")
		elif action_input == 'party':
			print("\nThis command is a work in progress. Sorry!")
			break
		elif action_input == 'save':
			save_game(gs)
			break
		elif action_input == 'wait':
			print("\nYou wait for one round.")
			break
		elif action_input == 'quests':
			for quest in player.quest_list:
				quest.print_quest_log()
		else:
			print("""
		Invalid action!
			""")
		

if __name__ == "__main__":
	play()