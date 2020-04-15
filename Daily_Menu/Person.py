from Daily_Menu.utils import *
from Daily_Menu.factors_calc_meal import factors


class Person:
	def __init__(self, username=None, height=None, weight=None, age=None, sex=None, activity=None):
		self.username = username
		self.height = float(height)
		self.weight = float(weight)
		self.age = int(age)
		self.sex = sex
		self.activity = float(activity)
		self.bmi = round(caluculate_bmi(self.weight, self.height), 2)
		self.bmr = round(calculate_bmr(self.weight, self.height, self.age, self.sex), 2)
		self.cmr = round(self.bmr * self.activity, 0)
		self.daily_proteins = round((self.cmr * 0.20) / 4, 0)
		self.daily_fats = round((self.cmr * 0.25) / 9, 0)
		self.daily_carbo = round((self.cmr * 0.55) / 4, 0)
	
	def show_info(self):
		print("-" * 58)
		print("Username: {}, Height: {} cm, Weight: {} kg, Age: {} y.".format(self.username, self.height, self.weight,
		                                                                      self.age))
		print("-" * 58)
		print("|{:<43} {:7.2f} {:<4}|".format('Your max. daily caloric demand is:', self.cmr, 'kcal'))
		print("|{:<46} {:7.2f} {}|".format('Your max. daily requirement for protein:', self.daily_proteins, 'g'))
		print("|{:<46} {:7.2f} {}|".format('Your max. daily requirement for fats:', self.daily_fats, 'g'))
		print("|{:<46} {:7.2f} {}|".format('Your max. daily requirement for carbohydrates:', self.daily_carbo, 'g'))
		print("-" * 58)
		
	@classmethod
	def create_person(cls):
		username = input("Enter your username [max 20 alphanum. characters('.'/'_'/'-' are allowed, min. 2 letters): ")
		username = check_username(username)
		height = input("Enter your height in [cm]: ")
		height = check_height(height)
		weight = input("Enter your weight in [kg]: ")
		weight = check_weight(weight)
		age = input("Enter your age: ")
		age = check_age(age)
		sex = input("Enter your sex [M/F]: ")
		sex = check_sex(sex)
		print("-" * 59)
		print("Daily activities: ")
		for i in range(1, len(factors) + 1):
			print("{} : {}".format(i, factors.loc[i, 'Activity']))
		print("-" * 59)
		activity_index = input("Select number of your activity from list above: ")
		activity_index = check_activity_index(activity_index, factors)
		activity = factors.iloc[int(activity_index) - 1, 1]
		return Person(username, height, weight, age, sex, activity)
