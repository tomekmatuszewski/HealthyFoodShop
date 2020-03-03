from ShoppingList.Store_Warehouse import StoreWarehouse
from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shopping_list import ShoppingList

MainWarehouse = StoreWarehouse("Healthy Food Shop Warehouse")
bread = ShoppingItem("Diet bread",2, {"Protein": 5, "Carbohydrates" : 10 , "Fats" : 20})
mineralwater = ShoppingItem("Mineral water",1, {"Protein": 0, "Carbohydrates" : 0 , "Fats" : 0})

MainWarehouse.add_new_product(bread,10)

MainWarehouse.add_new_product(mineralwater,20)




new_Shopping_list = ShoppingList(1)
new_Shopping_list.add_product(bread,2,MainWarehouse)
new_Shopping_list.add_product(mineralwater,2,MainWarehouse)

print(new_Shopping_list.check_total_cost())
print(new_Shopping_list.Show_Shopping_list())




