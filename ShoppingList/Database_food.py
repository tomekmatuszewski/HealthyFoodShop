import pandas as pd
pd.set_option('display.max_columns', 10)


food = pd.read_excel(r"E:\SDA\HealthyFoodShop\ShoppingList\food.xlsx",usecols = ['Product','Category','Kcal','Carbo(g)','Protein(g)','Fats(g)','Price[PLN]','unit','Weight[g/ml]'],)
food = food.fillna(0)

food['Number'] = food.groupby(by='Category').cumcount()+1
food = food.set_index(["Category","Number"]).sort_index()






