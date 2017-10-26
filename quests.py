import world
import items

# Quests... How do we handle this.....
"""
What is needed for a quest?
Name, gold, exp, item rewards

Quest start location
Quest start requirements

Quest finish requirements
Quest failed requirements

If it has been accepted
Quest dialogue
"""



class Quest:
    def __init__(self):
        raise NotImplementedError("Do not create raw quest classes")
        
    def __str__(self):
        return self.quest_name


class NoobQuest(Quest):
    def __init__(self):
        self.quest_name = None
        self.reward_gold = 250
        self.reward_exp = 500
        self.reward_item = [items.Longsword()]