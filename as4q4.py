class Bank_account:
	def __init__(self):
		self.balance=0
		print("hello!! welcome to the deposit and withdrawal")
	def deposit(self):
		amount=float(input("enter amount to be deposited: "))
		self.balance += amount
		print("  amount deposited:",amount)
	def withdraw(self):
		amount = float(input("enter amount to be withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("  you withdrew:", amount)
		else:
			print("  insufficient balance  ")
	def display(self):
		print("  net available balance=",self.balance)
s = Bank_account()
s.deposit()
s.withdraw()
s.display()
							