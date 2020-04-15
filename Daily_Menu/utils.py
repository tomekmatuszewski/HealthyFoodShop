import re


def caluculate_bmi(weight, height):
	return round(weight / ((height / 100) ** 2), 2)


def calculate_bmr(weight, height, age, sex):
	if sex == 'M':
		return 9.99 * weight + 6.25 * height - 4.92 * age + 5
	elif sex == 'F':
		return 9.99 * weight + 6.25 * height - 4.92 * age - 161
	else:
		print("Enter 'M' - Male or 'F' - Female")


def check_username(username):
	while re.match(r"^(?=.*[a-zA-Z].*[a-zA-Z])[\w\. -]{,20}$", username) is None:
		print("Wrong username")
		username = input("Enter your username [max 20 alphanum. characters('.'/'_'/'-' are allowed, min. 2 letters): ")
		continue
	return username


def check_height(height):
	while re.match(r"^\d\d\d(\.\d)?$", height) is None:
		print("Wrong height!")
		height = input("Enter your height in [cm]: ")
		continue
	return height


def check_weight(weight):
	while re.match(r"^\d\d\d?(\.\d)?$", weight) is None:
		print("Wrong weight!")
		weight = input("Enter your weight in [kg]: ")
		continue
	return weight


def check_age(age):
	while re.match(r"^1?\d\d$", age) is None:
		print("Wrong age!")
		age = input("Enter your age : ")
		continue
	return age


def check_sex(sex):
	while re.match(r"^(M|F)$", sex) is None:
		print("Wrong sex!")
		sex = input("Enter your sex : ")
		continue
	return sex


def check_activity_index(activity_index, factors):
	while re.match(r"^([1-{}])$".format(len(factors)), activity_index) is None:
		print("Wrong number!")
		activity_index = input("Select number of your activity from list above: ")
		continue
	return activity_index


def check_set_menu(your_menu, possible_set_meals):
	while re.match(r"^([1-{}])$".format(len(possible_set_meals)), your_menu) is None:
		print("Wrong number!")
		your_menu = input("Select set of meals from list above: ")
		continue
	return your_menu


def check_chosen_meal(chosen_meal, menu_list):
	while re.match(r"^([1-{}]|F|P)$".format(len(menu_list)), chosen_meal) is None:
		print("Select the correct command !")
		chosen_meal = input("Select meal to compose (choose number above) or select [F] to Finish"
		                    " / [P] print your menu and personal info: ")
		continue
	return chosen_meal


def check_action(action):
	while re.match(r"^(A|F|P)$", action) is None:
		print("Select the correct command !")
		action = input("Select action [Add product: (A), Finish (F), Print personal parameters (P)]: ")
		continue
	return action


def check_action_two(action):
	while re.match(r"^(A|F|P|R|Q)$", action) is None:
		print("Select the correct command !")
		action = input("Select action [Add product: (A), Remove Product: (R), "
		               "Change quantity [g]: (Q), Finish (F), Print your personal parameters and menu (P)]: ")
		continue
	return action


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


def check_unit(unit):
	while re.match(r"^(P|G)$", unit) is None:
		print("Select the correct command !")
		unit = input("Select right unit type g [G] / psc. [P]: ")
		continue
	return unit


def check_selected_unit(quantity):
	while True:
		try:
			if quantity == "0":
				print("Select the correct quantity [g or pcs.  > 0]!")
				quantity = input("How many grams/pcs. of product do you want to add: ")
				continue
			float(quantity)
			return float(quantity)
			break
		except ValueError:
			print("Select the correct quantity [g or pcs.  > 0]!")
			quantity = input("How many grams/pcs. of product do you want to add: ")
			continue


def check_number_of_product(number, list_products):
	while not number.isdecimal() or int(number) > len(list_products):
		print("Wrong position!")
		number = input("Choose the right position from your meal! [select 0 to Undo]: ")
		continue
	return int(number)


def check_change_quantity(change_quantity):
	while re.match(r"^(A|R|F)$", change_quantity) is None:
		print("Select the correct command !")
		change_quantity = input("Select: increase the number of grams of the product - [A], "
		                        "reduce the number of grams of the product [R], Finish [F]: ")
		continue
	return change_quantity


def check_change_next(change_next):
	while re.match(r"^(Y|N)$", change_next) is None:
		print("Select Y - Yes / N - No!")
		change_next = input("Do you want to reduce the quantity of another product? [Y/N]:  ")
		continue
	return change_next


def check_change_next_two(change_next):
	while re.match(r"^(Y|N)$", change_next) is None:
		print("Select Y - Yes / N - No!")
		change_next = input("Do you want to increase the quantity of another product? [Y/N]: ")
		continue
	return change_next


def check_continue_adding(continue_adding):
	while re.match(r"^(Y|N)$", continue_adding) is None:
		print("Select Y - Yes / N - No!")
		continue_adding = input("Do you want to continue completing your meal? [Y/N]: ")
		continue
	return continue_adding


def check_continue_removing(remove_next):
	while re.match(r"^(Y|N)$", remove_next) is None:
		print("Select Y - Yes / N - No!")
		remove_next = input("Do you want to remove next product: [Y/N]: ")
		continue
	return remove_next

