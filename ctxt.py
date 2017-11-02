import colorama
from colorama import Fore, Back, Style

def atkprint(text):
	print(Back.RED + Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)
	
def missprint(text):
	print(Back.BLUE + text + Style.RESET_ALL)