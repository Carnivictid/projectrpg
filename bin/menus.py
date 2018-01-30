# Basic info for menues. To reduce clutter.
import getpass
import os



def enter_to_continue():
	getpass.getpass("Press Enter to Continue...")


def game_intro(VERSIONINFO, display=True):
	if display:
		os.system("cls")

		print("-=(ProjectRPG)=- [Version {}]".format(VERSIONINFO))
		print("Copyright (c) 2018 Shelby Banfield. All rights reserved.\n")
		
		print("Welcome to ProjectRPG. A D&D Text Adventure made for one person.\n")
		
		print("\nDear, Player...\n")
		print("  This game is a passion project that has no real end goal.")
		print("I am using this as a platform to learn and play with Python.")
		print("If you have any suggestions or comments, please email me at")
		print("ShelbyBanfield@gmail.com or message me on github. You can see")
		print("the source code at https://github.com/carnivictid/projectrpg\n")
		print("If you are playing this and you are not me, please enjoy!\n\n\n")
		
		enter_to_continue()
		os.system("cls")


def check_for_saves():
	fn = os.listdir(os.path.dirname(os.getcwd())+"\\rpg\\saves\\")
	for f in fn:
		if f.endswith(".pk"):
			return True
	return False


def get_latest_savename():
	return "NULL"


def main_menu(saves_exist):
	print("-=(ProjectRPG)=-\n")
	
	choices = {}
	if saves_exist:
		choices.update({
			"C": "Continue Last Game",
			"L": "Load Saved Game"})
	choices.update({
		"N": "Start New Game",
		"Q": "Quit Game"})
	
	while True:
		for key, value in choices.items():
			print("{}) {}".format(key, value))
		
		choice = input("\nChoice: ")
		
		if choice.upper() == "Q":
			print("\nQuitting game...")
			exit()
		if choice.upper() == "N":
			print("\nStarting new game!")
			return "n"
		if choice.upper() == "C" and choice.upper() in choices.keys():
			print("\nContinuing game!")
			return "c"
		if choice.upper() == "L" and choice.upper() in choices.keys():
			print("\nLoading a previous save!")
			return "l"
		else:
			print("\nInvalid choice, please try again.\n")



if __name__ == "__main__":
	game_intro("POOP")




