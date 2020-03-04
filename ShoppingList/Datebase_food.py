import pandas as pd

food = pd.read_excel('food.xlsx', usecols = ['Product','Kcal','Protein(g)','Fats(g)','Carbo(g)'])

print(food.head())

