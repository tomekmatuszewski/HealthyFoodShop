from ShoppingList.Database_food import food, categories


class ShoppingItem:
	
	def __init__(self, name, price, nutri_per_100, weight, calories, unit):
		self.name = name
		self.price = price
		self.nutri_per_100 = nutri_per_100
		self.weight = weight
		self.calories = calories
		self.unit = unit
		
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
	
	@classmethod
	def create_warehouse_item(cls, category, number):
		product = food.loc[(category, number + 1), "Product"]
		price = food.loc[(category, number + 1), "Price[PLN]"]
		nutritional_data = {"Protein(g)": food.loc[(category, number + 1), "Protein(g)"],
		                     "Fats(g)": food.loc[(category, number + 1), "Fats(g)"],
		                     "Carbo(g)": food.loc[(category, number + 1), "Carbo(g)"]}
		weight = food.loc[(category, number + 1), "Weight[g/ml]"]
		calories = food.loc[(category, number + 1), "Kcal"]
		unit = food.loc[(category, number + 1), "Kcal"], food.loc[(category, number + 1), "unit"]
		return ShoppingItem(product, price, nutritional_data, weight, calories, unit)
	
	@classmethod
	def create_shopping_item(cls, category, index_number):
		product = food.loc[(categories[category - 1], index_number), "Product"]
		price = food.loc[(categories[category - 1], index_number), "Price[PLN]"]
		nutritional_values = {"Protein(g)": food.loc[(categories[category - 1], index_number), "Protein(g)"],
		 "Fats(g)": food.loc[(categories[category - 1], index_number), "Fats(g)"],
		 "Carbo(g)": food.loc[(categories[category - 1], index_number), "Carbo(g)"]}
		weight = food.loc[(categories[category - 1], index_number), "Weight[g/ml]"]
		calories = food.loc[(categories[category - 1], index_number), "Kcal"]
		unit = food.loc[(categories[category - 1], index_number), "unit"]
		return ShoppingItem(product, price, nutritional_values, weight, calories, unit)
		
		
		
		
		













