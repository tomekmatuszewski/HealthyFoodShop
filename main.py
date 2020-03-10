from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shop import ShoppingList,ShopWarehouse
from ShoppingList.Database_food import food

# creating Main Warehouse for Healthy Food Shop !!!!
MainWarehouse = ShopWarehouse("Healthy Food Shop Warehouse")

# creating Items for Healthy Food Shop !!!!
for i in range(641):
	item = ShoppingItem(food.loc[i, "Product"], food.loc[i, "Price"],{"Protein(g)": food.loc[i, "Protein(g)"],"Fats(g)": food.loc[i, "Fats(g)"], "Carbo(g)": food.loc[i, "Carbo(g)"]},
	                    food.loc[i, "Weight[kg]"], food.loc[i, "Kcal"])

	MainWarehouse.Warehouse[item.name] = 100

print(MainWarehouse.Warehouse)

# Creating Shopping List !!!!
new_Shopping_Cart = ShoppingList(1)

while True:
	index_number = int(input('Select number of product from list: '))
	number_of_products = int(input("Select quantity of prodcuts: "))
	item = ShoppingItem(food.loc[index_number,"Product"],food.loc[index_number,"Price"],
	                    {"Protein(g)": food.loc[index_number,"Protein(g)"],"Fats(g)": food.loc[index_number,"Fats(g)"],"Carbo(g)": food.loc[index_number,"Carbo(g)"]},
	                    food.loc[index_number,"Weight[kg]"],food.loc[index_number,"Kcal"])
	new_Shopping_Cart.add_product(item,number_of_products)
	print("Item added to Shopping Cart")
	next_step = input("Do you want to continue [y/n]: ")
	if next_step == 'y':
		continue
	else:
		print(new_Shopping_Cart.Show_Shopping_list())
		print(new_Shopping_Cart.check_total_cost())
		break
	
	
	
	
	
	# print(item.nutri_per_100)
	# print(item.name)
	# print(item.calories, ' kcal per 100 g')
	# print(item.price)
	# new_Shopping_Cart.add_product(item, 5)
	# print(new_Shopping_Cart[0])
	# print(new_Shopping_Cart.check_total_cost())
	# print(new_Shopping_Cart.Show_Shopping_list())
	# break
	
print(MainWarehouse.Warehouse)






