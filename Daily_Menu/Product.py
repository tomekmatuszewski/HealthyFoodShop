from ShoppingList.Database_food import food, categories


class Product:
	
	def __init__(self, name, price, nutri_per_100, weight, calories, unit):
		self.name = name
		self.price = price
		self.nutri_per_100 = nutri_per_100
		self.weight = weight
		self.calories = calories
		self.unit = unit
		self.grams = 0
	
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
	def create_product(cls, index_number, category):
		product = food.loc[(categories[category - 1], index_number), "Product"]
		price = food.loc[(categories[category - 1], index_number), "Price[PLN]"]
		nutritional_values = {"Protein(g)": food.loc[(categories[category - 1], index_number), "Protein(g)"],
		                      "Fats(g)": food.loc[(categories[category - 1], index_number), "Fats(g)"],
		                      "Carbo(g)": food.loc[(categories[category - 1], index_number), "Carbo(g)"]}
		weight = food.loc[(categories[category - 1], index_number), "Weight_pcs/pack[g]"]
		calories = food.loc[(categories[category - 1], index_number), "Kcal"]
		unit = food.loc[(categories[category - 1], index_number), "unit"]
		return Product(product, price, nutritional_values, weight, calories, unit)
