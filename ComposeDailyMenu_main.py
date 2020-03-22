from ShoppingList.Database_food import food
from Menu.Person import Person
from Menu.factors_calc_meal import factors
from Menu.Meal import Product, Meal, Menu

# users inputs
full_name = input("Enter your name and surname: ")
height = input("Enter your height in [cm]: ")
weight = input("Enter your weight in [kg]: ")
age = input("Enter your age : ")
sex = input("Enter your sex [M/F]: ")
print("\nDaily activities: ")
for i in range(1,len(factors)+1):
	print("{} : {}".format(i,factors.loc[i,'Activity']))
print("\n")
activity_index = input("Select number of your activity from list above: ")
activity = factors.iloc[int(activity_index)-1, 1]

person1 = Person(full_name, height, weight, age, sex, activity)
person1.show_info()

menu = Menu(person1.cmr, person1.daily_carbo, person1.daily_proteins, person1.daily_fats)
print("Possible set of meals per day: ")
for k, v in menu.possible_set_meals.items():
	print("{}. {}".format(k, v))
	
your_menu = input("Select set of meals from list above: ")
menu.quantity_of_meals = len(menu.possible_set_meals[int(your_menu)])

for i in range(menu.quantity_of_meals):
	meal = Meal(menu.possible_set_meals[int(your_menu)][i])
	menu.add_meal(meal)

categories = sorted(list(set(food.index.get_level_values(0))))

for meal in menu.menu_list:
	print("Compose your first meal: {}". format(meal.name))
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
		product = Product(food.loc[(categories[category-1],index_number), "Product"], food.loc[(categories[category-1],index_number), "Price[PLN]"],
		                    {"Protein(g)": food.loc[(categories[category-1],index_number), "Protein(g)"],
		                     "Fats(g)": food.loc[(categories[category-1],index_number), "Fats(g)"], "Carbo(g)": food.loc[(categories[category-1],index_number), "Carbo(g)"]},
		                    food.loc[(categories[category-1],index_number), "Weight[g/ml]"], food.loc[(categories[category-1],index_number), "Kcal"],
		                  food.loc[(categories[category-1],index_number), "unit"])
		quantity_in_grams = input("How many grams of product do you want to add :")
		product.grams = float(quantity_in_grams)
		meal.add_product(product, product.grams)
		break
		

print(menu.get_menu_info())




















