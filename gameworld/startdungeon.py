import items
import random
import enemies
import npc
import quests
from .testhubs import MapTile
#from testhubs import MapTile


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
		if self.round_count == 0:
			return """\nYou walk forward, your boots sinking into the mud, causing your steps
to make sucking noises. As you move forward, you notice a light peaking
through the dim haze in the sewer.\n"""
		else:
			return """\nA dead rat lies on the ground.\n"""
		
	def title_text(self):
		if self.is_dangerous:
			return """\nA massive rat leaps at you from the shadows!\n"""
		if not self.is_dangerous:
			return  """\nThe sewer stretches North and South. There is a T junction going West. \n"""
		
	def modify_player(self, player):
		self.enemy_attacks(player)
		self.round_count += 1

		
# StartDungeon2b S2B - bandages
class StartDungeon2b(MapTile): # tile_dict name: S2B
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		if self.round_count == 0:
			return """\nYou walk east and are stopped by a rusty metal grate. You look around
and see an old leather bag on the ground. Inside the bag, you find a
small roll of bandages. You place them in your bag.\n"""
		else:
			return """/nThe sewer goes on to the West, but is blocked off by a grate./n"""
		
	def title_text(self):
		return """\nA faint dripping noise can be heard beyond the sewer grate.\n"""
		
	def modify_player(self, player):
		if self.round_count == 0:
			player.item_inventory.append(items.LightBandage())
		self.round_count += 1

		
# StartDungeon3  SD3 - fluff text, rat fight if entered s3b
class StartDungeon3(MapTile): # tile_dict name: SD3
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		if quests.spawn_rat == 1:
			self.enemy.append(enemies.LargeRat())
			self.is_dangerous = True
			quests.spawn_rat = 2
		if self.is_dangerous:
			return """\nYou hear a scurring sound as you walk through the sewer. The echo makes
it hard to tell where it is coming from, but you can tell whatever
it is is getting closer!\n"""
		elif quests.spawn_rat == 0:
			return """\nYou make your way through the sewer.\n"""
		elif quests.spawn_rat == 2:
			return """\nYou make your way through the sewer. A dead rat lies in the muck.\n"""
		
	def title_text(self):
		if self.is_dangerous:
			return """\nA large rat leaps at you from the shadows\n"""
		else:
			return """\nThe sewer goes North and South. A T-Junction splits off to the East.\n"""
		
	def modify_player(self, player):		
		if len(self.enemy) > 0:
			self.enemy_attacks(player)
		self.round_count += 1

		
# StartDungeon3b S3B - gold, trigger fight in sd3
class StartDungeon3b(MapTile): # tile_dict name: S3B
	def __init__(self, x, y):
		super().__init__(x, y)

	def intro_text(self):
		if self.round_count == 0:
			return """\nYou walk for a short way, but the path is blocked by antoher sewer grate.
You look around and notice a grimy coin purse on the ground. You grab the purse
and open it. There is some gold in the bag. You take it.\n"""
		else:
			return """\nThe sewer dead ends here. A grate is blocking the path.\n"""
		
	def title_text(self):
		return """\nThe sewers behind this grate are very dark. You can't see but 5 feet past it.\n"""
		
	def modify_player(self, player):
		if self.round_count == 0:
			quests.spawn_rat = 1
			player.gold += random.randint(10, 25)
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