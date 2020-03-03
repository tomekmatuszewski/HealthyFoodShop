from datetime import datetime
class ShoppingList():
	def __init__(self, number):
		self.number = number
		self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.List = {}
	
	def add_product(self, product, numbers, magazyn):
		if product not in magazyn.WarehouseState.keys():
			raise Exception("PRODUCT OUT OF STOCK!")
		elif numbers > magazyn.WarehouseState[product]:
			raise Exception("Not enough products on the Shopping List")
		else:
			self.List[product] = 0
			self.List[product] += numbers
			magazyn.WarehouseState[product] -= numbers
			
	def remove_product(self,product,numbers):
		if numbers > self.List[product]:
			raise Exception("Not enough products on the Shopping List")
		else:
			self.List[product] -= numbers
			
	def check_total_cost(self):
		total_bill = 0
		for k,v in self.List.items():
			total_bill += k.price * v
		return str(total_bill) + "$"
	
	def Show_Shopping_list(self):
		List_view = ""
		for k, v in self.List.items():
			List_view += "{}----{}pcs.----{}$\n".format(k.name,v,v*k.price)
		return List_view
	
	def __getitem__(self, key):
		return list(self.List.keys())[key]
	
	def __len__(self):
		return len(list(self.List.keys()))
	
	
		
	
		