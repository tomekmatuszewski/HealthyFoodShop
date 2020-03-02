from ShoppingList.Store_Warehouse import StoreWarehouse,ShoppingList
from ShoppingList.ShoppingItem import ShoppingItem

MainWarehouse = StoreWarehouse("Healthy Food Shop Warehouse")
bread = ShoppingItem("bread","2$", {"Protein": 5, "Carbohydrates" : 10 , "Fats" : 20})

MainWarehouse.add_new_product(bread,10)
MainWarehouse.remove_product(bread,1)

new_Shopping_list = ShoppingList(1)
new_Shopping_list.add_product(bread,2,MainWarehouse)

print(new_Shopping_list.List)

