from datetime import datetime


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
		return "{} {} pcs.".format(product.name, self.Warehouse[product])


class ShoppingList(ShopWarehouse):
	def __init__(self, number):
		self.number = number
		self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.List = {}
	
	def add_product(self, product, numbers):
		if product.name not in self.Warehouse.keys():
			raise Exception("PRODUCT OUT OF STOCK!")
		elif numbers > self.Warehouse[product.name]:
			print("Products on Stock: {}, {} psc.".format(product.name,self.Warehouse[product.name],))
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
		return "TOTAL BILL COST : " + str(total_bill) + "$"
	
	def Show_Shopping_list(self):
		List_view = ""
		counter = 1
		print("-"*65)
		for k,v in self.List.items():
			if counter == len(self.List.keys()):
				List_view += "|{:2}: {:45s}{:3} pcs. {:5}$|".format(counter,k.name,v,v*k.price)
			else:
				List_view += "|{:2}: {:45s}{:3} pcs. {:5}$|\n".format(counter, k.name, v, v * k.price)
				counter += 1
		print(List_view)
		print("-" * 65)
		
	
	def check_total_calories(self):
		total_kcal = 0
		for k,v in self.List.items():
			total_kcal += k.calories * v
		return "TOTAL CALORIES IN CHART : " + str(total_kcal) + "kcal"
	
	
	
	def __getitem__(self, key):
		return list(self.List.keys())[key]
	
	def __len__(self):
		return len(list(self.List.keys()))



		