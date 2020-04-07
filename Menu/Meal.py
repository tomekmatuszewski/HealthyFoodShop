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
			
	def remove_item(self, product):
		del self.products_list[product]
	
	def show_products_in_meal(self):
		counter = 1
		print('*' * 150)
		print(self.name)
		for k, v in self.products_list.items():
			print("{}. {}: {}g, proteins: {} g., carbohydrates: {} g., fats: {} g., calories: {} kcal: ".format(counter, k, v,
			                    round(float(k.nutri_per_100["Protein(g)"])*v/100, 1), round(float(k.nutri_per_100["Carbo(g)"])*v/100, 1),
			                    round(float(k.nutri_per_100["Fats(g)"])*v/100, 1), round(float(k.calories)*v/100, 1)))
			counter += 1
		print('*' * 150)
	
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
			sum_of_calories += float(product.calories) * (grams/100)
		return round(sum_of_calories, 1)
	
	def get_meal_name(self):
		return self.name
	
	def __getitem__(self, key):
		return list(self.products_list.keys())[key]
	
	def __len__(self):
		return len(list(self.products_list.keys()))
	
	
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
		
	def get_meals_names(self):
		counter = 1
		print("Your daily meals: ")
		for meal in self.menu_list:
			print("{} : {}{}".format(counter, meal.name, ", {} product{} added".format(len(meal.products_list.keys()),
			    "s" if len(meal.products_list.keys()) > 1 else "") if len(meal.products_list.keys()) else ""))
			counter += 1
	
	def get_menu_calories(self):
		total_calories = 0
		for meal in self.menu_list:
			total_calories += meal.get_meal_calories()
		return round(total_calories, 2)
	
	def get_menu_proteins(self):
		total_proteins = 0
		for meal in self.menu_list:
			total_proteins += meal.get_meal_nutri()["Protein(g)"]
		return round(total_proteins, 2)
	
	def get_menu_carbohydrates(self):
		total_carbohydrates = 0
		for meal in self.menu_list:
			total_carbohydrates += meal.get_meal_nutri()["Carbo(g)"]
		return round(total_carbohydrates, 2)

	def get_menu_fats(self):
		total_fats = 0
		for meal in self.menu_list:
			total_fats += meal.get_meal_nutri()["Fats(g)"]
		return round(total_fats, 2)
		
	def get_menu_info(self):
		for meal in self.menu_list:
			meal.show_products_in_meal()
			print("Nutritional values of {}: Proteins: {} g, Carbohydrates {} g, Fats {} g.".format(meal.name,
			    round(meal.get_meal_nutri()["Protein(g)"], 1), round(meal.get_meal_nutri()["Carbo(g)"], 1),
			    round(meal.get_meal_nutri()["Fats(g)"], 1)))
			print("Amount of calories in {}: {} kcal".format(meal.name, meal.get_meal_calories()))
		print("Total caloric value of the daily menu: {} kcal".format(self.get_menu_calories()))
		print("Total protein in the daily menu: {} g".format(self.get_menu_proteins()))
		print("Total carbohydrates in the daily menu: {} g".format(self.get_menu_carbohydrates()))
		print("Total fats in the daily menu: {} g".format(self.get_menu_fats()))
		print("\n")
		
	
	

