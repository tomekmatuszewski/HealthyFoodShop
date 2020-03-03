class ShoppingList(StoreWarehouse):
	def __init__(self, number):
		self.number = number
		self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.List = {}
	
	def add_product(self, product, numbers, magazyn):
		if product.name in magazyn.WarehouseState.keys():
			self.List[product.name] = 0
			self.List[product.name] += numbers
		else:
			print("PRODUCT OUT OF STOCK!")