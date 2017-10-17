import items
#import npc
import random
import enemies
#import cinematics


#========== Blank Maptile Class ==========#
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.round_count = 0
        self.is_dangerous = False
        self.enemy = []

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
                    print("The monster gives you {} exp!".format(monster.exp))
                    self.enemy.remove(monster)
        for number, monster in enumerate(self.enemy, 1):
            if monster.is_dead():
                self.enemy.remove(monster)
        if len(self.enemy) <= 0:
            self.is_dangerous = False
            
		
		
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
		return """\n\nYou see a bright light in the distance...\n... it grows as you get closer! It's sunlight!\n\nVictory is yours!"""
		
	def title_text(self):
		return """\nHere is the title text.\n"""

	def modify_player(self, player):
		player.victory = True		
		
		
#========== Enemy tile for testing. ==========#		
class EnemyTile(MapTile): #TODO Work on combat
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dangerous = True
        self.enemy = [enemies.LargeRat(),
                      enemies.LargeRat()]
        
    def intro_text(self):
        return """\n\nA monster is in this tile! Aaahhh!"""
    
    def title_text(self):
        return """\nHere is the title text.\n"""

    def modify_player(self, player):
        self.enemy_attacks(player)
    
    
