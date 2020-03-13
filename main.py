from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shop import ShoppingList,ShopWarehouse
from ShoppingList.Database_food import food

# creating Main Warehouse for Healthy Food Shop !!!!
MainWarehouse = ShopWarehouse("Healthy Food Shop Warehouse")

# creating Items for Healthy Food Shop !!!!
for i in range(351):
	item = ShoppingItem(food.loc[i, "Product"], food.loc[i, "Price[PLN]"],{"Protein(g)": food.loc[i, "Protein(g)"],"Fats(g)": food.loc[i, "Fats(g)"], "Carbo(g)": food.loc[i, "Carbo(g)"]},
	                    food.loc[i, "Weight[g/ml]"], food.loc[i, "Kcal"], food.loc[i,"unit"])

	MainWarehouse.Warehouse[item.name] = 100

print(MainWarehouse.Warehouse)

# Creating Shopping List !!!!
new_Shopping_Cart = ShoppingList(1)

while True:
	index_number = int(input('Select number of product from list: '))
	number_of_products = float(input("Select quantity of products: "))
	item = ShoppingItem(food.loc[index_number,"Product"],food.loc[index_number,"Price[PLN]"],
	                    {"Protein(g)": food.loc[index_number,"Protein(g)"],"Fats(g)": food.loc[index_number,"Fats(g)"],"Carbo(g)": food.loc[index_number,"Carbo(g)"]},
	                    food.loc[index_number,"Weight[g/ml]"],food.loc[index_number,"Kcal"],food.loc[i,"unit"])
	new_Shopping_Cart.add_product(item,number_of_products)
	print("Item added to Shopping Cart")
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
				remove_next = input("Do you want to remove next item [Y/N]: ")
				if remove_next == "Y":
					continue
				if remove_next == "N":
					break
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
	elif action == 'F':
		print("*" * 150)
		new_Shopping_Cart.Show_Shopping_list()
		print("*" * 150)
		print(new_Shopping_Cart.check_total_cost())
		print("Nutritional values of products in the basket per 100g / Calories per 100 g ")
		for product in new_Shopping_Cart.List:
			print("{} - {} - {} kcal".format(product.name,product.get_nutritional_values(),product.get_calories()))
		print(new_Shopping_Cart.check_total_calories())
		break
	else:
		raise Exception("Wrong command!")
	

print("*"*150)
print(MainWarehouse.Warehouse)






