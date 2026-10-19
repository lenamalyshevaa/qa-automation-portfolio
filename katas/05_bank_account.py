class BankAccount:
	def __init__(self):
		self.amount = 0

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("сумма должна быть больше нуля") 
		self.amount += amount			
	def withdraw(self, amount):
		if amount <= 0:
			raise ValueError('сумма должна быть больше нуля')
		if self.amount < amount:
			raise ValueError('недостаточно средств')
		self.amount -= amount 
	def balance(self):
		return(self.amount)

 
acc = BankAccount()
acc.deposit(100)
acc.withdraw(30)
print(acc.balance()) 
try:
    acc.withdraw(500)
except ValueError as e:
    print("Поймали:", e)
