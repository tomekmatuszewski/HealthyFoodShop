import pandas as pd
pd.set_option('display.max_columns', 10)


food = pd.read_excel(r"E:\SDA\HealthyFoodShop\ShoppingList\food.xlsx", usecols=['Product', 'Category', 'Kcal', 'Carbo(g)', 'Protein(g)', 'Fats(g)', 'Price[PLN]', 'unit', 'Weight[g/ml]', 'Weight_pcs/pack[g]'],)
food = food.fillna(0)

food['Category'] = food['Category'].astype('category')
food['unit'] = food['unit'].astype('category')



food['Number'] = food.groupby(by='Category').cumcount() + 1
food = food.set_index(["Category", "Number"]).sort_index()




if __name__ == '__main__':
	print(food.info(memory_usage='deep'))