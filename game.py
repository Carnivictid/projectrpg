import colorama
from colorama import Fore, Back, Style
from collections import OrderedDict
from players import Player
from bin import menus
import playeractions
import pickle
import textwrap
import os
import time
import sys
import world


# some constants
LOAD = "load"
NEW  = "new"
CWD = os.path.dirname(os.path.realpath(__file__)) + "\\saves\\"
PK = ".pk"
VERSIONINFO = "0.0.0002"


class GameState:
	def __init__(self, savename, game_world, player):
		self.savename = savename
		self.world = game_world
		self.player = player
		
		self.CWD = os.path.dirname(os.path.realpath(__file__)) + "\\saves\\"
		self.PK = ".pk"
		
	def __str__(self):
		return("Save Name: {}\nSaved: {}".format(self.savename, self.time))



def get_char_name():
	while True:
		savename = input("What would you like to name your character?\nName: ")
		good = input("Is {} your name? (y)es/(n)o/(q)uit\n>>> ".format(savename))
		if good.lower() == "q":
			return "cancel"
		if good.lower() == "n":
			pass
		if good.lower() == "y":
			return savename


def get_latest_save():
	max_mtime = 0
	for dirname, subdirs, files in os.walk(CWD):
		for fname in files:
			full_path = os.path.join(dirname, fname)
			mtime = os.stat(full_path).st_mtime
			if mtime > max_mtime:
				max_mtime = mtime
				max_dir = dirname
				max_file = fname
	
	return pickle.load(open(CWD + max_file, "rb"))


def new_game():
	savename = get_char_name()
	if savename is None:
		return "cancel"
		
			
	gs = GameState(savename, world.WorldClass(), Player(savename, 1))
	gs.player.refresh_level()
	gs.player.set_x_y(gs.world.start_tile_location[0],
					  gs.world.start_tile_location[1])
					  
	gs = save_game(gs, new=True)
	return gs


def load_game():
	# Get the list of saved games.
	saved_games = []
	for file in os.listdir(CWD):
		if file.endswith(PK):
			saved_games.append(file)
			
	# Prompt for choice of save to load
	print("Which one do you want to load?")
	for i, saved_game in enumerate(saved_games, 1):
		print("{}: {}".format(i, saved_game[:-3]))
	print("Q: Close choice.")
	choice = input("Choose a save game: ")
	savename = saved_games[int(choice)-1]
	
	print("Loading: {}".format(savename))
	return pickle.load(open(CWD + savename, "rb"))


def save_game(gs, new=False):
	if new and os.path.exists(CWD + gs.savename + PK):
		while True:
			print("{} already exists, do you want to overwrite this save?".format(gs.savename))
			ow = input("(y)es or (n)o: ")
			if ow.lower() == "n":
				print("We will not overwrite the existing save.")
				return "cancel"
			if ow.lower() == "y":
				print("Overwriting existing save.")
				pickle.dump(gs, open(CWD + gs.savename + PK, "wb"))
				return gs
			else:
				print("Invalid choice, try again.")
	elif new:
		pickle.dump(gs, open(CWD + gs.savename + PK, "wb"))
		print("New game created.")
		return gs
	elif not new and os.path.exists(CWD + gs.savename + PK):
		print("Saving game...")
		pickle.dump(gs, open(CWD + gs.savename + PK, "wb"))
		while True:
			cont = input("Game saved. Keep playing? (y)es or (n)o: ")
			if cont.lower() == "n":
				print("Quitting game...")
				exit()
			if cont.lower() == "y":
				print("Back to the game.")
				break


def launch_game():
	# initialize colorama for fluffy text colors.
	# if more things need initialization, then I will make a func.
	colorama.init()
	# intro
	menus.game_intro(VERSIONINFO)
	saves_exist = menus.check_for_saves()
	gs = None
	while True:
		start_game = menus.main_menu(saves_exist)
		if start_game == "n": # New game
			gs = new_game()
			if gs == "cancel":
				pass
			else:
				break
		if start_game == "c": # continue game
			gs = get_latest_save()
			if gs is not None:
				print("{} loaded successfully".format(gs.savename))
				break
		if start_game == "l": # load game
			gs = load_game()
			if gs is not None:
				print("Game loaded successfully")
				break
	if gs is not None:
		print("----------------")
		game_loop(gs)
	else:
		print("There was a problem with the gamestate")
		exit()


def game_loop(gs):
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


def choose_action(room, player, gs):
	action = None
	while not action:
		print("----------------")
		available_actions = playeractions.get_available_actions(room, player, gs)
		action_input = input("Action: ")
		action = available_actions.get(action_input)
		print("\n----------------")
		
		if action:
			action()
		
		# commands: help, save, wait, quests
		elif action_input.lower() == "help": 
			help_text()
			break
		elif action_input.lower() == "save":
			save_game(gs)
			break
		elif action_input.lower() == "XXXXX":
			# load
			pass
		elif action_input.lower() == "wait":
			print("You wait for one round.")
			break
		elif action_input.lower() == "quit":
			print("Quitting game.")
			exit()
			pass
		else:
			print("""
		Invalid Action!
			""")



if __name__ == "__main__":
	launch_game()

