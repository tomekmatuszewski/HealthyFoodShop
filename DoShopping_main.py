from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shop import ShoppingList,ShopWarehouse
from ShoppingList.Database_food import food
import json

categories = sorted(list(set(food.index.get_level_values(0))))

# creating Main Warehouse for Healthy Food Shop !!!!
MainWarehouse = ShopWarehouse("Healthy Food Shop Warehouse")

# creating Items for Healthy Food Shop !!!!

for category in categories:
	for number in range(len(food.loc[category])):
		item = ShoppingItem(food.loc[(category,number+1), "Product"], food.loc[(category,number+1), "Price[PLN]"],{"Protein(g)": food.loc[(category,number+1), "Protein(g)"],
		        "Fats(g)": food.loc[(category,number+1), "Fats(g)"], "Carbo(g)": food.loc[(category,number+1), "Carbo(g)"]},food.loc[(category,number+1), "Weight[g/ml]"],
		                    food.loc[(category,number+1), "Kcal"], food.loc[(category,number+1),"unit"])
		if item.unit == 'kg':
			MainWarehouse.Warehouse[item.name] = 10
		else:
			MainWarehouse.Warehouse[item.name] = 50
		
# Creating Shopping List !!!!
new_Shopping_Cart = ShoppingList()

while True:
	for item in range(len(categories)):
		print("{}: {}".format(item+1,categories[item]))
	category = int(input("Select categories [1-22]: "))
	if category > len(categories):
		print("Wrong number!")
		continue
	print(food.loc[categories[category-1]].loc[:, ["Product","Price[PLN]"]])
	index_number = int(input('Select number of product from list above [select "0" to undo]: '))
	if index_number == 0:
		continue
	elif index_number > len(food.loc[categories[category-1]].loc[:, ["Product","Price[PLN]"]]):
		print("Wrong number!")
		continue
	item = ShoppingItem(food.loc[(categories[category-1],index_number), "Product"], food.loc[(categories[category-1],index_number), "Price[PLN]"],
	                    {"Protein(g)": food.loc[(categories[category-1],index_number), "Protein(g)"],
	                     "Fats(g)": food.loc[(categories[category-1],index_number), "Fats(g)"], "Carbo(g)": food.loc[(categories[category-1],index_number), "Carbo(g)"]},
	                    food.loc[(categories[category-1],index_number), "Weight[g/ml]"], food.loc[(categories[category-1],index_number), "Kcal"], food.loc[(categories[category-1],index_number), "unit"])
	print("{} : {} {} in Stock, price {} PLN/{}{}".format(item.name,MainWarehouse.Warehouse[item.name],item.unit,item.price,item.unit, ", " + str(item.weight) + "g/szt" if item.unit == 'szt' else ""))
	number_of_products = float(input("Select quantity of products [szt/kg]: "))
	new_Shopping_Cart.add_product(item,number_of_products)
	print("Item added to Shopping Cart :)")
	view_of_chart = input("Do you want to view the contents of the basket [Y/N]:")
	if view_of_chart == 'Y':
		new_Shopping_Cart.Show_Shopping_list()
	action = input("Select next action [Continue :(C), Add (increase number for item): (A), Remove :(R), Finish (F)]: ")
	if action == 'C':
		continue
	elif action == 'R':
		while True:
			new_Shopping_Cart.Show_Shopping_list()
			product = int(input("Select position from Shopping List [select 0 to Undo]: "))
			if product == 0:
				break
			elif product > len(new_Shopping_Cart):
				print("Wrong number!")
				continue
			quantity = float(input("How many products do you want to remove: "))
			if quantity > new_Shopping_Cart.List[new_Shopping_Cart[product-1]]:
				print("Number of products in the basket is less! Choose the correct number")
				continue
			new_Shopping_Cart.remove_product(new_Shopping_Cart[product-1],quantity)
			new_Shopping_Cart.Show_Shopping_list()
			if len(new_Shopping_Cart) == 0:
				print("Shooping Cart is Empty!!")
				break
			else:
				remove_next = input("Do you want to remove next item :( [Y/N]: ")
				if remove_next == "Y":
					continue
				if remove_next == "N":
					break
				else:
					print("Wrong command!")
					continue
		continue_shopping = input("Do you want to continue shopping [Y/N]: ")
		if continue_shopping == "Y":
			continue
		elif continue_shopping == "N":
			print("*" * 150)
			new_Shopping_Cart.Show_Shopping_list()
			print("*" * 150)
			new_Shopping_Cart.get_nutritional_raport()
			break
		else:
			print("Wrong command!")
			continue
	elif action == "A":
		while True:
			new_Shopping_Cart.Show_Shopping_list()
			product = int(input("Select position from Shopping List [select 0 to Undo]: "))
			if product == 0:
				break
			elif product > len(new_Shopping_Cart):
				print("Wrong number!")
				continue
			quantity = float(input("How many products do you want to add: "))
			if quantity > new_Shopping_Cart.Warehouse[new_Shopping_Cart[product - 1].name]:
				print("Not enough products in stock!")
				continue
			new_Shopping_Cart.increase_number_product(new_Shopping_Cart[product - 1], quantity)
			new_Shopping_Cart.Show_Shopping_list()
			add_next = input("Do you want to add next item :( [Y/N]: ")
			if add_next == "Y":
				continue
			if add_next == "N":
				break
			else:
				print("Wrong command!")
				continue
		continue_shopping = input("Do you want to continue shopping [Y/N]: ")
		if continue_shopping == "Y":
			continue
		elif continue_shopping == "N":
			print("*" * 150)
			new_Shopping_Cart.Show_Shopping_list()
			print("*" * 150)
			new_Shopping_Cart.get_nutritional_raport()
			break
		else:
			print("Wrong command!")
			continue
	elif action == 'F':
		print("*" * 150)
		new_Shopping_Cart.Show_Shopping_list()
		print("*" * 150)
		new_Shopping_Cart.get_nutritional_raport()
		break
	else:
		print("Wrong command!")
		continue
		
print("*"*150)

new_Shopping_Cart.Print_Bill()



#print(MainWarehouse.Warehouse)






