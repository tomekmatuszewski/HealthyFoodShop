from datetime import datetime
from Daily_Menu.Meal import Meal
from Daily_Menu.utils import *
from ShoppingList.Database_food import food, categories
from Daily_Menu.Product import Product
import copy


class Menu:
	possible_set_meals = {1: ["Breakfast", "Dinner", "Supper"], 2: ["Breakfast", "Lunch", "Dinner", "Supper"],
	                      3: ["Breakfast", "Lunch", "Dinner", "Afternoon snack", "Supper"],
	                      4: ["Breakfast", "Lunch", "Dinner", "Afternoon snack", 'Post-workout meal', "Supper"]}
	
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
		print("-" * 40)
		print("Your daily meals: ")
		for meal in self.menu_list:
			print("{}: {:<19}{:<22}".format(counter, meal.name,
			                                "---> {} product{} added".format(len(meal.products_list.keys()),
			                                                                 "s" if len(
				                                                                 meal.products_list.keys()) > 1 else "") if len(
				                                meal.products_list.keys()) else ""))
			counter += 1
		print("-" * 40)
	
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
			print('Complete nutrition information for {}:\n\
		TOTAL:	----->      {:>15} {:7.2f} kcal\n\
				----->      {:>15} {:7.2f} g\n\
				----->      {:>15} {:7.2f} g\n\
				----->      {:>15} {:7.2f} g'.format(meal.name.upper(), "Calories:", meal.get_meal_calories(),
			                                         "Proteins:",
			                                         meal.get_meal_nutri()["Protein(g)"], "Fats:",
			                                         meal.get_meal_nutri()["Fats(g)"], "Carbohydrates:",
			                                         meal.get_meal_nutri()["Carbo(g)"]))
			print('-' * 56)
		print("Summary of values for the daily menu: ")
		print("Total {:<15}    {:7.2f} kcal".format('calories:', self.get_menu_calories()))
		print("Total {:<15}    {:7.2f} g".format('proteins:', self.get_menu_proteins()))
		print("Total {:<15}    {:7.2f} g".format('fats:', self.get_menu_fats()))
		print("Total {:<15}    {:7.2f} g".format('carbohydrates:', self.get_menu_carbohydrates()))
		print('-' * 56)
	
	def show_possible_set_meals(self):
		print("Possible set of meals per day: ")
		for k, v in self.possible_set_meals.items():
			item = ""
			for meal in v:
				if v.index(meal) == len(v) - 1:
					item += meal
				else:
					item += meal + ", "
			print("{}. {}".format(k, item))
	
	def print_menu(self, person):
		file_path = r"Daily_Menu\Menus\Menu{}_{}.txt".format(datetime.now().strftime("%Y_%m_%d_%H-%M-%S"),
		                                                     person.username)
		with open(file_path, 'a+') as file:
			file.write("*HEALTHY FOOD SHOP COMPOSE YOUR DAILY MENU*\n")
			file.write("-" * 65 + '\n')
			file.write("Username: {}, Height: {} cm, Weight: {} kg, Age: {} y.\n".format(person.username,
			                                                                             person.height, person.weight,
			                                                                             person.age))
			file.write("-" * 65 + '\n')
			file.write("|{:<50} {:7.2f} {:<4}|\n".format('Your max. daily caloric demand is:', person.cmr, 'kcal'))
			file.write(
				"|{:<53} {:7.2f} {}|\n".format('Your max. daily requirement for protein:', person.daily_proteins, 'g'))
			file.write("|{:<53} {:7.2f} {}|\n".format('Your max. daily requirement for fats:', person.daily_fats, 'g'))
			file.write(
				"|{:<53} {:7.2f} {}|\n".format('Your max. daily requirement for carbohydrates:', person.daily_carbo,
				                               'g'))
			file.write("-" * 65 + '\n')
			for meal in self.menu_list:
				counter = 1
				file.write("{} :\n".format(meal.name.upper()))
				for k, v in meal.products_list.items():
					file.write('{}. {:41}\n\
	----->      {:>14} {:7.1f} g\n\
	----->      {:>15} {:7.2f} kcal\n\
	----->      {:>15} {:7.2f} g\n\
	----->      {:>15} {:7.2f} g\n\
	----->      {:>15} {:7.2f} g\n'.format(counter, k.name + ':', "Product weight:", float(v),
					                       "Calories:", float(k.calories) * float(v) / 100,
					                       "Proteins:",
					                       float(k.nutri_per_100["Protein(g)"]) * float(v) / 100,
					                       "Fats:", float(k.nutri_per_100["Fats(g)"]) * float(v) / 100,
					                       "Carbohydrates:",
					                       float(k.nutri_per_100["Carbo(g)"]) * float(v) / 100))
					counter += 1
					file.write('-' * 65 + '\n')
				file.write('Complete nutrition information for {}:\n\
	TOTAL:	----->      {:>15} {:7.2f} kcal\n\
		----->      {:>15} {:7.2f} g\n\
		----->      {:>15} {:7.2f} g\n\
		----->      {:>15} {:7.2f} g\n'.format(meal.name.upper(), "Calories:", meal.get_meal_calories(),
				                               "Proteins:",
				                               meal.get_meal_nutri()["Protein(g)"], "Fats:",
				                               meal.get_meal_nutri()["Fats(g)"], "Carbohydrates:",
				                               meal.get_meal_nutri()["Carbo(g)"]))
				file.write('-' * 65 + '\n')
			file.write("Summary of values for the daily menu: \n")
			file.write("Total {:<15}    {:7.2f} kcal\n".format('calories:', self.get_menu_calories()))
			file.write("Total {:<15}    {:7.2f} g\n".format('proteins:', self.get_menu_proteins()))
			file.write("Total {:<15}    {:7.2f} g\n".format('fats:', self.get_menu_fats()))
			file.write("Total {:<15}    {:7.2f} g\n".format('carbohydrates:', self.get_menu_carbohydrates()))
			file.write('-' * 65 + '\n')
			file.write("ENJOY ! :)")
	
	def set_quantity_meals(self):
		self.show_possible_set_meals()
		your_menu = input("Select set of meals from list above: ")
		your_menu = check_set_menu(your_menu, self.possible_set_meals.keys())
		setattr(self, 'quantity_of_meals', len(self.possible_set_meals[int(your_menu)]))
		for i in range(self.quantity_of_meals):
			meal = Meal(self.possible_set_meals[int(your_menu)][i])
			self.add_meal(meal)
	
	def __len__(self):
		return len(self.menu_list)
	
	def __getitem__(self, key):
		return self.menu_list[key]
	
	def add_product_to_menu(self, chosen_meal, person):
		while True:
			for item in range(len(categories)):
				print("{}: {}".format(item + 1, categories[item]))
			category = input("Select categories [1-{}], select [0] to undo: ".format(len(categories)))
			category = check_category(category, categories)
			if category == 0:
				break
			print(food.loc[categories[category - 1]].loc[:, ["Product", 'Kcal', 'Carbo(g)', 'Protein(g)', 'Fats(g)']])
			index_number = input('Select number of product from list above [select "0" to undo]: ')
			index_number = check_index_number(index_number, food.loc[categories[category - 1]].loc[:,
			                                                ["Product", 'Kcal', 'Carbo(g)', 'Protein(g)', 'Fats(g)']])
			if index_number == 0:
				continue
			product = Product.create_product(index_number, category)
			print("Weight of average piece/portion of {}: {}g.".format(product.name, product.weight))
			unit_type = input("Select unit type g [G] / psc. [P]: ")
			unit_type = check_unit(unit_type)
			if unit_type == "G":
				quantity_in_grams = input("How many grams of product do you want to add: ")
				quantity = check_selected_unit(quantity_in_grams)
			elif unit_type == "P":
				quantity_in_pcs = input("How many pcs. of product do you want to add: ")
				quantity = check_selected_unit(quantity_in_pcs) * float(product.weight)
			# blockage in case of exceeding the daily limit - calories, nutrition
			temp_menu = copy.deepcopy(self)
			temp_menu[int(chosen_meal) - 1].add_product(product, quantity)
			if temp_menu.get_menu_calories() > person.cmr:
				print("Your daily calorie limit is {}.".format(person.cmr))
				print("Calorie content of your menu after adding the last product {} kcal.".format(
					temp_menu.get_menu_calories()))
				print("Reduce the number of calories!")
				continue
			elif temp_menu.get_menu_proteins() > person.daily_proteins:
				print("Your daily protein limit is {}.".format(person.daily_proteins))
				print("Proteins content of your menu after adding the last product {} g.".format(
					temp_menu.get_menu_proteins()))
				print("Reduce the number of Proteins!")
				continue
			elif temp_menu.get_menu_carbohydrates() > person.daily_carbo:
				print("Your daily carbohydrates limit is {}.".format(person.daily_carbo))
				print("Carbohydrates content of your menu after adding the last product {} g.".format(
					temp_menu.get_menu_carbohydrates()))
				print("Reduce the number of Carbohydrates!")
				continue
			elif temp_menu.get_menu_fats() > person.daily_fats:
				print("Your daily fats limit is {}.".format(person.daily_fats))
				print("Fats content of your menu after adding the last product {} g.".format(temp_menu.get_menu_fats()))
				print("Reduce the number of Fats!")
				continue
			else:
				self[int(chosen_meal) - 1].add_product(product, quantity)
				break
				
	@classmethod
	def create_menu(cls, person):
		return cls(person.cmr, person.daily_carbo, person.daily_proteins, person.daily_fats)
	
	@staticmethod
	def change_quantity_of_product(selected_meal):
		while True:
			selected_meal.show_products_in_meal()
			number_product = input("Select position from Product List [select 0 to Undo]: ")
			number_product = check_number_of_product(number_product, selected_meal)
			product = selected_meal[number_product - 1]
			if number_product == 0:
				break
			change_quantity = input("Select: increase the number of grams of the product - [A], reduce the "
			                        "number of grams of the product [R], Finish [F]: ")
			change_quantity = check_change_quantity(change_quantity)
			if change_quantity == "R":
				print("Weight of average piece/portion of {}: {}g".format(product.name, product.weight))
				unit_type = input("Select unit type g [G] / psc. [P]: ")
				unit_type = check_unit(unit_type)
				if unit_type == "G":
					quantity_in_grams = input("How many grams of product do you want to remove: ")
					quantity = check_selected_unit(quantity_in_grams)
				elif unit_type == "P":
					quantity_in_pcs = input("How many pcs. of product do you want to remove: ")
					quantity = check_selected_unit(quantity_in_pcs) * float(product.weight)
				if quantity > selected_meal.products_list[selected_meal[number_product - 1]]:
					print("Quantity of this product in your meal is less.Choose the correct quantity")
					continue
				selected_meal.remove_product(selected_meal[number_product - 1], quantity)
				if len(selected_meal) == 0:
					print("Meal is Empty!!")
					break
				change_next = input("Do you want to reduce the quantity of another product? [Y/N]:  ")
				change_next = check_change_next(change_next)
				if change_next == "Y":
					continue
				elif change_next == "N":
					break
			elif change_quantity == "A":
				print("Weight of average piece/portion of {}: {}g.".format(product.name, product.weight))
				unit_type = input("Select unit type g [G] / psc. [P]: ")
				unit_type = check_unit(unit_type)
				if unit_type == "G":
					quantity_in_grams = input("How many grams of product do you want to add: ")
					quantity = check_selected_unit(quantity_in_grams)
				elif unit_type == "P":
					quantity_in_pcs = input("How many pcs. of product do you want to add: ")
					quantity = check_selected_unit(quantity_in_pcs) * float(product.weight)
				selected_meal.add_product(selected_meal[number_product - 1], quantity)
				change_next = input("Do you want to increase the quantity of another product? [Y/N]: ")
				change_next = check_change_next_two(change_next)
				if change_next == "Y":
					continue
				if change_next == "N":
					break
			elif change_quantity == "F":
				break
	
	@staticmethod
	def remove_product_from_menu(selected_meal):
		while True:
			selected_meal.show_products_in_meal()
			number_product = input("Select position from Product List [select 0 to Undo]: ")
			number_product = check_number_of_product(number_product, selected_meal)
			if number_product == 0:
				break
			selected_meal.remove_item(selected_meal[number_product - 1])
			selected_meal.show_products_in_meal()
			if len(selected_meal) == 0:
				print("Meal is Empty!!")
				break
			remove_next = input("Do you want to remove next product: [Y/N]: ")
			remove_next = check_continue_removing(remove_next)
			if remove_next == "Y":
				continue
			elif remove_next == "N":
				break
