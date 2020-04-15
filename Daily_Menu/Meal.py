class Meal:
	
	def __init__(self, name):
		self.name = name
		self.products_list = {}

	def add_product(self, product, quantity):
		if product not in self.products_list:
			self.products_list[product] = 0
			self.products_list[product] += quantity
		else:
			self.products_list[product] += quantity
	
	def remove_product(self, product, quantity):
		self.products_list[product] -= quantity
		if self.products_list[product] <= 0:
			del self.products_list[product]
	
	def remove_item(self, product):
		del self.products_list[product]
	
	def show_products_in_meal(self):
		counter = 1
		print("{} :".format(self.name.upper()))
		for k, v in self.products_list.items():
			print('{}. {:41}\n\
	----->      {:>14} {:7.1f} g\n\
	----->      {:>15} {:7.2f} kcal\n\
	----->      {:>15} {:7.2f} g\n\
	----->      {:>15} {:7.2f} g\n\
	----->      {:>15} {:7.2f} g'.format(counter, k.name + ':', "Product weight:", float(v),
			                             "Calories:", float(k.calories) * float(v) / 100,
			                             "Proteins:", float(k.nutri_per_100["Protein(g)"]) * float(v) / 100,
			                             "Fats:", float(k.nutri_per_100["Fats(g)"]) * float(v) / 100,
			                             "Carbohydrates:", float(k.nutri_per_100["Carbo(g)"]) * float(v) / 100))
			counter += 1
		print('-' * 56)
	
	def price_of_meal(self):
		total_price = 0
		for product in self.products_list.keys():
			total_price += product.price
		return total_price
	
	def get_meal_nutri(self):
		sum_of_nutri = {"Protein(g)": 0, "Carbo(g)": 0, "Fats(g)": 0}
		for product, grams in self.products_list.items():
			sum_of_nutri["Protein(g)"] += float(product.nutri_per_100["Protein(g)"]) * round(grams / 100, 1)
			sum_of_nutri["Carbo(g)"] += float(product.nutri_per_100["Carbo(g)"]) * round(grams / 100, 1)
			sum_of_nutri["Fats(g)"] += float(product.nutri_per_100["Fats(g)"]) * round(grams / 100, 1)
		return sum_of_nutri
	
	def get_meal_calories(self):
		sum_of_calories = 0
		for product, grams in self.products_list.items():
			sum_of_calories += float(product.calories) * (grams / 100)
		return round(sum_of_calories, 1)
	
	def get_meal_name(self):
		return self.name
	
	def __getitem__(self, key):
		return list(self.products_list.keys())[key]
	
	def __len__(self):
		return len(list(self.products_list.keys()))


