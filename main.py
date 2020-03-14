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
		
		
#print(MainWarehouse.Warehouse)

# Creating Shopping List !!!!
new_Shopping_Cart = ShoppingList(1)

while True:
	for item in range(len(categories)):
		print("{}: {}".format(item+1,categories[item]))
	category = int(input("Select categories [1-22]: "))
	print(food.loc[categories[category-1]].loc[:, ["Product","Price[PLN]"]])
	index_number = int(input('Select number of product from list above: '))
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
	action = input("Select next action [continue :(C), remove item from Shopping Chart:(R), Finish Shopping (F)]: ")
	if action == 'C':
		continue
	elif action == 'R':
		while True:
			new_Shopping_Cart.Show_Shopping_list()
			product = int(input("Select position from Shopping List: "))
			quantity = float(input("How many products do you want to remove: "))
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
			print(new_Shopping_Cart.check_total_cost())
			print("Nutritional values of products in the basket per 100g / Calories per 100 g ")
			for product in new_Shopping_Cart.List:
				print("{} - {} - {} kcal".format(product.name, product.get_nutritional_values(),
				                                 product.get_calories()))
			print(new_Shopping_Cart.check_total_calories())
			break
		else:
			print("Wrong command!")
			continue
	elif action == 'F':
		print("*" * 150)
		new_Shopping_Cart.Show_Shopping_list()
		print("*" * 150)
		print(new_Shopping_Cart.check_total_cost())
		print("Nutritional values of products in the basket per 100g / Calories per 100 g: ")
		for product in new_Shopping_Cart.List:
			print("{:40} - {:55} - {:10} kcal".format(product.name,json.dumps(product.get_nutritional_values()),product.get_calories()))
		print(new_Shopping_Cart.check_total_calories())
		break
	else:
		print("Wrong command!")
		continue


print("*"*150)
print(MainWarehouse.Warehouse)






