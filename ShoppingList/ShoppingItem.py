class ShoppingItem:
	
	def __init__(self,name,price,nutri_per_100):
		self.name = name
		self.price = price
		self.nutri_per_100 = nutri_per_100
		

	def get_name(self):
		return self.name
	
	def get_price(self):
		return self.price
	
	def get_nutritional_values(self):
		return self.nutri_per_100
