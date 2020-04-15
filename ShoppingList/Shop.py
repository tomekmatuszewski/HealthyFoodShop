from datetime import datetime
import json
from ShoppingList.utils import check_selected_unit
from ShoppingList.Database_food import food, categories
from ShoppingList.ShoppingItem import ShoppingItem


class ShopWarehouse(object):
	warehouse = {}
	
	def __init__(self, name):
		self.name = name
	
	def get_warehouse(self):
		return self.warehouse
	
	def add_new_product(self, product, numbers):
		self.warehouse[product] = 0
		self.warehouse[product] += numbers
	
	def remove_product(self, product, numbers):
		if product in self.warehouse.keys():
			self.warehouse[product] -= numbers
		else:
			raise Exception("PRODUCT OUT OF STOCK!")
	
	def __repr__(self):
		return "Main Warehouse of Healthy Food Shop"
	
	def show_products_in_stock(self, product):
		return "{} {} {}".format(product.name, self.warehouse[product], product.unit)


class ShoppingList(ShopWarehouse):
	def __init__(self, name):
		super().__init__(name)
		self.date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
		self.cart = {}
	
	def add_product(self, product, quantity):
		while float(quantity) > self.warehouse[product.name] or product.name not in self.warehouse.keys():
			print("Not enough products in stock!")
			if product.unit == "kg":
				quantity = input("Select quantity of products [kg]: ")
				quantity = check_selected_unit(quantity, product)
				continue
			else:
				quantity = input("Select quantity of products [szt]: ")
				quantity = check_selected_unit(quantity, product)
				continue
		else:
			if product not in self.cart:
				self.cart[product] = 0
				self.cart[product] += quantity
				self.warehouse[product.name] -= quantity
			else:
				self.cart[product] += quantity
				self.warehouse[product.name] -= quantity
	
	def remove_product(self, product, numbers):
		self.cart[product] -= numbers
		self.warehouse[product.name] += numbers
		if self.cart[product] <= 0:
			del self.cart[product]
	
	def increase_number_product(self, product, quantity):
		self.cart[product] += quantity
		self.warehouse[product.name] -= quantity
	
	def check_total_cost(self):
		total_bill = 0
		for k, v in self.cart.items():
			total_bill += k.price * v
		return "TOTAL BILL COST : " + str(round(total_bill, 2)) + " PLN"
	
	def show_shopping_list(self):
		list_view = ""
		counter = 1
		print("-" * 72)
		for k, v in self.cart.items():
			if counter == len(self.cart.keys()):
				list_view += "|{:2}: {:45s}{:5.2f} {:3} : {:5.2f} PLN|".format(str(counter), k.name, v, k.unit,
				                                                               round(v * k.price, 2))
			else:
				list_view += "|{:2}: {:45s}{:5.2f} {:3} : {:5.2f} PLN|\n".format(str(counter), k.name, v, k.unit,
				                                                                 round(v * k.price, 2))
				counter += 1
		print(list_view)
		total_bill = 0
		for k, v in self.cart.items():
			total_bill += k.price * v
		print("-" * 72)
		print("{:>61}{:6.2f} PLN|".format("|TOTAL BILL COST : ", round(total_bill, 2)))
		print("{:>72}".format("-" * 30))
	
	def check_total_calories(self):
		total_kcal = 0
		for k, v in self.cart.items():
			if k.unit == 'kg':
				total_kcal += k.calories * v * 10
			else:
				total_kcal += k.calories * v * k.weight / 100
		return "{:>118}".format('|TOTAL CALORIES IN CHART : ' + str(round(total_kcal, 1)) + " kcal|")
	
	def get_nutritional_report(self):
		print("Nutritional values of products in the basket per 100g / Calories per 100 g:")
		print("{}".format("-" * 118))
		for product in self.cart:
			print("|{:40} - {:55} - {:10} kcal|".format(product.name, json.dumps(product.get_nutritional_values()),
			                                            product.get_calories()))
		print("{}".format("-" * 118))
		print(self.check_total_calories())
		print("{:>118}\n".format("-" * 39))
	
	def __getitem__(self, key):
		return list(self.cart.keys())[key]
	
	def __len__(self):
		return len(list(self.cart.keys()))
	
	def print_bill(self):
		file_path = r"ShoppingList\Bills\Bill_{}.txt".format(datetime.now().strftime("%Y_%m_%d_%H-%M-%S"))
		with open(file_path, 'a+') as file:
			list_view = ""
			counter = 1
			file.write("*HEALTHY FOOD SHOP COMPANY*\n")
			file.write("Total receipt:\n")
			file.write("{}\n".format("-" * 72))
			for k, v in self.cart.items():
				if counter == len(self.cart.keys()):
					list_view += "|{:2}: {:45s}{:>5.2f} {:3} : {:>5.2f} PLN|\n".format(str(counter), k.name, v, k.unit,
					                                                                   round(v * k.price, 2))
				else:
					list_view += "|{:2}: {:45s}{:>5.2f} {:3} : {:>5.2f} PLN|\n".format(str(counter), k.name, v, k.unit,
					                                                                   round(v * k.price, 2))
					counter += 1
			file.write(list_view)
			total_bill = 0
			for k, v in self.cart.items():
				total_bill += k.price * v
			file.write("{}\n".format("-" * 72))
			file.write("{:>61}{:>6.2f} PLN|\n".format("|TOTAL BILL COST : ", round(total_bill, 2)))
			file.write("{:>72}\n\n".format("-" * 30))
			file.write("Nutritional values of products in the basket per 100g / Calories per 100 g: \n\n")
			file.write("{}\n".format("-" * 118))
			for product in self.cart.keys():
				file.write(
					"|{:40} - {:55} - {:10} kcal|\n".format(product.name, json.dumps(product.get_nutritional_values()),
					                                        product.get_calories()))
			file.write("{}\n".format("-" * 118))
			file.write("{:>118}\n".format(self.check_total_calories()))
			file.write("{:>118}\n".format("-" * 39))
			file.write("Thank you for shopping and welcome again ! :)")
			
	def fill_up_warehouse(self, kilograms: int, pieces: int):
		for category in categories:
			for number in range(len(food.loc[category])):
				item = ShoppingItem.create_warehouse_item(category, number)
				if item.unit == 'kg':
					self.warehouse[item.name] = kilograms
				else:
					self.warehouse[item.name] = pieces
					
	def show_availability(self, item):
		print("{} : {} {} in Stock, price {} PLN/{}{}".format(item.name, self.warehouse[item.name],
		                                                      item.unit, item.price, item.unit, ", " + str(
				item.weight) + "g/szt" if item.unit == 'szt' else ""))
