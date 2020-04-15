import pandas as pd
pd.set_option('display.max_colwidth', 200)

factors = pd.read_excel(r"E:\SDA\HealthyFoodShop\Daily_Menu\Factors.xlsx")
factors.index = factors.index + 1

