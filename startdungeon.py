import items
import random
import enemies
import npc
import quests
from testhubs import MapTile


"""
|   |   |   |   |
|   |SD4|   |   |
|   |SD3|S3B|   |
|S2B|SD2|   |   |
|   |SD1|   |   |
|   |   |   |   |
"""

#========== Start Dungeon! ==========#
# StartDungeon1  SD1 - start
class StartDungeon1(MapTile): # tile_dict name: SD1
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		if self.round_count == 0:
			return """\nYou feel the soft, cold ground beneath you, but it's too dark to see.
You realize quickly that this is because your eyes are closed.
You open your eyes, and the dim light reminds you of a sharp 
pain in your head. You are on the ground, your head pounding. 
You sit up and look around. You appear to be in a sewer.\n"""
		else:
			return """\nYou see the grate to the south. The sewer continues north.\n"""
		
	def title_text(self):
		if self.round_count == 0:
			return """\nYou stand up, and pick up your small backpack. You look behind you, to the 
south, and see the sewer is blocked off by a grate. You notice something
shining in the muck behind the bars. You reach through and try to grab
it. You pull it free and it makes a wet sucking noise. Its a rusty sword.
You put it in your bag.\n"""
		else:
			return """\nYou should press onward.\n"""
		
	def modify_player(self, player):
		if self.round_count == 0:
			player.item_inventory.append(items.RustySword())
		self.round_count += 1

		
# StartDungeon2  SD2 - rat fight
class StartDungeon2(MapTile): # tile_dict name: SD2
	def __init__(self, x, y):
		super().__init__(x, y)
		self.enemy = [enemies.LargeRat()]
		self.is_dangerous = True

	def intro_text(self):
		return """\nHere is the intro_text.\n"""
		
	def title_text(self):
		return """\nHere is the title_text.\n"""
		
	def modify_player(self, player):
		self.enemy_attacks(player)
		self.round_count += 1

		
# StartDungeon2b S2B - bandages
class StartDungeon2b(MapTile): # tile_dict name: S2B
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		return """\nHere is the intro_text.\n"""
		
	def title_text(self):
		return """\nHere is the title_text.\n"""
		
	def modify_player(self, player):
		self.round_count += 1

		
# StartDungeon3  SD3 - fluff text, rat fight if entered s3b
class StartDungeon3(MapTile): # tile_dict name: SD3
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		return """\nHere is the intro_text.\n"""
		
	def title_text(self):
		return """\nHere is the title_text.\n"""
		
	def modify_player(self, player):
		self.round_count += 1

		
# StartDungeon3b S3B - gold, trigger fight in sd3
class StartDungeon3b(MapTile): # tile_dict name: S3B
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		return """\nHere is the intro_text.\n"""
		
	def title_text(self):
		return """\nHere is the title_text.\n"""
		
	def modify_player(self, player):
		self.round_count += 1


# StartDungeon4  SD4 - manhold to escape dungeon
class StartDungeon4(MapTile): # tile_dict name: SD4
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		return """\nHere is the intro_text.\n"""
		
	def title_text(self):
		return """\nHere is the title_text.\n"""
		
	def modify_player(self, player):
		self.round_count += 1