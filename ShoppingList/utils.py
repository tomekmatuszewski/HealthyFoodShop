# function to calculate calories based on weight and makro

def get_calories(makro,weight):
	kcal = (makro["Protein"]*4 +  makro["Carbohydrates"]*4 + makro["Fats"]*9)*(weight/100)
	return kcal
	