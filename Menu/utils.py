import re


def caluculate_bmi(weight, height):
	return round(weight / ((height / 100) ** 2), 2)


def calculate_bmr(weight, height, age, sex):
	if sex == 'M':
		return 9.99 * weight + 6.25 * height - 4.92 * age + 5
	elif sex == 'F':
		return 9.99 * weight + 6.25 * height - 4.92 * age - 161
	else:
		print("Enter 'M' - Male or 'F' - Female")


def check_username(username):
	while re.match(r"^(?=.*[a-zA-Z].*[a-zA-Z])[\w\.-]{,20}$", username) is None:
		print("Wrong username")
		username = input("Enter your username [max 20 alphanum. characters('.'/'_'/'-' are allowed, min. 2 letters): ")
		continue
	else:
		print("Username correct!")
	return username


def check_height(height):
	while re.match(r"^\d\d\d(\.\d)?$", height) is None:
		print("Wrong height!")
		height = input("Enter your height in [cm]: ")
		continue
	return height


def check_weight(weight):
	while re.match(r"^\d\d\d?(\.\d)?$", weight) is None:
		print("Wrong weight!")
		weight = input("Enter your weight in [kg]: ")
		continue
	return weight


def check_age(age):
	while re.match(r"^\d\d\d?$", age) is None:
		print("Wrong age!")
		age = input("Enter your age : ")
		continue
	return age


def check_sex(sex):
	while re.match(r"^M|F$", sex) is None:
		print("Wrong sex!")
		sex = input("Enter your sex : ")
		continue
	return sex


def check_activity_index(activity_index, factors):
	while re.match(r"^[1-{}]$".format(len(factors)), activity_index) is None:
		print("Wrong number!")
		activity_index = input("Select right number of your activity from list above: ")
		continue
	return activity_index
