class Account:

	def __init__(self, file):
		self.file = file
		with open(self.file, 'r') as file:
			self.balance = int(file.read())

	def withdraw(self, amount):
		self.balance = self.balance - amount

	def deposit(self, amount):
		self.balance = self.balance + amount

	def commit(self):
		with open(self.file, 'w') as file:
			file.write(str(self.balance))


class Checking(Account):
	"""This class generates checking account objects"""
	type = "checking"
	
	def __init__(self, file, fee):
		Account.__init__(self,file)
		self.fee = fee
	def transfer(self, amount):
		self.balance = self.balance - amount - self.fee

person1_checking = Checking("person1.txt",1)
person1_checking.transfer(100)
print(person1_checking.balance)
person1_checking.commit()

person2_checking = Checking("person2.txt",1)
person2_checking.transfer(100)
print(person2_checking.balance)
person2_checking.commit()