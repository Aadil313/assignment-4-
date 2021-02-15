class Port():
	def __init__(self):
		self.str1 = ""
	def my_str(self):
		self.str1 = input()
	def call_str(self):
		print(self.str1.upper())
str1 = Port()
str1.my_str()
str1.call_str()

