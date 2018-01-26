import npc
import world
from collections import OrderedDict
from gameworld import testhubs
from gameworld import startdungeon

import newworld


def get_available_actions(room, player, gs):
	actions = OrderedDict()
	print("\nChoose an action: ")
	print("You: {}/{} HP | {} lv.{} | {} Exp".format(player.hp, player.max_hp, player.player_class, player.level, player.exp))
	if player.is_alive:
		action_adder(actions, 'i', player.print_inventory, "Look in backpack")
	if player.is_alive:
		action_adder(actions, 'h', player.heal, "Heal\n") #TODO Add a healing function.
	# ======= MOVEMENT COMMANDS ======= #
	if gs.world.tile_at(room.x, room.y - 1) and room.is_dangerous is False:
		action_adder(actions, 'n', player.move_north, "Go north")
	if gs.world.tile_at(room.x, room.y + 1) and room.is_dangerous is False:
		action_adder(actions, 's', player.move_south, "Go south")
	if gs.world.tile_at(room.x + 1, room.y) and room.is_dangerous is False:
		action_adder(actions, 'e', player.move_east, "Go east")
	if gs.world.tile_at(room.x - 1, room.y) and room.is_dangerous is False:
		action_adder(actions, 'w', player.move_west, "Go west")
	# ======= ATTACK COMMANDS ======= #
	if player.is_alive and room.is_dangerous:
		action_adder(actions, 'a', player.attack, "Attack")
	# ======= NPC COMMANDS ======= #
	if player.is_alive and room.npc != None and isinstance(room.npc, npc.QuestGiver):
		action_adder(actions, 't', player.talk, "Talk")
	if player.is_alive and room.npc != None and isinstance(room.npc, npc.Trader):
		action_adder(actions, 't', player.trade, "Trade")
	return actions


def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))