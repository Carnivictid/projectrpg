import map
from gameworld import testhubs
from gameworld import startdungeon
from gameworld import starttown
#import .gameworld.testhubs
#import .gameworld.startdungeon

# TODO: Make this a class for pickeling so we can save games.



class WorldClass:
	def __init__(self):
		self.world_dsl = map.map
		self.world_map = []
		self.start_tile_location = None
		
		self.STARTING_TILE = startdungeon.StartDungeon1 #testhubs.StartingTile
		self.VICTORY_TILE = testhubs.VictoryTile

		# Could change this to a new file alltogether. 
		# World.py shouldn't have anything else added to it.
		self.tile_type_dict = {"STT": self.STARTING_TILE,
							   "VYT": self.VICTORY_TILE,
							   "ENT": testhubs.EnemyTile,
							   "TRT": testhubs.TraderTile,
							   "QGT": testhubs.QuestTile,
							   "SD1": startdungeon.StartDungeon1,
							   "SD2": startdungeon.StartDungeon2,
							   "S2B": startdungeon.StartDungeon2b,
							   "SD3": startdungeon.StartDungeon3,
							   "S3B": startdungeon.StartDungeon3b,
							   "SD4": startdungeon.StartDungeon4,
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
							   "WH1": starttown.Warehouse1,
							   "WH2": starttown.Warehouse2,
							   "WH3": starttown.Warehouse3,
							   "WH4": starttown.Warehouse4,
							   "WH5": starttown.Warehouse5,
							   "WH6": starttown.Warehouse6,
							   "WH7": starttown.Warehouse7,
							   "   ": None}
		self.parse_world_dsl()

		
	def check_start_tile(self):
		if self.start_tile_location is None:
			print("World did not parse, shutting down.")
			exit()
	
	def is_dsl_valid(self, dsl):
		if dsl.count("|STT|") != 1:
			return False
		if dsl.count("|VYT|") == 0:
			return False
		lines = dsl.splitlines()
		lines = [l for l in lines if l]
		pipe_counts = [line.count("|") for line in lines]
		for count in pipe_counts:
			if count != pipe_counts[0]:
				return False
		return True


	def parse_world_dsl(self):
		if not self.is_dsl_valid(self.world_dsl):
			raise SyntaxError("DSL is invalid!")

		dsl_lines = self.world_dsl.splitlines()
		dsl_lines = [x for x in dsl_lines if x]

		for y, dsl_row in enumerate(dsl_lines):
			row = []
			dsl_cells = dsl_row.split("|")
			dsl_cells = [c for c in dsl_cells if c]
			for x, dsl_cell in enumerate(dsl_cells):
				tile_type = self.tile_type_dict[dsl_cell]
				if tile_type == self.STARTING_TILE:
					self.start_tile_location = x, y
				row.append(tile_type(x, y) if tile_type else None)
			self.world_map.append(row)


	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.world_map[y][x]
		except IndexError:
			return None