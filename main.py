from ShoppingList.Store_Warehouse import MainWarehouse
from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shopping_list import ShoppingList
from ShoppingList.Database_food import food


# creating Items for Healthy Food Shop !!!!
for i in range(641):
	item = ShoppingItem(food.loc[i, "Product"], food.loc[i, "Price"],{"Protein(g)": food.loc[i, "Protein(g)"],"Fats(g)": food.loc[i, "Fats(g)"], "Carbo(g)": food.loc[i, "Carbo(g)"]},
	                    food.loc[i, "Weight[kg]"], food.loc[i, "Kcal"])

	MainWarehouse.WarehouseState[item.name] = 100

print(MainWarehouse.WarehouseState)

# Creating Shopping List !!!!
new_Shopping_list = ShoppingList(1)


while True:
	index_number = int(input('Select number of product from list: '))
	item = ShoppingItem(food.loc[index_number,"Product"],food.loc[index_number,"Price"],
	                    {"Protein(g)": food.loc[index_number,"Protein(g)"],"Fats(g)": food.loc[index_number,"Fats(g)"],"Carbo(g)": food.loc[index_number,"Carbo(g)"]},
	                    food.loc[index_number,"Weight[kg]"],food.loc[index_number,"Kcal"])
	print(item.nutri_per_100)
	print(item.name)
	print(item.calories)
	print(item.price)
	new_Shopping_list.add_product(item, 5)
	print(new_Shopping_list[0])
	print(new_Shopping_list.check_total_cost())
	print(new_Shopping_list.Show_Shopping_list())
	break
	
	




#
#
#
# print(new_Shopping_list[0])
# print(len(new_Shopping_list))
#
#



