class Fighter:
	def __init__(self):	   
		self.hit_dice = 10
		self.base_attack = {1: 1,
							2: 2,
							3: 3,
							4: 4,
							5: 5,
							6: 6,
							7: 7,
							8: 8,
							9: 9,
							10: 10,
							11: 11,
							12: 12,
							13: 13,
							14: 14,
							15: 15,
							16: 16,
							17: 17,
							18: 18,
							19: 19,
							20: 20
							}
							
		self.base_fort_save = {1: 2,
							   2: 3,
							   3: 3,
							   4: 4,
							   5: 4,
							   6: 5,
							   7: 5,
							   8: 6,
							   9: 6,
							   10: 7,
							   11: 7,
							   12: 8,
							   13: 8,
							   14: 9,
							   15: 9,
							   16: 10,
							   17: 10,
							   18: 11,
							   19: 11,
							   20: 12
							   }
							   
		self.base_ref_save = {1: 0,
							  2: 0,
							  3: 1,
							  4: 1,
							  5: 1,
							  6: 2,
							  7: 2,
							  8: 2,
							  9: 3,
							  10: 3,
							  11: 3,
							  12: 4,
							  13: 4,
							  14: 4,
							  15: 5,
							  16: 5,
							  17: 5,
							  18: 6,
							  19: 6,
							  20: 6
							   }
							   
		self.base_will_save = {1: 0,
							   2: 0,
							   3: 1,
							   4: 1,
							   5: 1,
							   6: 2,
							   7: 2,
							   8: 2,
							   9: 3,
							   10: 3,
							   11: 3,
							   12: 4,
							   13: 4,
							   14: 4,
							   15: 5,
							   16: 5,
							   17: 5,
							   18: 6,
							   19: 6,
							   20: 6
							   }
							   
	def __str__(self):
		return 'Fighter'
							   
	def level_up(self, level):
		bab = self.base_attack[level]
		fort = self.base_fort_save[level]
		ref = self.base_ref_save[level]
		will = self.base_fort_save[level]
		level = level
		
		return level, bab, fort, ref, will













