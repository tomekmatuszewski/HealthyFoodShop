import pandas as pd
pd.set_option('display.max_colwidth', 70)

factors = pd.read_excel(r"E:\SDA\HealthyFoodShop\Menu\Factors.xlsx")
factors.index = factors.index + 1

