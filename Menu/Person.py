from Menu.utils import caluculate_bmi, calculate_bmr

class Person:
	def __init__(self, username, height, weight, age, sex, activity):
		self.username = username
		self.height = float(height)
		self.weight = float(weight)
		self.age = int(age)
		self.sex = sex
		self.activity = float(activity)
		self.bmi = round(caluculate_bmi(self.weight, self.height), 2)
		self.bmr = round(calculate_bmr(self.weight, self.height, self.age, self.sex), 2)
		self.cmr = round(self.bmr * self.activity, 0)
		self.daily_proteins = round((self.cmr * 0.20)/4, 0)
		self.daily_fats = round((self.cmr * 0.25)/9, 0)
		self.daily_carbo = round((self.cmr * 0.55)/4, 0)
		
	
	def show_info(self):
		print("-" * 58)
		print("Username: {}, Height: {} cm, Weight: {} kg, Age: {} y.".format(self.username, self.height, self.weight, self.age))
		print("-"*58)
		print("|{:<43} {:7.2f} {:<4}|".format('Your max. daily caloric demand is:', self.cmr, 'kcal'))
		print("|{:<46} {:7.2f} {}|".format('Your max. daily requirement for protein:', self.daily_proteins, 'g'))
		print("|{:<46} {:7.2f} {}|".format('Your max. daily requirement for fats:', self.daily_fats, 'g'))
		print("|{:<46} {:7.2f} {}|".format('Your max. daily requirement for carbohydrates:', self.daily_carbo, 'g'))
		print("-" * 58)
		