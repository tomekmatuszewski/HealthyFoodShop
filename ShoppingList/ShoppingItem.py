from ShoppingList.utils import get_calories
class ShoppingItem:
	
	def __init__(self,name,price,nutri_per_100,weight):
		self.name= name
		self.price = price
		self.nutri_per_100 = nutri_per_100
		self.weight = weight
		self.calories = round(get_calories(nutri_per_100,weight),0)
		
	def get_name(self):
		return self.name
	
	def get_price(self):
		return self.price
	
	def get_nutritional_values(self):
		return self.nutri_per_100
	
	def __str__(self):
		return self.name
	
	def __lt__(self, other):
		return self.calories < other.calories
	
