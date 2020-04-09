from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shop import ShoppingList,ShopWarehouse
from ShoppingList.Database_food import food
from ShoppingList.utils import *
import json

categories = sorted(list(set(food.index.get_level_values(0))))

# creating Main Warehouse for Healthy Food Shop !!!!
MainWarehouse = ShopWarehouse("Healthy Food Shop Warehouse")

# creating Items for Healthy Food Shop !!!!

for category in categories:
	for number in range(len(food.loc[category])):
		item = ShoppingItem(food.loc[(category,number+1), "Product"], food.loc[(category,number+1), "Price[PLN]"],{"Protein(g)": food.loc[(category,number+1), "Protein(g)"],
		        "Fats(g)": food.loc[(category,number+1), "Fats(g)"], "Carbo(g)": food.loc[(category, number+1), "Carbo(g)"]},food.loc[(category,number+1), "Weight[g/ml]"],
		                    food.loc[(category,number+1), "Kcal"], food.loc[(category,number+1),"unit"])
		if item.unit == 'kg':
			MainWarehouse.Warehouse[item.name] = 10
		else:
			MainWarehouse.Warehouse[item.name] = 50
		
# Creating Shopping List !!!!
new_Shopping_Cart = ShoppingList()

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
	item = ShoppingItem(food.loc[(categories[category-1], index_number), "Product"], food.loc[(categories[category-1],index_number), "Price[PLN]"],
	                    {"Protein(g)": food.loc[(categories[category-1], index_number), "Protein(g)"],
	                     "Fats(g)": food.loc[(categories[category-1], index_number), "Fats(g)"], "Carbo(g)": food.loc[(categories[category-1],index_number), "Carbo(g)"]},
	                    food.loc[(categories[category-1], index_number), "Weight[g/ml]"], food.loc[(categories[category-1], index_number), "Kcal"], food.loc[(categories[category-1], index_number), "unit"])
	print("{} : {} {} in Stock, price {} PLN/{}{}".format(item.name, MainWarehouse.Warehouse[item.name], item.unit, item.price, item.unit, ", " + str(item.weight) + "g/szt" if item.unit == 'szt' else ""))
	number_of_products = input("Select quantity of products [szt/kg]: ")
	number_of_products = check_selected_unit(number_of_products)
	new_Shopping_Cart.add_product(item, number_of_products)
	print("Item added to Shopping Cart :)")
	view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
	view_of_chart = check_view_of_chart(view_of_chart)
	if view_of_chart == 'Y':
		new_Shopping_Cart.Show_Shopping_list()
	while True:
		action = input("Select next action [Continue :(C), Add (increase number for item): (A), Remove :(R), Finish (F)]: ")
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
			item = ShoppingItem(food.loc[(categories[category - 1], index_number), "Product"],
			                    food.loc[(categories[category - 1], index_number), "Price[PLN]"],
			                    {"Protein(g)": food.loc[(categories[category - 1], index_number), "Protein(g)"],
			                     "Fats(g)": food.loc[(categories[category - 1], index_number), "Fats(g)"],
			                     "Carbo(g)": food.loc[(categories[category - 1], index_number), "Carbo(g)"]},
			                    food.loc[(categories[category - 1], index_number), "Weight[g/ml]"],
			                    food.loc[(categories[category - 1], index_number), "Kcal"],
			                    food.loc[(categories[category - 1], index_number), "unit"])
			print("{} : {} {} in Stock, price {} PLN/{}{}".format(item.name, MainWarehouse.Warehouse[item.name],
			                                                      item.unit, item.price, item.unit, ", " + str(
					item.weight) + "g/szt" if item.unit == 'szt' else ""))
			number_of_products = input("Select quantity of products [szt/kg]: ")
			number_of_products = check_selected_unit(number_of_products)
			new_Shopping_Cart.add_product(item, number_of_products)
			print("Item added to Shopping Cart :)")
			view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
			view_of_chart = check_view_of_chart(view_of_chart)
			if view_of_chart == 'Y':
				new_Shopping_Cart.Show_Shopping_list()
			continue
		elif action == 'R':
			while True:
				new_Shopping_Cart.Show_Shopping_list()
				product = input("Select position from Shopping List [select 0 to Undo]: ")
				product = check_product(product, new_Shopping_Cart)
				if product == 0:
					break
				quantity = input("How many products do you want to remove: ")
				quantity = check_selected_unit(quantity)
				if quantity > new_Shopping_Cart.List[new_Shopping_Cart[product-1]]:
					print("Number of products in the basket is less! Choose the correct number")
					continue
				new_Shopping_Cart.remove_product(new_Shopping_Cart[product-1], quantity)
				new_Shopping_Cart.Show_Shopping_list()
				if len(new_Shopping_Cart) == 0:
					print("Shopping Cart is Empty!!")
					break
				else:
					break
			continue
		elif action == "A":
			while True:
				new_Shopping_Cart.Show_Shopping_list()
				product = input("Select position from Shopping List [select 0 to Undo]: ")
				product = check_product(product, new_Shopping_Cart)
				if product == 0:
					break
				quantity = float(input("How many products do you want to add: "))
				quantity = check_selected_unit(quantity)
				if quantity > new_Shopping_Cart.Warehouse[new_Shopping_Cart[product - 1].name]:
					print("Not enough products in stock!")
					continue
				new_Shopping_Cart.increase_number_product(new_Shopping_Cart[product - 1], quantity)
				new_Shopping_Cart.Show_Shopping_list()
				break
			continue
		elif action == 'F':
			print("*" * 150)
			new_Shopping_Cart.Show_Shopping_list()
			print("*" * 150)
			new_Shopping_Cart.get_nutritional_raport()
			break
	break
		
print("*"*150)

new_Shopping_Cart.Print_Bill()



#print(MainWarehouse.Warehouse)






