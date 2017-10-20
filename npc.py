import items


class NPC():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects")
        
    def __str__(self):
        return self.name
        
        
class Trader(NPC):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.trade_inventory = [items.LightHealingPotion(),
                                items.LightHealingPotion(),
                                items.LightHealingPotion()]