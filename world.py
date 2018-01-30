import map
from gameworld import conceptmap


class WorldClass:
	def __init__(self):
		self.world_dsl = map.map
		self.world_map = []
		self.start_tile_location = None
		
		self.STARTING_TILE = conceptmap.StartingTile
		self.VICTORY_TILE = conceptmap.VictoryTile

		# Could change this to a new file alltogether. 
		# World.py shouldn't have anything else added to it.
		self.tile_type_dict = {
			"STT": self.STARTING_TILE,
			"VYT": self.VICTORY_TILE,
			"ST1": conceptmap.Tile1,
			"ST2": conceptmap.Tile2,
			"ST3": conceptmap.Tile3,
			"ST4": conceptmap.Tile4,
			"ST5": conceptmap.Tile5,
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