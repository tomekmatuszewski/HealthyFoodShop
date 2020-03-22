from collections import Counter


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


class Meal(Product):
	
	def __init__(self, name):
		self.name = name
		self.products_list = {}
	
	def add_product(self, product, grams):
		if product not in self.products_list:
			self.products_list[product] = 0
			self.products_list[product] += grams
		else:
			self.products_list[product] += grams
	
	def remove_product(self, product, grams):
		self.products_list[product] -= grams
		if self.products_list[product] <= 0:
			del self.products_list[product]
	
	def show_products_in_meal(self):
		counter = 1
		print(self.name)
		for k, v in self.products_list.items():
			print("{}. {}: {}g. ".format(counter, k, v))
			counter += 1
	
	def price_of_meal(self):
		total_price = 0
		for product in self.products_list.keys():
			total_price += product.price
		return
	
	def get_meal_nutri(self):
		sum_of_nutri = Counter({})
		for product in self.products_list.keys():
			sum_of_nutri += Counter(product.nutri_per_100)
		return dict(sum_of_nutri)
	
	def get_meal_calories(self):
		sum_of_calories = 0
		for product in self.products_list.keys():
			sum_of_calories += product.calories * (product.grams/100)
		return round(sum_of_calories, 0)


class Menu(Meal):
	
	possible_set_meals = {1: ["Breakfast", "Dinner", "Supper"], 2: ["Breakfast", "Lunch", "Dinner", "Supper"],
	                      3: ["Breakfast", "Lunch", "Dinner", "Afternoon snack", "Supper"]}
	
	def __init__(self, max_calories, max_carbo, max_protein, max_fats):
		self.max_calories = max_calories
		self.max_carbo = max_carbo
		self.max_protein = max_protein
		self.max_fats = max_fats
		self.menu_list = []
		self.quantity_of_meals = None
	
	def add_meal(self, meal):
		if len(self.menu_list) > self.quantity_of_meals:
			print("Max. quantity of meals is {}.".format(self.quantity_of_meals))
		self.menu_list.append(meal)
	
	def get_menu_info(self):
		for meal in self.menu_list:
			meal.show_products_in_meal()
			print("Nutritional values of {}: {}.".format(meal.name, meal.get_meal_nutri()))
			print("Amount of calories in {}: {} kcal".format(meal.name, meal.get_meal_calories()))
		print("\n")

