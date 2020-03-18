from datetime import datetime
import os
import json

class ShopWarehouse(object):
	
	Warehouse = {}
	
	def __init__(self, name):
		self.name = name
		
	def get_Warehouse(self):
		return self.Warehouse
	
	def add_new_product(self, product, numbers):
		self.Warehouse[product] = 0
		self.Warehouse[product] += numbers
	
	def remove_product(self, product, numbers):
		if product in self.Warehouse.keys():
			self.Warehouse[product] -= numbers
		else:
			raise Exception("PRODUCT OUT OF STOCK!")
	
	def __repr__(self):
		return "Main Warehouse of Healthy Food Shop"
	
	def Show_Products_InStock(self, product):
		return "{} {} {}".format(product.name, self.Warehouse[product], product.unit)


class ShoppingList(ShopWarehouse):
	def __init__(self):
		self.date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
		self.List = {}
	
	def add_product(self, product, numbers):
		if product.name not in self.Warehouse.keys():
			raise Exception("PRODUCT OUT OF STOCK!")
		elif numbers > self.Warehouse[product.name]:
			print("Products on Stock: {}, {} {}".format(product.name,self.Warehouse[product.name],product.unit))
			raise Exception("Not enough products in stock!")
		else:
			if product not in self.List:
				self.List[product] = 0
				self.List[product] += numbers
				self.Warehouse[product.name] -= numbers
			else:
				self.List[product] += numbers
				self.Warehouse[product.name] -= numbers
			
	def remove_product(self,product,numbers):
		if numbers > self.List[product]:
			raise Exception("Not enough products in stock!")
		else:
			self.List[product] -= numbers
			self.Warehouse[product.name] += numbers
			if self.List[product] <= 0:
				del self.List[product]
			
	def check_total_cost(self):
		total_bill = 0
		for k,v in self.List.items():
			total_bill += k.price * v
		return "TOTAL BILL COST : " + str(round(total_bill,2)) + " PLN"
	
	def Show_Shopping_list(self):
		List_view = ""
		counter = 1
		print("-"*72)
		for k,v in self.List.items():
			if counter == len(self.List.keys()):
				List_view += "|{:2}: {:45s}{:5.2f} {:3} : {:5.2f} PLN|".format(str(counter),k.name,v,k.unit,round(v*k.price,2))
			else:
				List_view += "|{:2}: {:45s}{:5.2f} {:3} : {:5.2f} PLN|\n".format(str(counter), k.name, v,k.unit, round(v * k.price,2))
				counter += 1
		print(List_view)
		total_bill = 0
		for k, v in self.List.items():
			total_bill += k.price * v
		print("-" * 72)
		print("{:>61}{:6.2f} PLN|".format("|TOTAL BILL COST : ",round(total_bill, 2)))
		print("{:>72}".format("-" * 30))



	def check_total_calories(self):
		total_kcal = 0
		for k,v in self.List.items():
			if k.unit == 'kg':
				total_kcal += k.calories * v * 10
			else:
				total_kcal += k.calories * v * k.weight/100
		return "TOTAL CALORIES IN CHART : " + str(round(total_kcal,1)) + " kcal"
	
	
	
	def __getitem__(self, key):
		return list(self.List.keys())[key]
	
	def __len__(self):
		return len(list(self.List.keys()))
	
	
	def Print_Bill(self):
		file_path = r"ShoppingList\Bills\Bill_{}.txt".format(datetime.now().strftime("%Y_%m_%d_%H-%M-%S"))
		with open(file_path,'a+') as file:
			List_view = ""
			counter = 1
			file.write("*HEALTHY FOOD SHOP COMPANY*\n")
			file.write("Total receipt:\n")
			file.write("{}\n".format("-" * 72))
			for k, v in self.List.items():
				if counter == len(self.List.keys()):
					List_view += "|{:2}: {:45s}{:>5.2f} {:3} : {:>5.2f} PLN|\n".format(str(counter), k.name, v, k.unit,
					                                                       round(v * k.price, 2))
				else:
					List_view += "|{:2}: {:45s}{:>5.2f} {:3} : {:>5.2f} PLN|\n".format(str(counter), k.name, v, k.unit,
					                                                         round(v * k.price, 2))
					counter += 1
			file.write(List_view)
			total_bill = 0
			for k, v in self.List.items():
				total_bill += k.price * v
			file.write("{}\n".format("-" * 72))
			file.write("{:>61}{:>6.2f} PLN|\n".format("|TOTAL BILL COST : ", round(total_bill, 2)))
			file.write("{:>72}\n\n".format("-" * 30))
			file.write("Nutritional values of products in the basket per 100g / Calories per 100 g: \n\n")
			file.write("{}\n".format("-" * 118))
			for product in self.List.keys():
				file.write("|{:40} - {:55} - {:10} kcal|\n".format(product.name, json.dumps(product.get_nutritional_values()),
				                                          product.get_calories()))
			file.write("{:>118}\n".format("-" * 39))
			file.write("{:>117}\n".format(self.check_total_calories()))
			file.write("{}\n".format("-" * 118))
			file.write("Thank you for shopping and welcome again ! :)")

