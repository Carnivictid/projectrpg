import items
import random
import enemies
import npc
import quests
from .testhubs import MapTile


map = """
|   |   |MC9|   |WH2|   |WH5|
|MCD|MC7|MC6|MC8|WH1|WH3|WH4|
|   |   |MC5|   |   |   |WH6|
|   |MC3|MC2|MC4|   |   |WH7|
|   |   |MC1|   |   |   |   |
|   |   |SD4|   |   |   |   |
|   |   |SD3|S3B|   |   |   |
|   |S2B|SD2|   |   |   |   |
|   |   |SD1|   |   |VYT|STT|
"""

"""
"MC1": starttown.MaencarCoasts1,
"MC2": starttown.MaencarCoasts2,
"MC3": starttown.MaencarCoasts3,
"MC4": starttown.MaencarCoasts4,
"MC5": starttown.MaencarCoasts5,
"MC6": starttown.MaencarCoasts6,
"MC7": starttown.MaencarCoasts7,
"MC8": starttown.MaencarCoasts8,
"MC9": starttown.MaencarCoasts9,

"MCD": starttown.MaencarDock,

"MC1": starttown.Warehouse1,
"MC2": starttown.Warehouse2,
"MC3": starttown.Warehouse3,
"MC4": starttown.Warehouse4,
"MC5": starttown.Warehouse5,
"MC6": starttown.Warehouse6,
"MC7": starttown.Warehouse7,
"""

#========== Start Town, Maencar Coast! ==========#
class MaencarCoasts1(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts1"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts1"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts2(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts2"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts2"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts3(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts3"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts3"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts4(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts4"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts4"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts5(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts5"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts5"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts6(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts6"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts6"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts7(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts7"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts7"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts8(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts8"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts8"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarCoasts9(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarCoasts9"""
		
	def title_text(self):
		return """This is the title_text for MaencarCoasts9"""
		
	def modify_player(self, player):
		self.round_count += 1


class MaencarDock(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for MaencarDock"""
		
	def title_text(self):
		return """This is the title_text for MaencarDock"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse1(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse1"""
		
	def title_text(self):
		return """This is the title_text for Warehouse1"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse2(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse2"""
		
	def title_text(self):
		return """This is the title_text for Warehouse2"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse3(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse3"""
		
	def title_text(self):
		return """This is the title_text for Warehouse3"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse4(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse4"""
		
	def title_text(self):
		return """This is the title_text for Warehouse4"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse5(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse2"""
		
	def title_text(self):
		return """This is the title_text for Warehouse2"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse6(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse3"""
		
	def title_text(self):
		return """This is the title_text for Warehouse3"""
		
	def modify_player(self, player):
		self.round_count += 1


class Warehouse7(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		
	def intro_text(self):
		return """This is the intro_text for Warehouse4"""
		
	def title_text(self):
		return """This is the title_text for Warehouse4"""
		
	def modify_player(self, player):
		self.round_count += 1

