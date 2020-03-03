from datetime import datetime
class ShoppingList():
	def __init__(self, number):
		self.number = number
		self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.List = {}
	
	def add_product(self, product, numbers, magazyn):
		if product.name in magazyn.WarehouseState.keys():
			self.List[product] = 0
			self.List[product] += numbers
		else:
			print("PRODUCT OUT OF STOCK!")
			
	def remove_product(self,product,numbers):
		if numbers > self.List[product]:
			raise Exception("Not enought products on the Shopping List")
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
		