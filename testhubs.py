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

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")

    def modify_player(self, player):
        pass
		
		
		
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
		
		
		
		
		
		
	
'''
class StartTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_dangerous = True
        self.enemy = [enemies.LargeRat(),
                      enemies.SmallGoblin()]

    def intro_text(self):
        return """\nThe stench of death and rot are all around you."""
    
    def title_text(self):
        return """This is the starting tile!"""

    def modify_player(self, player):
        attack_pool = []
        attack_pool.append(player)
        for member in player.party:
            attack_pool.append(member)
            
        if len(self.enemy) > 0:
            for number, monster in enumerate(self.enemy, 1):
                if monster.is_dead():
                    self.enemy.remove(monster)
                elif monster.is_alive():
                    chance = random.randint(1, len(attack_pool)) - 1
                    monster.attack_player(attack_pool[chance], number)
        if len(self.enemy) <= 0:
            self.is_dangerous = False
'''