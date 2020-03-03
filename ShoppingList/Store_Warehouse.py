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

			
	

