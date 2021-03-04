import Play
import Super_User
import Login_and_Logout_and_Add
if __name__ == "__main__":

	while 1:
		print('\n=========WELCOME TO QUIZ ==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print("2. CREATE NEW ACCOUNT FOR PLAYER")
		print("3. CREATE NEW ACCOUNT FOR ADMIN")
		print("4. LOGIN")
		print("5. LOGOUT")
		print("6. ADD A QUESTION")
		print("7. EXIT")
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			Play.Play()
		elif choice == 2:
			name=input("Enter your name is : ")
			password=input("Enter your password is : ")
			Super_User.User(name,password)
		elif choice == 3:
			name=input("Enter your name is : ")
			password=input("Enter your password is : ")
			Super_User.Super_User(name,password)
		elif choice == 4:
			test_name=input("Enter your name is : ")
			test_password=input("Enter your password is : ")
			Login_and_Logout_and_Add.Login(test_name,test_password)
		elif choice == 5:
			Login_and_Logout_and_Add.Logout()
		elif choice == 6:
			Login_and_Logout_and_Add.Add()
		elif choice == 7:
			print("Thank you....Quiz Over")
			break
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
