from random import randint
import map


class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{}: {}D{} / {} x {} Crit".format(
                self.name, self.dice_amount, self.dice_number, self.crit_range, self.crit_multi)


class Armor:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{}: {} AC / {} max Dex".format(self.name, self.ac_bonus, self.max_dex)


class Shield:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{}: {} AC".format(self.name, self.ac_bonus)


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return self.name + ': ' + self.heals


class Item:
    def __init__(self):
        raise NotImplementedError("Do not create raw Item objects.")

    def __str__(self):
        return "{}".format(self.name)

# ======= The following classes are weapons!


class Fists(Weapon):
    def __init__(self):
        self.name = "Fists"
        self.dice_amount = 1
        self.dice_number = 4
        self.crit_range = 20
        self.crit_multi = 2


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.dice_amount = 1
        self.dice_number = 4
        self.crit_range = 19
        self.crit_multi = 2
        self.value = 2


class ShortSword(Weapon):
    def __init__(self):
        self.name = "Short Sword"
        self.dice_amount = 1
        self.dice_number = 6
        self.crit_range = 19
        self.crit_multi = 2
        self.value = 10


class Rapier(Weapon):
    def __init__(self):
        self.name = "Rapier"
        self.dice_amount = 1
        self.dice_number = 6
        self.crit_range = 18
        self.crit_multi = 2
        self.value = 20


class Longsword(Weapon):
    def __init__(self):
        self.name = "Longsword"
        self.dice_amount = 1
        self.dice_number = 8
        self.crit_range = 19
        self.crit_multi = 2
        self.value = 15


class DwarvenWarAxe(Weapon):
    def __init__(self):
        self.name = "Dwarven War Axe"
        self.dice_amount = 1
        self.dice_number = 10
        self.crit_range = 20
        self.crit_multi = 3
        self.value = 30


# ======= The following classes are armor!
# === Light Armor === #
class PaddedArmor(Armor):
    def __init__(self):
        self.name = "Padded Shirt"
        self.ac_bonus = 1
        self.max_dex = 8
        self.value = 5


class LeatherArmor(Armor):
    def __init__(self):
        self.name = "Leather Shirt"
        self.ac_bonus = 2
        self.max_dex = 6
        self.value = 10


class StuddedLeather(Armor):
    def __init__(self):
        self.name = "Studded Leather"
        self.ac_bonus = 3
        self.max_dex = 5
        self.value = 25


class ChainShirt(Armor):
    def __init__(self):
        self.name = "Chain Shirt"
        self.ac_bonus = 4
        self.max_dex = 4
        self.value = 100


# === Medium Armor === #
class HideArmor(Armor):
    def __init__(self):
        self.name = "Hide Armor"
        self.ac_bonus = 3
        self.max_dex = 4
        self.value = 15


class ScaleMail(Armor):
    def __init__(self):
        self.name = "Scale Mail"
        self.ac_bonus = 3
        self.max_dex = 4
        self.value = 50


class ChainMail(Armor):
    def __init__(self):
        self.name = "Chain Mail"
        self.ac_bonus = 5
        self.max_dex = 2
        self.value = 150


class BreastPlate(Armor):
    def __init__(self):
        self.name = "Breastplate Armor"
        self.ac_bonus = 5
        self.max_dex = 4
        self.value = 200


# === Heavy Armor === #
class SplintMail(Armor):
    def __init__(self):
        self.name = "Splint Mail"
        self.ac_bonus = 6
        self.max_dex = 0
        self.value = 200


class BandedMail(Armor):
    def __init__(self):
        self.name = "Banded Mail"
        self.ac_bonus = 6
        self.max_dex = 1
        self.value = 250


class HalfPlate(Armor):
    def __init__(self):
        self.name = "Half Plate"
        self.ac_bonus = 7
        self.max_dex = 0
        self.value = 600


class FullPlate(Armor):
    def __init__(self):
        self.name = "Full Plate"
        self.ac_bonus = 8
        self.max_dex = 1
        self.value = 1500


# ======= The following classes are shields!
class BucklerShield(Shield):
    def __init__(self):
        self.name = "Buckler"
        self.ac_bonus = 1
        self.value = 15


class HeavySteelShield(Shield):
    def __init__(self):
        self.name = "Heavy Steel Shield"
        self.ac_bonus = 2
        self.value = 20


# ======= The following classes are other items!
class LightHealingPotion(Consumable):
    def __init__(self):
        self.name = "Potion of Cure Light Wounds"
        self.heals = "1D8 + 1"
        self.healing_value = randint(1, 8) + 1
        self.value = 50

