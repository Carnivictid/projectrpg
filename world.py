import map
from gameworld import testhubs
from gameworld import startdungeon
from gameworld import starttown
#import .gameworld.testhubs
#import .gameworld.startdungeon


world_dsl = map.map
world_map = []
start_tile_location = None

STARTING_TILE = startdungeon.StartDungeon1 #testhubs.StartingTile
VICTORY_TILE = testhubs.VictoryTile

# Could change this to a new file alltogether. 
# World.py shouldn't have anything else added to it.
tile_type_dict = {"STT": STARTING_TILE,
				  "VYT": VICTORY_TILE,
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

				  
def is_dsl_valid(dsl):
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


def parse_world_dsl():
	if not is_dsl_valid(world_dsl):
		raise SyntaxError("DSL is invalid!")

	dsl_lines = world_dsl.splitlines()
	dsl_lines = [x for x in dsl_lines if x]

	for y, dsl_row in enumerate(dsl_lines):
		row = []
		dsl_cells = dsl_row.split("|")
		dsl_cells = [c for c in dsl_cells if c]
		for x, dsl_cell in enumerate(dsl_cells):
			tile_type = tile_type_dict[dsl_cell]
			if tile_type == STARTING_TILE:
				global start_tile_location
				start_tile_location = x, y
			row.append(tile_type(x, y) if tile_type else None)
		world_map.append(row)


def tile_at(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None