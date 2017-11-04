import colorama
from colorama import Fore, Back, Style

def atkprint(text):
	print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)
	
def missprint(text):
	print(Fore.BLUE + Style.BRIGHT + text + Style.RESET_ALL)
	
def expprint(text):
	print(Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL)