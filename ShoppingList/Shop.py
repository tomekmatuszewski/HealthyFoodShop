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
			self.List[product] = 0
			self.List[product] += numbers
			self.Warehouse[product.name] -= numbers
			
	def remove_product(self,product,numbers):
		if numbers > self.List[product]:
			raise Exception("Not enough products in stock!")
		else:
			self.List[product] -= numbers
			if self.List[product] <= 0:
				del self.List[product]
			
	def check_total_cost(self):
		total_bill = 0
		for k,v in self.List.items():
			total_bill += k.price * v
		return "Total bill cost : " + str(total_bill) + "$"
	
	def Show_Shopping_list(self):
		List_view = ""
		for k, v in self.List.items():
			List_view += "{}----{}pcs.----{}$\n".format(k.name,v,v*k.price)
		return List_view
	
	def __getitem__(self, key):
		return list(self.List.keys())[key]
	
	def __len__(self):
		return len(list(self.List.keys()))



		