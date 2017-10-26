import items
#import npc
import random
import enemies
#import cinematics
import npc


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
                    player.exp += monster.exp
                    print("\nThe monster gives you {} exp!".format(monster.exp))
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
        return """\n\nThis is the starting tile. This is intro text."""
        
    def title_text(self):
        return """\nHere is the title text.\n"""
        
    def modify_player(self, player):
        self.round_count += 1
        if self.round_count >= 2:
            print("What are you doing just standing around?")
        else:
            return
		
		
#========== Victory tile for testing. ==========#
class VictoryTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		return """\n\nYou see a bright light in the distance...\n... it grows as you get closer! It's sunlight!"""
		
	def title_text(self):
		return """\nVictory is yours!\n"""

	def modify_player(self, player):
		player.victory = True		
		
		
#========== Enemy tile for testing. ==========#		
class EnemyTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dangerous = True
        self.enemy = [enemies.LargeRat()]
        self.reinforced = 0
        
    def intro_text(self):
        return """\nThis is the intro_text!"""
    
    def title_text(self):
        return """\nThis is the title_text!"""

    def modify_player(self, player):
        self.enemy_attacks(player)
        

#========== Trader tile for testing. ==========#
class TraderTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.npc = npc.Trader()

    def intro_text(self):
        return """\nThere is a trader on this tile"""
        
    def title_text(self):
        return """\nTraders don't like to be kept waiting."""


#========== Quest tile for testing. ==========#
class QuestTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.npc = npc.QuestGiver()
        
    def intro_text(self):
        return """\nThere is a guy here who looks like he wants to talk."""
        
    def title_text(self):
        return """\nMaybe you should talk to him."""




