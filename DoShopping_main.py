from ShoppingList.Shop import ShoppingList
from ShoppingList.utils import *

# creating Healthy Food Shop !!!!
new_shopping_cart = ShoppingList("Healthy Food Shop")

# creating Items for Healthy Food Shop - filling up the Warehouse!!!!
new_shopping_cart.fill_up_warehouse(10, 50)

while True:
	new_shopping_cart.add_product()
	view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
	view_of_chart = check_view_of_chart(view_of_chart)
	if view_of_chart == 'Y':
		new_shopping_cart.show_shopping_list()
	while True:
		action = input("Select next action [Continue Shopping :(C), Add (increase quantity of product): (A), Remove :(R), Finish (F)]: ")
		action = check_action(action)
		if action == 'C':
			new_shopping_cart.add_product()
			view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
			view_of_chart = check_view_of_chart(view_of_chart)
			if view_of_chart == 'Y':
				new_shopping_cart.show_shopping_list()
			continue
		elif action == 'R':
			new_shopping_cart.remove_product()
			continue
		elif action == "A":
			new_shopping_cart.increase_number_product()
			continue
		elif action == 'F':
			print("*" * 150)
			new_shopping_cart.show_shopping_list()
			print("*" * 150)
			new_shopping_cart.get_nutritional_report()
			break
	break
		
print("*"*150)

new_shopping_cart.print_bill()







