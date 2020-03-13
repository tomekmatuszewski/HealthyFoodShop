from ShoppingList.utils import get_calories
class ShoppingItem:
	
	def __init__(self,name,price,nutri_per_100,weight,calories,item):
		self.name= name
		self.price = price
		self.nutri_per_100 = nutri_per_100
		self.weight = weight
		self.calories = calories
		self.item = item
		
	def get_name(self):
		return self.name
	
	def get_price(self):
		return self.price
	
	def get_nutritional_values(self):
		return self.nutri_per_100
	
	def get_calories(self):
		return self.calories
	
	def __str__(self):
		return self.name
	
	def __lt__(self, other):
		return self.calories < other.calories
	
	def __hash__(self):
		return int(len(self.name) + self.price + self.calories)

	def __eq__(self, other):
		return hash(self) == hash(other)
	
