from Daily_Menu.Person import Person
from Daily_Menu.Menu import Menu
import pandas as pd
from Daily_Menu.utils import *

pd.set_option('display.width', 200)

person1 = Person.create_person()
person1.show_info()
menu = Menu.create_menu(person1)
# user
menu.set_quantity_meals()

while True:
	menu.get_meals_names()
	chosen_meal = input("Select meal to compose (choose number above) or select [F] to Finish / "
	                    "[P] print your menu and personal info: ")
	chosen_meal = check_chosen_meal(chosen_meal,  menu.menu_list)
	if chosen_meal == "F":
		break
	elif chosen_meal == "P":
		person1.show_info()
		menu.get_menu_info()
		continue
	selected_meal = menu[int(chosen_meal) - 1]
	
	while True:
		if len(selected_meal) == 0:
			print("-"*82)
			print('Completing {}'.format(selected_meal.get_meal_name()))
			action = input("Select action [Add product: (A), Finish (F), Print personal parameters (P)]: ")
			action = check_action(action)
			if action == "F":
				break
			elif action == "P":
				person1.show_info()
			elif action == "A":
				menu.add_product_to_menu(chosen_meal, person1)
				
		if len(selected_meal) > 0:
			print("Completing {}".format(selected_meal.get_meal_name()))
			action = input("Select action [Add product: (A), Remove Product: (R), "
			               "Change quantity [g]: (Q), Finish (F), Print your personal parameters and menu (P)]: ")
			action = check_action_two(action)
			if action == "A":
				selected_meal.show_products_in_meal()
				menu.add_product_to_menu(chosen_meal, person1)
				
			elif action == "Q":
				menu.change_quantity_of_product(selected_meal)
				continue_adding = input("Do you want to continue completing your meal? [Y/N]: ")
				continue_adding = check_continue_adding(continue_adding)
				if continue_adding == "Y":
					continue
				elif continue_adding == "N":
					selected_meal.show_products_in_meal()
					break
					
			elif action == "R":
				menu.remove_product_from_menu(selected_meal)
				continue_adding = input("Do you want to continue completing your meal? [Y/N]: ")
				continue_adding = check_continue_adding(continue_adding)
				if continue_adding == "Y":
					continue
				elif continue_adding == "N":
					selected_meal.show_products_in_meal()
					break
					
			elif action == "P":
				person1.show_info()
				menu.get_menu_info()
	
			elif action == 'F':
				break
			
menu.get_menu_info()
menu.print_menu(person1)
print("ENJOY ! :)")
