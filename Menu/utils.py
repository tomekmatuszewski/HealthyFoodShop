def caluculate_bmi(weight, height):
	return round(weight / ((height / 100) ** 2), 2)


def calculate_bmr(weight, height, age, sex):
	if sex == 'M':
		return 9.99 * weight + 6.25 * height - 4.92 * age + 5
	elif sex == 'F':
		return 9.99 * weight + 6.25 * height - 4.92 * age - 161
	else:
		print("Enter 'M' - Male or 'F' - Female")



