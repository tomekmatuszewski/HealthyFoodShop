from ShoppingList.Store_Warehouse import StoreWarehouse
from ShoppingList.ShoppingItem import ShoppingItem
from ShoppingList.Shopping_list import ShoppingList

# creating Main Warehouse for Healthy Food Shop !!!!
MainWarehouse = StoreWarehouse("Healthy Food Shop Warehouse")


# creating Products !!!!
bread = ShoppingItem("Rye Bread",2, {"Protein": 9, "Carbohydrates" : 48 , "Fats" : 3.3},400)
mineralwater = ShoppingItem("Mineral Aqua",1, {"Protein": 0, "Carbohydrates" : 0 , "Fats" : 0},1500)
BasmatiRice = ShoppingItem("Basmati Rice",1.5,{"Protein": 7, "Carbohydrates" : 76.7 , "Fats" : 1.2},400)


# Adding Products to Warehouse !!!!
MainWarehouse.add_new_product(bread,10)
MainWarehouse.add_new_product(mineralwater,20)
MainWarehouse.add_new_product(BasmatiRice,50)



# Creating Shopping List !!!!
new_Shopping_list = ShoppingList(1)

new_Shopping_list.add_product(bread,5,MainWarehouse)
new_Shopping_list.add_product(mineralwater,2,MainWarehouse)
new_Shopping_list.add_product(BasmatiRice,2,MainWarehouse)

print(new_Shopping_list.check_total_cost())
print(new_Shopping_list.Show_Shopping_list())


print(new_Shopping_list[0])
print(len(new_Shopping_list))


print(MainWarehouse.Show_Products_InStock(BasmatiRice))




