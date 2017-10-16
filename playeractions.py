import world, testhubs
from collections import OrderedDict


def get_available_actions(room, player):
    actions = OrderedDict()
    print("\nChoose an action: ")
    print("You: {}/{} HP | {} Gold".format(player.hp, player.max_hp, player.gold))
    if player.is_alive:
        action_adder(actions, 'i', player.print_inventory, "Look in backpack")
    if player.is_alive:
        action_adder(actions, 'h', player.wait, "Heal\n") #TODO Add a healing function.
    # ======= MOVEMENT COMMANDS ======= #
    if world.tile_at(room.x, room.y - 1) and room.is_dangerous is False:
        action_adder(actions, 'n', player.move_north, "Go north")
    if world.tile_at(room.x, room.y + 1) and room.is_dangerous is False:
        action_adder(actions, 's', player.move_south, "Go south")
    if world.tile_at(room.x + 1, room.y) and room.is_dangerous is False:
        action_adder(actions, 'e', player.move_east, "Go east")
    if world.tile_at(room.x - 1, room.y) and room.is_dangerous is False:
        action_adder(actions, 'w', player.move_west, "Go west")
	# ======= ATTACK COMMANDS ======= #
    if player.is_alive and room.is_dangerous:
        action_adder(actions, 'a', player.attack, "Attack")
    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))