from datetime import datetime
class StoreWarehouse(object):
	
	def __init__(self,name):
		self.name = name
		self.WarehouseState = {}
		
	def get_Warehouse(self):
		return self.WarehouseState
	
	def add_new_product(self,product,numbers):
		self.WarehouseState[product.name] = 0
		self.WarehouseState[product.name] += numbers
		
	def remove_product(self,product,numbers):
		if product.name in self.WarehouseState.keys():
			self.WarehouseState[product.name] -= numbers
		else:
			print("PRODUCT OUT OF STOCK!")



class ShoppingList(StoreWarehouse):
	def __init__(self, number):
		self.number = number
		self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.List = {}
	
	def add_product(self, product,numbers,magazyn):
		if product.name in magazyn.WarehouseState.keys():
			self.List[product.name] = 0
			self.List[product.name] += numbers
		else:
			print("PRODUCT OUT OF STOCK!")
			
	

