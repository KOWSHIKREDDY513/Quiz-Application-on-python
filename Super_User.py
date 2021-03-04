import json
class User():
	def __init__(self,name,password):
		with open(r'C:\Users\KOWSHIK REDDY\Desktop\CODE\user_accounts.json', 'r+') as user_accounts:
			users = json.load(user_accounts)
			self.name=name
			self.password=password
			if name in users.keys():
				print("An account of this Username already exists.\nPlease Login insted.")
			else:
				users[name] = [password, "PLAYER"]
				user_accounts.seek(0)
				json.dump(users, user_accounts)
				user_accounts.truncate()
				print("Account created for Player successfully!")
class Super_User():
	def __init__(self,name,password):
		with open(r'C:\Users\KOWSHIK REDDY\Desktop\CODE\user_accounts.json', 'r+') as user_accounts:
			users = json.load(user_accounts)
			self.name=name
			self.password=password
			if name in users.keys():
				print("An account of this Username already exists.\nPlease enter the login panel.")
			else:
				users[name] = [password, "ADMIN"]
				user_accounts.seek(0)
				json.dump(users, user_accounts)
				user_accounts.truncate()
				print("Account created for Admin successfully!")
