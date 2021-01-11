acceptableTypes = ['consumable', 'deployable', 'key']
acceptableActions = ['buff', 'open', 'deploy']


import Buffs

def CheckVal(AcceptableValues, Value, Debug):
	#TODO: Make it so that the value type in debug message is customisable
	if not Value in AcceptableValues:
		if Debug:
			print('Invalid Value: %s'%Value)
		Value = None
		return Value
	elif Debug:
		print('Value set to %s'%Value)
	
	
class Item:
	def __init__(self, Type, Action, ActionType, Value1, Value2, Debug):
		
		#Assign the initiation values to the class
		self.Type = Type
		self.Action = Action
		self.ActionType = ActionType
		self.Value1 = Value1
		self.Value2 = Value2
		self.Debug = Debug
		'''
		#Check that the Item Type is in allowed
		if not self.Type in acceptableTypes:
			if self.Debug:
				print('Invalid Type: %s'%self.Type)
			self.Type = None
		elif self.Debug:
			print('Type set to %s'%self.Type)
		'''
		#Check Item Type
		CheckVal(acceptableTypes, self.Type, self.Debug)
		
		'''#Check the Action is acceptable
		if not self.Action in acceptableActions:
			if self.Debug:
				print('Invalid Action: %s'%self.Action)
			self.Type = None
		elif self.Debug:
			print('Action set to %s'%self.Action)'''
		#Check Item Action on Use
		CheckVal(acceptableActions, self.Action, self.Debug)
		
		if self.Action == 'buff':
			CheckVal(Buffs.acceptableBuffs, self.ActionType, self.Debug)
			
			
	def use(self, entityUsedBy):
		self.entityUsedBy = entityUsedBy
		if self.Action == 'buff':
			#Buffs.buffs.applyEffect(self.ActionType, self.Value1, self.Value2)
			print(f'Applied {self.ActionType} to {self.entityUsedBy} for {self.Value2} seconds at {self.Value1} multiplier due to consumed ITEM.')	


	def remove(self):
		return


Food = Item('consumable', 'buff', 'regen', 15, 5, True)
Food.use('Player')
