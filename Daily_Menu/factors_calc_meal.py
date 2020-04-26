import pandas as pd
import os
pd.set_option('display.max_colwidth', 200)

path = os.path.join(os.path.dirname(__file__), "Factors.xlsx")

factors = pd.read_excel(path)
factors.index = factors.index + 1

