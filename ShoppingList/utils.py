import re


# function to calculate calories based on weight and makro
def get_calories(makro, weight):
	kcal = (makro["Protein"] * 4 + makro["Carbohydrates"] * 4 + makro["Fats"] * 9) * (weight / 100)
	return kcal


def check_category(category, categories):
	while not category.isdecimal() or int(category) > len(categories):
		print("Select the correct command !")
		category = input("Select categories [1-{}], select [0] to undo: ".format(len(categories)))
		continue
	return int(category)


def check_index_number(index, list_index):
	while not index.isdecimal() or int(index) > len(list_index):
		print("Select the correct command !")
		index = input('Select number of product from list above [select "0" to undo]: ')
		continue
	return int(index)


def check_selected_unit(quantity, item):
	if item.unit == "szt":
		while not quantity.isdecimal() or quantity == '0':
			print("The selected product - {} is sold in whole pieces/packs. Please select a valid quantity".format(item.name))
			quantity = input("Select quantity of products [szt]: ")
			continue
		return int(quantity)
	else:
		while True:
			try:
				if quantity == "0":
					print("Select the correct quantity [kg > 0]!")
					quantity = input("How many kg. of product do you want to add: ")
					continue
				float(quantity)
				return float(quantity)
				break
			except ValueError:
				print("Select the correct quantity [kg > 0]!")
				quantity = input("How many kg. of product do you want to add: ")
				continue


def check_view_of_chart(view_of_cart):
	while re.match(r"^(Y|N)$", view_of_cart) is None:
		print("Select Y - Yes / N - No!")
		view_of_cart = input("Do you want to view the contents of the basket [Y/N]:")
		continue
	return view_of_cart


def check_action(action):
	while re.match(r"^(A|F|C|R)$", action) is None:
		print("Select the correct command !")
		action = input(
			"Select next action [Continue :(C), Add (increase number for item): (A), Remove :(R), Finish (F)]: ")
		continue
	return action


def check_product(product, products_list):
	while not product.isdecimal() or int(product) > len(products_list):
		print("Select the correct command !")
		product = input("Select position from Shopping List [select 0 to Undo]: ")
		continue
	return int(product)


def check_remove_next(remove_next):
	while re.match(r"^(Y|N)$", remove_next) is None:
		print("Select Y - Yes / N - No!")
		remove_next = input("Do you want to remove next item :( [Y/N]: ")
		continue
	return remove_next


def check_continue_shopping(continue_shopping):
	while re.match(r"^(Y|N)$", continue_shopping) is None:
		print("Select Y - Yes / N - No!")
		continue_shopping = input("Do you want to continue shopping [Y/N]: ")
		continue
	return continue_shopping


def check_add_next(add_next):
	while re.match(r"^(Y|N)$", add_next) is None:
		print("Select Y - Yes / N - No!")
		add_next = input("Do you want to add next item :( [Y/N]: ")
		continue
	return add_next