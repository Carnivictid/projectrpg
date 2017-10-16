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

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")

    def modify_player(self, player):
        pass
		
		
		
#========== Starting tile for testing. ==========#
class StartingTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.round_count = 0
        self.is_dangerous = False
        
    def intro_text(self):
        return """\nThis is the starting tile. This is intro text."""
        
    def title_text(self):
        return """\nHere is the title text."""
        
    def modify_player(self, player):
        self.round_count += 1
        if self.round_count == 2:
            print("What are you doing just standing around?")
        else:
            return
		
		
#========== Victory tile for testing. ==========#
class VictoryTile(MapTile):
	def modify_player(self, player):
		player.victory = True

	def intro_text(self):
		return """
		You see a bright light in the distance...
		... it grows as you get closer! It's sunlight!

		Victory is yours!
		"""
	def title_text(self):
		return """\nHere is the title text."""