from Menu.utils import caluculate_bmi, calculate_bmr

class Person:
	def __init__(self, full_name, height, weight, age, sex, activity):
		self.full_name = full_name
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
		print("*"*150)
		print("Your daily caloric demand is: {} kcal".format(self.cmr))
		print("Your max. daily requirement for protein, fats and carbohydrates is: ")
		print("Proteins - {} g, Fats - {} g, Carbohydrates - {} g.".format(self.daily_proteins, self.daily_fats, self.daily_carbo))