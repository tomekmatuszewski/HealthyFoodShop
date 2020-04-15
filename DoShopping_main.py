from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shop import ShoppingList
from ShoppingList.Database_food import food, categories
from ShoppingList.utils import *

# creating Healthy Food Shop !!!!
new_shopping_cart = ShoppingList("Healthy Food Shop")

# creating Items for Healthy Food Shop - filling up the Warehouse!!!!
new_shopping_cart.fill_up_warehouse(10, 50)


while True:
	for item in range(len(categories)):
		print("{}: {}".format(item+1, categories[item]))
	category = input("Select categories [1-22]: ")
	category = check_category(category, categories)
	print(food.loc[categories[category-1]].loc[:, ["Product", "Price[PLN]"]])
	index_number = input('Select number of product from list above [select "0" to undo]: ')
	index_number = check_index_number(index_number, food.loc[categories[category-1]].loc[:, ["Product", "Price[PLN]"]])
	if index_number == 0:
		continue
	item = ShoppingItem.create_shopping_item(category, index_number)
	new_shopping_cart.show_availability(item)
	if item.unit == "szt":
		quantity = input("Select quantity of products [szt]: ")
		quantity = check_selected_unit(quantity, item)
	else:
		quantity = input("Select quantity of products [kg]: ")
		quantity = check_selected_unit(quantity, item)
	new_shopping_cart.add_product(item, quantity)
	print("Item added to Shopping Cart :)")
	view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
	view_of_chart = check_view_of_chart(view_of_chart)
	if view_of_chart == 'Y':
		new_shopping_cart.show_shopping_list()
	while True:
		action = input("Select next action [Continue :(C), Add (increase quantity of product): \
		(A), Remove :(R), Finish (F)]: ")
		action = check_action(action)
		if action == 'C':
			for item in range(len(categories)):
				print("{}: {}".format(item + 1, categories[item]))
			category = input("Select categories [1-22]: ")
			category = check_category(category, categories)
			print(food.loc[categories[category - 1]].loc[:, ["Product", "Price[PLN]"]])
			index_number = input('Select number of product from list above [select "0" to undo]: ')
			index_number = check_index_number(index_number,
			                                  food.loc[categories[category - 1]].loc[:, ["Product", "Price[PLN]"]])
			if index_number == 0:
				continue
			item = ShoppingItem.create_shopping_item(category, index_number)
			new_shopping_cart.show_availability(item)
			
			if item.unit == "szt":
				quantity = input("Select quantity of products [szt]: ")
				quantity = check_selected_unit(quantity, item)
			else:
				quantity = input("Select quantity of products [kg]: ")
				quantity = check_selected_unit(quantity, item)
			new_shopping_cart.add_product(item, quantity)
			print("Item added to Shopping Cart :)")
			view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
			view_of_chart = check_view_of_chart(view_of_chart)
			if view_of_chart == 'Y':
				new_shopping_cart.show_shopping_list()
			continue
		elif action == 'R':
			while True:
				new_shopping_cart.show_shopping_list()
				product = input("Select position from Shopping List [select 0 to Undo]: ")
				product = check_product(product, new_shopping_cart)
				if product == 0:
					break
				if new_shopping_cart[product-1].unit == "szt":
					quantity = input("How many products do you want to remove [szt]: ")
					quantity = check_selected_unit(quantity, new_shopping_cart[product-1])
				else:
					quantity = input("How many products do you want to remove [kg]: ")
					quantity = check_selected_unit(quantity, new_shopping_cart[product - 1])
				if quantity > new_shopping_cart.cart[new_shopping_cart[product-1]]:
					print("Number of products in the basket is less! Choose the correct number")
					continue
				new_shopping_cart.remove_product(new_shopping_cart[product-1], quantity)
				new_shopping_cart.show_shopping_list()
				if len(new_shopping_cart) == 0:
					print("Shopping Cart is Empty!!")
					break
				else:
					break
			continue
		elif action == "A":
			while True:
				new_shopping_cart.show_shopping_list()
				product = input("Select position from Shopping List [select 0 to Undo]: ")
				product = check_product(product, new_shopping_cart)
				if product == 0:
					break
				if new_shopping_cart[product-1].unit == 'szt':
					quantity = input("How many products do you want to add [szt]: ")
					quantity = check_selected_unit(quantity, new_shopping_cart[product-1])
				else:
					quantity = input("How many products do you want to add [kg]: ")
					quantity = check_selected_unit(quantity, new_shopping_cart[product - 1])
				if quantity > new_shopping_cart.warehouse[new_shopping_cart[product - 1].name]:
					print("Not enough products in stock!")
					continue
				new_shopping_cart.increase_number_product(new_shopping_cart[product - 1], quantity)
				new_shopping_cart.show_shopping_list()
				break
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



#print(new_shopping_cart.warehouse)






