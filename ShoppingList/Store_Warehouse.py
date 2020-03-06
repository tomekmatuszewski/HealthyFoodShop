class StoreWarehouse(object):
	
	def __init__(self,name):
		self.name = name
		self.WarehouseState = {}
		
	def get_Warehouse(self):
		return self.WarehouseState
	
	def add_new_product(self,product,numbers):
		self.WarehouseState[product] = 0
		self.WarehouseState[product] += numbers
		
	def remove_product(self,product,numbers):
		if product in self.WarehouseState.keys():
			self.WarehouseState[product] -= numbers
		else:
			raise Exception("PRODUCT OUT OF STOCK!")
		
		
	def __repr__(self):
		return "Main Warehouse of Healthy Food Shop"

			
	def Show_Products_InStock(self,product):
		return "{} {} pcs.".format(product.name,self.WarehouseState[product])



# creating Main Warehouse for Healthy Food Shop !!!!
MainWarehouse = StoreWarehouse("Healthy Food Shop Warehouse")